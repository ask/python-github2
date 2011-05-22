# -*- coding: latin-1 -*-

import _setup

import datetime
import sys
import unittest

from nose.tools import (assert_equals, assert_true)

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
        assert_equals(str, type(repr(i)))


class RateLimits(utils.HttpMockTestCase):
    """Test API rate-limitting"""
    def test_delays(self):
        """Test call delay is at least one second"""
        client = Github(requests_per_second=.5)
        client.users.show('defunkt')
        start = datetime.datetime.now()
        client.users.show('mojombo')
        end = datetime.datetime.now()

        delta = end - start
        delta_seconds = delta.days * 24 * 60 * 60 + delta.seconds

        assert_true(delta_seconds >= 2,
                    "Expected .5 reqs per second to require a 2 second delay "
                    "between calls.")


def test_project_for_user_repo():
    client = Github()
    assert_equals(client.project_for_user_repo('JNRowe', 'misc-overlay'),
                  'JNRowe/misc-overlay')
