from nose.tools import assert_equals

from github2.request import charset_from_headers


def no_match_test():
    d = {}
    assert_equals("ascii", charset_from_headers(d))


def utf_test():
    d = {'content-type': 'application/json; charset=utf-8'}
    assert_equals("utf-8", charset_from_headers(d))
