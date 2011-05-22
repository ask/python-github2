import _setup

import unittest

from nose.tools import (assert_equals, assert_true)

from github2 import request


class TestAuthEncode(unittest.TestCase):
    """Test processing of authentication data"""
    def setUp(self):
        self.r = request.GithubRequest()

    def test_unauthenticated(self):
        assert_equals('', self.r.encode_authentication_data({}))

    def test_access_token(self):
        self.r.access_token = 'hex string'
        assert_equals('access_token=hex+string',
                      self.r.encode_authentication_data({}))
        assert_true('access_token=hex+string' in
                    self.r.encode_authentication_data({'key': 'value'}))
        self.r.access_token = None

    def test_user_token(self):
        self.r.username = 'user'
        self.r.api_token = 'hex string'
        assert_equals('login=user&token=hex+string',
                      self.r.encode_authentication_data({}))
        assert_true('login=user&token=hex+string' in
                    self.r.encode_authentication_data({'key': 'value'}))
        self.r.username = self.r.api_token = None
