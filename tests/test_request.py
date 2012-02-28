import unittest

try:
    from urllib.parse import parse_qs  # For Python 3
except ImportError:
    try:
        from urlparse import parse_qs  # NOQA
    except ImportError:  # For Python <2.6
        from cgi import parse_qs  # NOQA

try:
    from nose.tools import (assert_dict_contains_subset, assert_dict_equal)
except ImportError:  # for Python <2.7
    import unittest2

    _binding = unittest2.TestCase('run')
    assert_dict_contains_subset = _binding.assertDictContainsSubset  # NOQA
    assert_dict_equal = _binding.assertDictEqual  # NOQA


from github2 import request


def assert_params(first, second):
    assert_dict_equal(first, parse_qs(second))


def assert_params_contain(first, second):
    assert_dict_contains_subset(first, parse_qs(second))


class TestAuthEncode(unittest.TestCase):
    """Test processing of authentication data"""
    def setUp(self):
        self.r = request.GithubRequest()

    def test_unauthenticated(self):
        assert_params({}, self.r.encode_authentication_data({}))

    def test_access_token(self):
        try:
            self.r.access_token = 'hex string'
            assert_params({'access_token': ['hex string', ]},
                          self.r.encode_authentication_data({}))
        finally:
            self.r.access_token = None

    def test_user_token(self):
        try:
            self.r.username = 'user'
            self.r.api_token = 'hex string'
            token_params = {'login': ['user', ], 'token': ['hex string', ]}
            assert_params(token_params, self.r.encode_authentication_data({}))
        finally:
            self.r.username = self.r.api_token = None


class TestParameterEncoding(unittest.TestCase):
    def setUp(self):
        self.r = request.GithubRequest()
        self.params = {
            'key1': 'value1',
            'key2': 'value2',
        }

    def test_no_parameters(self):
        assert_params({}, self.r.encode_authentication_data({}))

    def test_parameters(self):
        assert_params({'key1': ['value1', ], 'key2': ['value2', ]},
                      self.r.encode_authentication_data(self.params))

    def test_parameters_with_auth(self):
        try:
            self.r.username = 'user'
            self.r.api_token = 'hex string'
            assert_params({'key2': ['value2', ], 'login': ['user', ],
                           'token': ['hex string', ], 'key1': ['value1', ]},
                            self.r.encode_authentication_data(self.params))
        finally:
            self.r.username = ''
            self.r.api_token = ''

    def test_multivalue_parameters(self):
        multivals = {'key': ['value1', 'value2']}
        assert_params(multivals, self.r.encode_authentication_data(multivals))
