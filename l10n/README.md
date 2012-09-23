Description
===========

This codegolf challenge was to format numbers according to 
the german standard format for money (eG 123.456,0123).

Content
=======

Web
---

Realized via djangos l10n framework a view renders the value 
given in the request URL and returns the localized version.
Different localisations can be realized by setting the requests
accepted languages.

A client which takes the number from the command line sends 
the value to the server and prints the returned result.

dry.py
------

According to pythons DRY (Don't Repeat Yourself) principle the 
locale module is used.

To get different localisations simply set the system locale.

codegolf
--------

Various attempts at code golfing in python 2 and 3:

codegolf_str_py2 (129 bytes): shortest version, accepts strings 
as argument and breaks with negative numbers having a 
multiple of 3 digits.

codegolf_str_py3 (122 bytes): same script but shortened by using 
python3 features.

codegolf2_verbose: verbose and documented version to explain the
concepts used in codegolf_str_py2.

codegolf_num_py2 (131 bytes): a bit longer version of 
codegolf_str_py2 as it also accepts integers, decimals and 
floats.

codegolf_num_py3 (127 bytes): python3 version of codegolf_num_py2

codegolf_negative_py2 (145 bytes): also working for negative numbers

codegolf_negative_py3 (138 bytes): python3 version of 
codegolf_negative_py3
