#!/Users/troydo42/Development/Web/vegaslivinglife/env/bin/python

# -*- coding: utf-8 -*-
import re
import sys

from jsonpath_rw.bin.jsonpath import entry_point

if __name__ == '__main__':
    sys.argv[0] = re.sub(r'(-script\.pyw?|\.exe)?$', '', sys.argv[0])
    sys.exit(entry_point())
