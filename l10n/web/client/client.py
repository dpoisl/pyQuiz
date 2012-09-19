#!/usr/bin/python

import urllib2

def query(value):
    """
    request l10n result from web server
    """
    data = urllib2.urlopen("http://localhost:8000/l10n/number/%s" % value)
    print data.read()

if __name__ == "__main__":
    import sys
    value = sys.argv[1]
    query(value)
