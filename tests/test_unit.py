# -*- coding: utf-8 -*-
# Copyright (C) 2010-2012 Adam Vandenberg <flangy@gmail.com>
#                         James Rowe <jnrowe@gmail.com>
#                         Jeremy Dunck <jdunck@gmail.com>
#                         modocache <modocache@gmail.com>
#
# This file is part of python-github2, and is made available under the 3-clause
# BSD license.  See LICENSE for the full details.

import datetime
import unittest

from nose.tools import (eq_, ok_)

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

    """Test API rate-limitting."""

    def test_delays(self):
        """Test call delay is at least one second."""
        client = Github(requests_per_second=.5)
        client.users.show('defunkt')
        start = datetime.datetime.utcnow()
        client.users.show('mojombo')
        end = datetime.datetime.utcnow()

        delta = end - start
        delta_seconds = delta.days * 24 * 60 * 60 + delta.seconds

        ok_(delta_seconds >= 2,
            "Expected .5 reqs per second to require a 2 second delay between "
            "calls.")


class BaseDataIter(utils.HttpMockTestCase):

    """Test iter availability of objects."""

    def test_iter(self):
        commit_id = '1c83cde9b5a7c396a01af1007fb7b88765b9ae45'
        commit = self.client.commits.show('ask/python-github2', commit_id)
        ok_('__iter__' in dir(commit))


class BaseDataDict(utils.HttpMockTestCase):

    """Test __getitem__ availability on objects."""

    def test_getitem(self):
        user = self.client.users.show('defunkt')
        eq_(user['blog'], user.blog)
        eq_(user['company'], user.company)
        eq_(user['email'], user.email)
        eq_(user['location'], user.location)
        eq_(user['login'], user.login)
        eq_(user['name'], user.name)


def test_project_for_user_repo():
    client = Github()
    eq_(client.project_for_user_repo('JNRowe', 'misc-overlay'),
                  'JNRowe/misc-overlay')


def test_repr_string():
    eq_(repr_string('test'), 'test')
    eq_(repr_string('abcdefghijklmnopqrst'), 'abcdefghijklmnopqrst')
    eq_(repr_string('abcdefghijklmnopqrstu'), 'abcdefghijklmnopq...')
