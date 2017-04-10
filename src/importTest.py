#! /usr/bin/env python
from __future__ import print_function
import sys

name = 'libcgns_utils'
print ("Testing if module %s can be imported..." % name)
import_cmd = "import %s" % name
try:
    exec(import_cmd)
except:
    print ("Error: libcgns_utils was not imported correctly")
    sys.exit(1)
# end try

print("Module %s was successfully imported." % name)

