# -*- coding: utf-8 -*-
# Copyright (C) 2010-2012 Adam Vandenberg <flangy@gmail.com>
#                         James Rowe <jnrowe@gmail.com>
#                         Jeremy Dunck <jdunck@gmail.com>
#                         modocache <modocache@gmail.com>
#
# This file is part of python-github2, and is made available under the 3-clause
# BSD license.  See LICENSE for the full details.

import unittest

from mock import patch
from nose.tools import (eq_, ok_, raises)

from github2.core import (AuthError, repr_string, requires_auth)
from github2.issues import Issue
from github2.client import Github

import utils


class ReprTests(unittest.TestCase):

    """__repr__ must return strings, not unicode objects."""

    def test_issue(self):
        """Issues can have non-ASCII characters in the title."""
        title = 'abcdé'
        i = Issue(title=title)
        eq_(str, type(repr(i)))


class HostSetting(unittest.TestCase):
    def test_default_host(self):
        client = Github()
        eq_(client.request.github_url, 'https://github.com')

    def test_non_standard_host(self):
        client = Github(github_url="http://your-github-enterprise-url.com/")
        eq_(client.request.github_url,
            'http://your-github-enterprise-url.com/')


class RateLimits(utils.HttpMockTestCase):

    """Test API rate-limiting."""

    @patch('github2.request.time.sleep')
    def test_delays(self, sleep):
        """Test calls in quick succession are delayed."""
        client = Github(requests_per_second=.5)
        client.users.show('defunkt')
        client.users.show('mojombo')

        # 0.5 requests per second, means a two second delay
        sleep.assert_called_once_with(2.0)


class BaseDataIter(utils.HttpMockTestCase):

    """Test iter availability of objects."""

    def test_iter(self):
        commit_id = '1c83cde9b5a7c396a01af1007fb7b88765b9ae45'
        commit = self.client.commits.show('ask/python-github2', commit_id)
        ok_('__iter__' in dir(commit))


class BaseDataDict(utils.HttpMockTestCase):

    """Test dict compatibility on objects."""

    def test_getitem(self):
        user = self.client.users.show('defunkt')
        eq_(user['blog'], user.blog)
        eq_(user['company'], user.company)
        eq_(user['email'], user.email)
        eq_(user['location'], user.location)
        eq_(user['login'], user.login)
        eq_(user['name'], user.name)

    @raises(KeyError)
    def test_getitem_failure(self):
        user = self.client.users.show('defunkt')
        ok_(user['invalid_key'])

    def test_setitem(self):
        user = self.client.users.show('defunkt')
        user['blog'] = 'http://example.com'
        eq_(user['blog'], 'http://example.com')

    @raises(KeyError)
    def test_setitem_failure(self):
        user = self.client.users.show('defunkt')
        user['invalid_key'] = 'test'


def test_project_for_user_repo():
    client = Github()
    eq_(client.project_for_user_repo('JNRowe', 'misc-overlay'),
                  'JNRowe/misc-overlay')


def test_repr_string():
    eq_(repr_string('test'), 'test')
    eq_(repr_string('abcdefghijklmnopqrst'), 'abcdefghijklmnopqrst')
    eq_(repr_string('abcdefghijklmnopqrstu'), 'abcdefghijklmnopq...')


class RequiresAuth(utils.HttpMockTestCase):
    @raises(AuthError)
    def test_no_auth(self):
        f = lambda: None
        f.__doc__ = 'test func'
        wrapped = requires_auth(f)
        wrapped(self.client)
