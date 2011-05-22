# -*- coding: latin-1 -*-

import _setup

import sys
import unittest

from github2.issues import Issue
from github2.client import Github

import utils


class ReprTests(unittest.TestCase):
    """__repr__ must return strings, not unicode objects."""

    def test_issue(self):
        """Issues can have non-ASCII characters in the title."""
        title = 'abcdé'
        if sys.version_info[0] == 2:
            title = title.decode("utf-8")
        i = Issue(title=title)
        self.assertEqual(str, type(repr(i)))


class RateLimits(unittest.TestCase):
    """Test API rate-limitting"""
    def setUp(self):
        utils.set_http_mock()

    def tearDown(self):
        utils.unset_http_mock()

    def test_delays(self):
        """Test call delay is at least one second"""
        import datetime
        USERNAME = ''
        API_KEY = ''
        client = Github(username=USERNAME, api_token=API_KEY,
            requests_per_second=.5)
        client.users.show('defunkt')
        start = datetime.datetime.now()
        client.users.show('mojombo')
        end = datetime.datetime.now()

        delta = end - start
        delta_seconds = delta.days * 24 * 60 * 60 + delta.seconds

        self.assertTrue(delta_seconds >= 2,
            "Expected .5 reqs per second to require a 2 second delay between "
            "calls.")
