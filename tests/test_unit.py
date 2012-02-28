# -*- coding: utf-8 -*-

import datetime
import unittest

from nose.tools import (assert_equals, assert_true)

from github2.core import repr_string
from github2.issues import Issue
from github2.client import Github

import utils


class ReprTests(unittest.TestCase):
    """__repr__ must return strings, not unicode objects."""

    def test_issue(self):
        """Issues can have non-ASCII characters in the title."""
        title = 'abcdé'
        i = Issue(title=title)
        assert_equals(str, type(repr(i)))


class HostSetting(unittest.TestCase):
    def test_default_host(self):
        client = Github()
        assert_equals(client.request.github_url, 'https://github.com')

    def test_non_standard_host(self):
        client = Github(github_url="http://git.gree-dev.net/")
        assert_equals(client.request.github_url, 'http://git.gree-dev.net/')


class RateLimits(utils.HttpMockTestCase):
    """Test API rate-limitting"""
    def test_delays(self):
        """Test call delay is at least one second"""
        client = Github(requests_per_second=.5)
        client.users.show('defunkt')
        start = datetime.datetime.utcnow()
        client.users.show('mojombo')
        end = datetime.datetime.utcnow()

        delta = end - start
        delta_seconds = delta.days * 24 * 60 * 60 + delta.seconds

        assert_true(delta_seconds >= 2,
                    "Expected .5 reqs per second to require a 2 second delay "
                    "between calls.")


class BaseDataIter(utils.HttpMockTestCase):
    """Test iter availability of objects"""
    def test_iter(self):
        commit_id = '1c83cde9b5a7c396a01af1007fb7b88765b9ae45'
        commit = self.client.commits.show('ask/python-github2', commit_id)
        assert_true('__iter__' in dir(commit))


class BaseDataDict(utils.HttpMockTestCase):
    """Test __getitem__ availability on objects"""
    def test_getitem(self):
        user = self.client.users.show('defunkt')
        assert_equals(user['blog'], user.blog)
        assert_equals(user['company'], user.company)
        assert_equals(user['email'], user.email)
        assert_equals(user['location'], user.location)
        assert_equals(user['login'], user.login)
        assert_equals(user['name'], user.name)


def test_project_for_user_repo():
    client = Github()
    assert_equals(client.project_for_user_repo('JNRowe', 'misc-overlay'),
                  'JNRowe/misc-overlay')


def test_repr_string():
    assert_equals(repr_string('test'), 'test')
    assert_equals(repr_string('abcdefghijklmnopqrst'), 'abcdefghijklmnopqrst')
    assert_equals(repr_string('abcdefghijklmnopqrstu'), 'abcdefghijklmnopq...')
