#!C:\Users\sujan\Desktop\Filtering-sexist-text\venv\Scripts\python.exe
# EASY-INSTALL-ENTRY-SCRIPT: 'py-thesaurus==1.0.5','console_scripts','py_thesaurus'
__requires__ = 'py-thesaurus==1.0.5'
import re
import sys
from pkg_resources import load_entry_point

if __name__ == '__main__':
    sys.argv[0] = re.sub(r'(-script\.pyw?|\.exe)?$', '', sys.argv[0])
    sys.exit(
        load_entry_point('py-thesaurus==1.0.5', 'console_scripts', 'py_thesaurus')()
    )
