#!/tmp/rst2html5/.venv/bin/python
# EASY-INSTALL-ENTRY-SCRIPT: 'rst2html5==1.10.5','console_scripts','rst2html5.py'
__requires__ = 'rst2html5==1.10.5'
import re
import sys
from pkg_resources import load_entry_point

if __name__ == '__main__':
    sys.argv[0] = re.sub(r'(-script\.pyw?|\.exe)?$', '', sys.argv[0])
    sys.exit(
        load_entry_point('rst2html5==1.10.5', 'console_scripts', 'rst2html5.py')()
    )
