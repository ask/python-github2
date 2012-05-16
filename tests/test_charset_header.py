# Copyright (C) 2011-2012 James Rowe <jnrowe@gmail.com>
#
# This file is part of python-github2, and is made available under the 3-clause
# BSD license.  See LICENSE for the full details.

from nose.tools import eq_

from github2.request import charset_from_headers


def no_match_test():
    d = {}
    eq_("ascii", charset_from_headers(d))


def utf_test():
    d = {'content-type': 'application/json; charset=utf-8'}
    eq_("utf-8", charset_from_headers(d))
