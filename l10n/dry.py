#!/usr/bin/python

import locale
import sys

def setup(locale_=""):
    """
    set locale for LC_NUMERIC to the given locale

    required setup to use locale.format with numbers. If locale_
    is "", the environment variables are used.
    """
    locale.setlocale(locale.LC_NUMERIC, locale_)

if __name__ == "__main__":
    if len(sys.argv) < 2:
        sys.stderr.write("Usage: %s number [locale]" % sys.argv[0])
        sys.exit(1)
    if len(sys.argv) >= 3:
        setup(sys.argv[2])
    else:
        setup()
    try:
        print(locale.format("%d", int(sys.argv[1]), grouping=True))
    except ValueError:
        print("no int")
    print(locale.format("%f", float(sys.argv[1]), grouping=True))
    
