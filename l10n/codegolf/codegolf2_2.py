from locale import *
def f(n,l=""):setlocale(LC_ALL,l);return format("%%.%df"%(len(repr(n))-repr(n).find(".")-1),n,1)
