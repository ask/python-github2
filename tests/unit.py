# -*- coding: latin-1 -*-
import unittest

from github2.issues import Issue
from github2.client import Github


class ReprTests(unittest.TestCase):
    """__repr__ must return strings, not unicode objects."""

    def test_issue(self):
        """Issues can have non-ASCII characters in the title."""
        i = Issue(title = u'abcdé')
        self.assertEqual(str, type(repr(i)))


class RateLimits(unittest.TestCase):
    """
    How should we handle actual API calls such that tests can run?
    Perhaps the library should support a ~/.python_github2.conf from which to get the auth?
    """
    def test_delays(self):
        import datetime, time
        USERNAME=''
        API_KEY=''
        client = Github(username=USERNAME, api_token=API_KEY, 
            requests_per_second=.5)
        client.users.show('defunkt')
        start = datetime.datetime.now()
        client.users.show('mojombo')
        end = datetime.datetime.now()
        self.assertGreaterEqual((end-start).total_seconds(), 2.0, 
            "Expected .5 reqs per second to require a 2 second delay between calls.")
        