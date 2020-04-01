# Copyright (C) 2018 Semicon Networks
# Author: Hans Roh <hansroh@gmail.com>

__version__ = 2

import os
import sys
import subprocess
from getpass import getpass
from hashlib import md5
import os, struct
from ..termcolor import tc
from .. import ifaces
import time
ENCRYPTED = None
LICENSE_FILE = None
POSITION = 0

def configure (key, name = '.license'):
    global ENCRYPTED, LICENSE_FILE, POSITION
    ENCRYPTED = md5 (key.encode ()).hexdigest ()
    POSITION = (sum ([ord (c) for c in ENCRYPTED]) * 1978524790) % 1008
    LICENSE_FILE = os.path.join (os.path.dirname (os.path.join (os.getcwd (), sys.argv [0])), name)

def hide_file (filename):
    import win32file
    import win32con
    import win32api
    flags = win32file.GetFileAttributesW(filename)
    win32file.SetFileAttributes(filename,
        win32con.FILE_ATTRIBUTE_HIDDEN | flags)

def check_license ():
    global ENCRYPTED, LICENSE_FILE
    assert ENCRYPTED and LICENSE_FILE, 'call license.configure first'

    if not os.path.isfile (LICENSE_FILE):
        return "cannot find license"
    try:
        hwid = ifaces.get_hwid ().lower ()
    except subprocess.CalledProcessError:
        return "cannot get hardware ID, maybe run wiht root permission"
    key = md5 ('{}:{}'.format (ENCRYPTED, hwid).encode ()).digest ()
    with open (LICENSE_FILE, 'rb') as f:
        data = f.read ()
    ver = struct.unpack ('H', data [:2])
    s = sum (struct.unpack ('BBB', data [2:5])) + 5 + POSITION
    if data [s:s + 16] != key:
        return "invalid license"
    a, b = struct.unpack ('II', data [s+16:s+24])
    if int (time.time ()) > a + b:
        return "license expired"

def create_license (uuid = None):
    global ENCRYPTED, LICENSE_FILE
    assert ENCRYPTED and LICENSE_FILE, 'call license.configure first'

    if os.path.isfile (LICENSE_FILE):
        with open (LICENSE_FILE, 'rb') as f:
            data = f.read ()
        lns = struct.unpack ('HBBB', data [:5])
        data = data [5:]
        ver = lns [0]
        name = data [:lns [1]].decode (); data = data [lns [1]:]
        org = data [:lns [2]].decode (); data = data [lns [2]:]
        contact = data [:lns [3]].decode (); data = data [lns [3]:]

        print (check_license ())
        print (tc.ok ("\nLicense Information\n"))
        print (tc.echo ("  Organization:"), org)
        print (tc.echo ("  Point of Contact Name:"), name)
        print (tc.echo ("  Email/Phone Number:"), contact)
        print (tc.echo ("\n  License Status:"), check_license () and tc.error ('INVALID') or tc.ok ('VALID'))

        if input ('\nDo you want to replace to new license? (n/y) ') != 'y':
            sys.exit ()

    print ()
    org, name, contact = None, None, None
    while not org:
        org = input ('Enter Organization Name: ')
        if len (org.encode ()) > 64:
            print ('  too long, should be within 64 bytes')
            org = None
    while not name:
        name = input ('Enter Point of Contact Name: ')
        if len (name.encode ()) > 64:
            print ('  too long, should be within 64 bytes')
            name = None
    while not contact:
        contact = input ('Enter Email or Phone Number: ')
        if len (contact.encode ()) > 32:
            print ('  too long, should be within 32 bytes')
            contact = None

    name = name.encode ()
    org = org.encode ()
    contact = contact.encode ()

    premble = struct.pack ('H', __version__) + struct.pack ('B', len (name)) + struct.pack ('B', len (org)) + struct.pack ('B', len (contact)) + name + org + contact
    for i in range (3):
        password = getpass('\nEnter License Permit Key: ')
        try:
            password, period = password.split ('/', 1)
        except ValueError:
            period = 0
        passed = False
        try:
            period = int (period)
        except ValueError:
            print ("  incorrect key, try again...")
            continue
        if md5 (password.encode ()).hexdigest () == ENCRYPTED:
            passed = True
            break
        print ("  incorrect key, try again...")

    if not passed:
        return "incorrect key"

    try:
        hwid = uuid or ifaces.get_hwid ()
        hwid = hwid.lower ()
    except subprocess.CalledProcessError:
        return "cannot get hardware ID, maybe run wiht root permission"
    key = md5 ('{}:{}'.format (ENCRYPTED, hwid).encode ()).digest () + struct.pack ('I', period * 24 * 3600) + struct.pack ('I', int (time.time ()))
    data = premble + os.urandom (POSITION) + key + os.urandom (1024 - 20 - POSITION)
    with open (LICENSE_FILE, 'wb') as f:
        f.write (data)
    os.chmod (LICENSE_FILE, 0o644)
