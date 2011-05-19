import sys

from nose.tools import assert_equals

# Forcibly insert path for `setup.py build` output, so that we import from the
# ``2to3`` converted sources
sys.path.insert(0, 'build/lib')

from github2.request import charset_from_headers


def no_match_test():
    d = {}
    assert_equals("ascii", charset_from_headers(d))

def utf_test():
    d = {'content-type': 'application/json; charset=utf-8'}
    assert_equals("utf-8", charset_from_headers(d))
