import os

from django.conf import settings

MOCK_SEARCH_KEYS_RESPONSE = [
    {
        'algo': u'1',
        'date': u'1311475606',
        'expires': u'1643601600',
        'keyid': u'607138F1AECC5A5CA31CB7715F3F7F75D210724D',
        'length': u'2048',
        'type': u'pub',
        'uids': [u'Roberto Rosario <roberto.rosario.gonzalez@gmail.com>']
    }
]

TEST_DETACHED_SIGNATURE = os.path.join(
    settings.BASE_DIR, 'apps', 'django_gpg', 'tests', 'contrib',
    'test_files', 'test_file.txt.asc'
)

TEST_FILE = os.path.join(
    settings.BASE_DIR, 'apps', 'django_gpg', 'tests', 'contrib',
    'test_files', 'test_file.txt'
)

TEST_KEY_PRIVATE_DATA = '''-----BEGIN PGP PRIVATE KEY BLOCK-----
Version: GnuPG v1

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
8aeg3z/W+YctdRt81bi5isgM+oML9LAQ
=JZ5G
-----END PGP PRIVATE KEY BLOCK-----'''

TEST_KEY_PRIVATE_ID = '4125E9C571F378AC'
TEST_KEY_PRIVATE_FINGERPRINT = '6A24574E0A35004CDDFD22704125E9C571F378AC'
TEST_KEY_PRIVATE_PASSPHRASE = 'testpassphrase'

TEST_KEY_PUBLIC_FILE_PATH = os.path.join(
    settings.BASE_DIR, 'apps', 'django_gpg', 'tests', 'contrib',
    'test_files', 'key0x5F3F7F75D210724D.asc'
)
TEST_KEY_PUBLIC_ID = '5F3F7F75D210724D'

TEST_KEYSERVERS = ['pool.sks-keyservers.net']

TEST_SEARCH_UID = 'Roberto Rosario'
TEST_SEARCH_FINGERPRINT = '607138F1AECC5A5CA31CB7715F3F7F75D210724D'

TEST_SIGNED_FILE = os.path.join(
    settings.BASE_DIR, 'apps', 'django_gpg', 'tests', 'contrib',
    'test_files', 'test_file.txt.gpg'
)
TEST_SIGNED_FILE_CONTENT = b'test_file.txt\n'

TEST_RECEIVE_KEY = '''-----BEGIN PGP PUBLIC KEY BLOCK-----
Version: SKS 1.1.5
Comment: Hostname: keyserver.deuxpi.ca

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
z2RCi1bkJgTu3RihfhbYE1t94fJO17Mq6O845QF2vWkuF4WWREGX7/Zr1PZ1UhR6Y0gnbfS+
OBkd+PLTk6NxQb8D4ctXvR89iF0EZsWEz+ssonM4c9MwLl2jQ7o6CzeeI1OAy3xJwOvLGhWR
3hQxL5++k1LG0fmOsLEyWAMCQH5kqTSDxAC1mcdBYuSq4B9oQjZbuWXLEE9geU0HZK5HYJJj
doqSfWKvH5LAz0zLKiHdYFlsIGPjT/A7XtSnbbE5MKwUdYJjSkfwZbWqUCrzvY6RFnWhXfEE
nIfmLKfco1kKVmrYBvPp/qxq+Ti8V8KTQJjTXngg31OAycQv3l00gVNWNWx8aybm77UUnxl3
yuxe6RavfCMUZo6hIDSOUJiw8KI8dj9GS8zn+jZ6ERAE8/v4TDp0X/jR/wAAD73O+wEQAAEB
AAAAAAAAAAAAAAAA/9j/4AAQSkZJRgABAQAAAQABAAD/2wBDAAgGBgcGBQgHBwcJCQgKDBQN
DAsLDBkSEw8UHRofHh0aHBwgJC4nICIsIxwcKDcpLDAxNDQ0Hyc5PTgyPC4zNDL/2wBDAQkJ
CQwLDBgNDRgyIRwhMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIy
MjIyMjIyMjL/wAARCACKAIMDASIAAhEBAxEB/8QAHwAAAQUBAQEBAQEAAAAAAAAAAAECAwQF
BgcICQoL/8QAtRAAAgEDAwIEAwUFBAQAAAF9AQIDAAQRBRIhMUEGE1FhByJxFDKBkaEII0Kx
wRVS0fAkM2JyggkKFhcYGRolJicoKSo0NTY3ODk6Q0RFRkdISUpTVFVWV1hZWmNkZWZnaGlq
c3R1dnd4eXqDhIWGh4iJipKTlJWWl5iZmqKjpKWmp6ipqrKztLW2t7i5usLDxMXGx8jJytLT
1NXW19jZ2uHi4+Tl5ufo6erx8vP09fb3+Pn6/8QAHwEAAwEBAQEBAQEBAQAAAAAAAAECAwQF
BgcICQoL/8QAtREAAgECBAQDBAcFBAQAAQJ3AAECAxEEBSExBhJBUQdhcRMiMoEIFEKRobHB
CSMzUvAVYnLRChYkNOEl8RcYGRomJygpKjU2Nzg5OkNERUZHSElKU1RVVldYWVpjZGVmZ2hp
anN0dXZ3eHl6goOEhYaHiImKkpOUlZaXmJmaoqOkpaanqKmqsrO0tba3uLm6wsPExcbHyMnK
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
9iQqDpPWYJVqPczCuq6IzuzYZ3DXPOw=
=3sHD
-----END PGP PUBLIC KEY BLOCK-----'''
