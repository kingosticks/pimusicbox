#!/usr/bin/env python
from __future__ import unicode_literals, print_function

import io, sys

PY2 = sys.version_info[0] == 2
if PY2:
    import ConfigParser as configparser
else:
    import configparser


config = configparser.RawConfigParser()

for filename in sys.argv[1:]:
    with io.open(filename, 'rb') as filehandle:
        config.readfp(filehandle)

print('unset INI; declare -A INI;')
for sec in config.sections():
    for key, val in config.items(sec):
        print(b'INI[%s__%s]="%s"' % (bytes(sec), bytes(key), bytes(val)))
