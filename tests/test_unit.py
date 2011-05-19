# -*- coding: latin-1 -*-
import os
import sys
import unittest

# Forcibly insert path for `setup.py build` output, so that we import from the
# ``2to3`` converted sources
sys.path.insert(0, 'build/lib')

from email import message_from_file

import httplib2

from github2.issues import Issue
from github2.client import Github
from github2.request import charset_from_headers


HTTP_DATA_DIR = "tests/data/"


class HttpMock(object):
    """Simple Http mock that returns saved entries

    Implementation tests should never span network boundaries
    """

    def __init__(self, cache=None, timeout=None, proxy_info=None):
        pass

    def request(self, uri, method='GET', body=None, headers=None,
                redirections=5, connection_type=None):
        file = os.path.join(HTTP_DATA_DIR, httplib2.safename(uri))
        if os.path.exists(file):
            response = message_from_file(open(file))
            headers = httplib2.Response(response)
            body = response.get_payload().encode(charset_from_headers(headers))
            return (headers, body)
        else:
            return (httplib2.Response({"status": "404"}),
                    "Resource unavailable from test data store")


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
        self.old_httplib2 = httplib2.Http
        httplib2.Http = HttpMock

    def tearDown(self):
        httplib2.Http = self.old_httplib2

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
