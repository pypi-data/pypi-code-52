from multiprocessing import Process, Manager, Lock
import subprocess
import signal
import os
import sys
import logging
import json
import yaml
import codecs
import time
import tempfile
import inspect
import warnings
import re
import math
from threading import Thread, Event
import unicodedata
import hashlib
#from fcntl import fcntl, F_GETFL, F_SETFL
#from os import O_NONBLOCK, read
import codecs

DEBUG = False
INTERRUPT_TIME = 2.0  # seconds -- do not want to constantly interrupt the child process
LIVELOG_TIME = 0.1

class StimelaCabRuntimeError(RuntimeError):
    pass


CPUS = 1


def _logger(level=0, logfile=None):

    if logfile and not logging.getLogger("STIMELA"):
        logging.basicConfig(filename=logfile)
    elif not logging.getLogger("STIMELA"):
        logging.basicConfig()

    LOGL = {"0": "INFO",
            "1": "DEBUG",
            "2": "ERROR",
            "3": "CRITICAL"}

    log = logging.getLogger("STIMELA")
    log.setLevel(eval("logging."+LOGL[str(level)]))

    return log


def assign(key, value):
    frame = inspect.currentframe().f_back
    frame.f_globals[key] = value


def xrun(command, options, log=None, _log_container_as_started=False, logfile=None, timeout=-1, kill_callback=None):
    """
        Run something on command line.

        Example: _run("ls", ["-lrt", "../"])
    """
    if "LOGFILE" in os.environ and logfile is None:
        logfile = os.environ["LOGFILE"] # superceed if not set  

    # skip lines from previous log files
    if logfile is not None and os.path.exists(logfile):
        with codecs.open(logfile, "r", encoding="UTF-8",
                         errors="ignore", buffering=0) as foutlog:
            lines = foutlog.readlines()
            prior_log_bytes_read = foutlog.tell()
    else: # not existant, create
        prior_log_bytes_read = 0
        if logfile is not None and not os.path.exists(logfile):
            with codecs.open(logfile, "w+", encoding="UTF-8",
                             errors="ignore", buffering=0) as foutlog:
                pass

    cmd = " ".join([command] + list(map(str, options)))

    def _remove_ctrls(msg):
        import re
        ansi_escape = re.compile(r'\x1B[@-_][0-?]*[ -/]*[@-~]')
        return ansi_escape.sub('', msg)

    def _print_info(msg):
        if msg is None:
            return
        msg = _remove_ctrls(msg)
        if msg.strip() == "": return
        if log:
            try:
                log.info(msg.rstrip('\n'))
            except UnicodeError:
                log.warn("Log contains unicode and will not be printed")
        else:
            try:
                print(msg),
            except UnicodeError:
                print("Log contains unicode and will not be printed")

    def _print_warn(msg):
        if msg is None:
            return
        msg = _remove_ctrls(msg)
        if msg.strip() == "": return
        if log:
            try:
                log.info(msg.rstrip('\n'))
            except UnicodeError:
                log.warn("Log contains unicode and will not be printed")
        else:
            try:
                print(msg),
            except UnicodeError:
                print("Log contains unicode and will not be printed")


    _print_info(u"Running: {0:s}".format(cmd))

    sys.stdout.flush()
    starttime = time.time()
    process = p = None
    stop_log_printer = Event()

    try:
        foutname = os.path.join("/tmp", "stimela_output_{0:s}_{1:f}".format(
            hashlib.md5(cmd.encode('utf-8')).hexdigest(), starttime))


        p = process = subprocess.Popen(cmd,
                                       shell=True)
        kill_callback = kill_callback or p.kill

        def clock_killer(p):
            while process.poll() is None and (timeout >= 0):
                currenttime = time.time()
                if (currenttime - starttime < timeout):
                    DEBUG and _print_warn(u"Clock Reaper: has been running for {0:f}, must finish in {1:f}".format(
                        currenttime - starttime, timeout))
                else:
                    _print_warn(
                        u"Clock Reaper: Timeout reached for '{0:s}'... sending the KILL signal".format(cmd))
                    kill_callback()
                time.sleep(INTERRUPT_TIME)

        def log_reader(logfile, stop_event):
            bytes_read = prior_log_bytes_read # skip any previous runs' output
            while not stop_event.isSet():
                if logfile is not None and os.path.exists(logfile):
                    with codecs.open(logfile, "r", encoding="UTF-8",
                                     errors="ignore", buffering=0) as foutlog:
                        foutlog.seek(bytes_read, 0)
                        lines = foutlog.readlines()
                        bytes_read = foutlog.tell()
                        for line in lines:
                            line and _print_info(line)
                time.sleep(LIVELOG_TIME) # wait for the log to go to disk

        Thread(target=clock_killer, args=tuple([p])).start()
        if log is not None:
            # crucial - child process should not write to stdout unless it is
            # the container process itself
            Thread(target=log_reader, args=tuple([logfile, stop_log_printer])).start()


        while (process.poll() is None):
            currenttime = time.time()
            DEBUG and _print_info(
                u"God mode on: has been running for {0:f}".format(currenttime - starttime))
            # this is probably not ideal as it interrupts the process every few seconds,
            time.sleep(INTERRUPT_TIME)
            # check whether there is an alternative with a callback

        assert hasattr(
            process, "returncode"), "No returncode after termination!"
    finally:
        stop_log_printer.set()
        if (process is not None) and process.returncode:
            raise StimelaCabRuntimeError(
                '%s: returns errr code %d' % (command, process.returncode))


def readJson(conf):
    with open(conf, "r") as _std:
        jdict = yaml.safe_load(_std)
        return jdict


def writeJson(config, dictionary):
    with codecs.open(config, 'w', 'utf8') as std:
        std.write(json.dumps(dictionary, ensure_ascii=False))


def get_Dockerfile_base_image(image):

    if os.path.isfile(image):
        dockerfile = image
    else:
        dockerfile = "{:s}/Dockerfile".format(image)

    with open(dockerfile, "r") as std:
        _from = ""
        for line in std.readlines():
            if line.startswith("FROM"):
                _from = line

    return _from


def change_Dockerfile_base_image(path, _from, label, destdir="."):
    if os.path.isfile(path):
        dockerfile = path
        dirname = os.path.dirname(path)
    else:
        dockerfile = "{:s}/Dockerfile".format(path)
        dirname = path

    with open(dockerfile, "r") as std:
        lines = std.readlines()
        for line in lines:
            if line.startswith("FROM"):
                lines.remove(line)

    temp_dir = tempfile.mkdtemp(
        prefix="tmp-stimela-{:s}-".format(label), dir=destdir)
    xrun(
        "cp", ["-r", "{:s}/Dockerfile {:s}/src".format(dirname, dirname), temp_dir])

    dockerfile = "{:s}/Dockerfile".format(temp_dir)

    with open(dockerfile, "w") as std:
        std.write("{:s}\n".format(_from))

        for line in lines:
            std.write(line)

    return temp_dir, dockerfile


def get_base_images(logfile, index=1):

    with opEn(logfile, "r") as std:
        string = std.read()

    separator = "[================================DONE==========================]"

    log = string.split(separator)[index-1]

    images = []

    for line in log.split("\n"):
        if line.find("<=BASE_IMAGE=>") > 0:
            tmp = line.split("<=BASE_IMAGE=>")[-1]
            image, base = tmp.split("=")
            images.append((image.strip(), base))

    return images


def icasa(taskname, mult=None, clearstart=False, loadthese=[], **kw0):
    """ 
      runs a CASA task given a list of options.
      A given task can be run multiple times with a different options, 
      in this case the options must be parsed as a list/tuple of dictionaries via mult, e.g 
      icasa('exportfits',mult=[{'imagename':'img1.image','fitsimage':'image1.fits},{'imagename':'img2.image','fitsimage':'image2.fits}]). 
      Options you want be common between the multiple commands should be specified as key word args.
    """

    # create temp directory from which to run casapy
    td = tempfile.mkdtemp(dir='.')
    # we want get back to the working directory once casapy is launched
    cdir = os.path.realpath('.')

    # load modules in loadthese
    _load = ""
    if "os" not in loadthese or "import os" not in loadthese:
        loadthese.append("os")

    if loadthese:
        exclude = filter(lambda line: line.startswith("import")
                         or line.startswith("from"), loadthese)
        for line in loadthese:
            if line not in exclude:
                line = "import %s" % line
            _load += "%s\n" % line

    if mult:
        if isinstance(mult, (tuple, list)):
            for opts in mult:
                opts.update(kw0)
        else:
            mult.upadte(kw0)
            mult = [mult]
    else:
        mult = [kw0]

    run_cmd = """ """
    for kw in mult:
        task_cmds = []
        for key, val in kw.items():
            if isinstance(val, (str, unicode)):
                val = '"%s"' % val
            task_cmds .append('%s=%s' % (key, val))

        task_cmds = ", ".join(task_cmds)
        run_cmd += """ 
%s
os.chdir('%s')
%s
%s(%s)
""" % (_load, cdir, "clearstart()" if clearstart else "", taskname, task_cmds)

    tf = tempfile.NamedTemporaryFile(suffix='.py')
    tf.write(run_cmd)
    tf.flush()
    t0 = time.time()
    # all logging information will be in the pyxis log files
    print("Running {}".format(run_cmd))
    xrun("cd", [td, "&& casa --nologger --log2term --nologfile -c", tf.name])

    # log taskname.last
    task_last = '%s.last' % taskname
    if os.path.exists(task_last):
        with opEn(task_last, 'r') as last:
            print('%s.last is: \n %s' % (taskname, last.read()))

    # remove temp directory. This also gets rid of the casa log files; so long suckers!
    xrun("rm", ["-fr ", td, task_last])
    tf.close()


def stack_fits(fitslist, outname, axis=0, ctype=None, keep_old=False, fits=False):
    """ Stack a list of fits files along a given axiis.

       fitslist: list of fits file to combine
       outname: output file name
       axis: axis along which to combine the files
       fits: If True will axis FITS ordering axes
       ctype: Axis label in the fits header (if given, axis will be ignored)
       keep_old: Keep component files after combining?
    """
    import numpy
    try:
        import pyfits
    except ImportError:
        warnings.warn(
            "Could not find pyfits on this system. FITS files will not be stacked")
        sys.exit(0)

    hdu = pyfits.open(fitslist[0])[0]
    hdr = hdu.header
    naxis = hdr['NAXIS']

    # find axis via CTYPE key
    if ctype is not None:
        for i in range(1, naxis+1):
            if hdr['CTYPE%d' % i].lower().startswith(ctype.lower()):
                axis = naxis - i  # fits to numpy convention
    elif fits:
        axis = naxis - axis

    fits_ind = abs(axis-naxis)
    crval = hdr['CRVAL%d' % fits_ind]

    imslice = [slice(None)]*naxis
    _sorted = sorted([pyfits.open(fits) for fits in fitslist],
                     key=lambda a: a[0].header['CRVAL%d' % (naxis-axis)])

    # define structure of new FITS file
    nn = [hd[0].header['NAXIS%d' % (naxis-axis)] for hd in _sorted]
    shape = list(hdu.data.shape)
    shape[axis] = sum(nn)
    data = numpy.zeros(shape, dtype=float)

    for i, hdu0 in enumerate(_sorted):
        h = hdu0[0].header
        d = hdu0[0].data
        imslice[axis] = range(sum(nn[:i]), sum(nn[:i+1]))
        data[imslice] = d
        if crval > h['CRVAL%d' % fits_ind]:
            crval = h['CRVAL%d' % fits_ind]

    # update header
    hdr['CRVAL%d' % fits_ind] = crval
    hdr['CRPIX%d' % fits_ind] = 1

    pyfits.writeto(outname, data, hdr, clobber=True)
    print("Successfully stacked images. Output image is %s" % outname)

    # remove old files
    if not keep_old:
        for fits in fitslist:
            os.system('rm -f %s' % fits)


def substitute_globals(string, globs=None):
    sub = set(re.findall('\{(.*?)\}', string))
    globs = globs or inspect.currentframe().f_back.f_globals
    if sub:
        for item in map(str, sub):
            string = string.replace("${%s}" % item, globs[item])
        return string
    else:
        return False


def get_imslice(ndim):
    imslice = []
    for i in xrange(ndim):
        if i < ndim-2:
            imslice.append(0)
        else:
            imslice.append(slice(None))

    return imslice


def addcol(msname, colname=None, shape=None,
           data_desc_type='array', valuetype=None, init_with=0, **kw):
    """ add column to MS 
        msanme : MS to add colmn to
        colname : column name
        shape : shape
        valuetype : data type 
        data_desc_type : 'scalar' for scalar elements and array for 'array' elements
        init_with : value to initialise the column with 
    """
    import numpy
    import pyrap.tables
    tab = pyrap.tables.table(msname, readonly=False)

    try:
        tab.getcol(colname)
        print('Column already exists')

    except RuntimeError:
        print('Attempting to add %s column to %s' % (colname, msname))

        from pyrap.tables import maketabdesc
        valuetype = valuetype or 'complex'

        if shape is None:
            dshape = list(tab.getcol('DATA').shape)
            shape = dshape[1:]

        if data_desc_type == 'array':
            from pyrap.tables import makearrcoldesc
            # God forbid this (or the TIME) column doesn't exist
            coldmi = tab.getdminfo('DATA')
            coldmi['NAME'] = colname.lower()
            tab.addcols(maketabdesc(makearrcoldesc(
                colname, init_with, shape=shape, valuetype=valuetype)), coldmi)

        elif data_desc_type == 'scalar':
            from pyrap.tables import makescacoldesc
            coldmi = tab.getdminfo('TIME')
            coldmi['NAME'] = colname.lower()
            tab.addcols(maketabdesc(makescacoldesc(
                colname, init_with, valuetype=valuetype)), coldmi)

        print('Column added successfuly.')

        if init_with:
            nrows = dshape[0]

            rowchunk = nrows//10 if nrows > 1000 else nrows
            for row0 in range(0, nrows, rowchunk):
                nr = min(rowchunk, nrows-row0)
                dshape[0] = nr
                tab.putcol(colname, numpy.ones(
                    dshape, dtype=valuetype)*init_with, row0, nr)

    tab.close()


def sumcols(msname, col1=None, col2=None, outcol=None, cols=None, suntract=False):
    """ add col1 to col2, or sum columns in 'cols' list.
        If subtract, subtract col2 from col1
    """
    from pyrap.tables import table

    tab = table(msname, readonly=False)
    if cols:
        data = 0
        for col in cols:
            data += tab.getcol(col)
    else:
        if subtract:
            data = tab.getcol(col1) - tab.getcol(col2)
        else:
            data = tab.getcol(col1) + tab.getcol(col2)

    rowchunk = nrows//10 if nrows > 1000 else nrows
    for row0 in range(0, nrows, rowchunk):
        nr = min(rowchunk, nrows-row0)
        tab.putcol(outcol, data[row0:row0+nr], row0, nr)

    tab.close()


def copycol(msname, fromcol, tocol):
    from pyrap.tables import table

    tab = table(msname, readonly=False)
    data = tab.getcol(fromcol)
    if tocol not in tab.colnames():
        addcol(msname, tocol)

    nrows = tab.nrows()
    rowchunk = nrows//10 if nrows > 5000 else nrows
    for row0 in range(0, nrows, rowchunk):
        nr = min(rowchunk, nrows-row0)
        tab.putcol(tocol, data[row0:row0+nr], row0, nr)

    tab.close()


def cab_dict_update(dictionary, key=None, value=None, options=None):
    if options is None:
        options = {key: value}
    for key, value in options.items():
        dictionary[key] = dictionary.pop(key, None) or value
    return dictionary


def compute_vis_noise(msname, sefd, spw_id=0):
    """Computes nominal per-visibility noise"""
    from pyrap.tables import table

    tab = table(msname)
    spwtab = table(msname + "/SPECTRAL_WINDOW")

    freq0 = spwtab.getcol("CHAN_FREQ")[spw_id, 0]
    wavelength = 300e+6/freq0
    bw = spwtab.getcol("CHAN_WIDTH")[spw_id, 0]
    dt = tab.getcol("EXPOSURE", 0, 1)[0]
    dtf = (tab.getcol("TIME", tab.nrows()-1, 1)-tab.getcol("TIME", 0, 1))[0]

    # close tables properly, else the calls below will hang waiting for a lock...
    tab.close()
    spwtab.close()

    print(">>> %s freq %.2f MHz (lambda=%.2fm), bandwidth %.2g kHz, %.2fs integrations, %.2fh synthesis" % (
        msname, freq0*1e-6, wavelength, bw*1e-3, dt, dtf/3600))
    noise = sefd/math.sqrt(abs(2*bw*dt))
    print(">>> SEFD of %.2f Jy gives per-visibility noise of %.2f mJy" %
          (sefd, noise*1000))

    return noise
