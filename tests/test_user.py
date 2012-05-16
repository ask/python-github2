# Copyright (C) 2011-2012 James Rowe <jnrowe@gmail.com>
#
# This file is part of python-github2, and is made available under the 3-clause
# BSD license.  See LICENSE for the full details.

import datetime

from nose.tools import (eq_, assert_false, assert_true)

import utils


class UserProperties(utils.HttpMockTestCase):
    """Test user property handling"""
    def test_user(self):
        user = self.client.users.show('defunkt')
        eq_(user.blog, 'http://chriswanstrath.com/')
        eq_(user.company, 'GitHub')
        eq_(user.email, 'chris@wanstrath.com')
        eq_(user.location, 'San Francisco')
        eq_(user.login, 'defunkt')
        eq_(user.name, 'Chris Wanstrath')

    def test_meta(self):
        user = self.client.users.show('defunkt')
        eq_(user.created_at, datetime.datetime(2007, 10, 19, 22, 24, 19))
        eq_(user.followers_count, 3402)
        eq_(user.following_count, 212)
        eq_(user.gravatar_id, 'b8dbb1987e8e5318584865f880036796')
        eq_(user.id, 2)
        eq_(user.public_gist_count, 278)
        eq_(user.public_repo_count, 93)

    def test_followers(self):
        eq_(len(self.client.users.followers('defunkt')), 3402)

    def test_following(self):
        eq_(len(self.client.users.following('defunkt')), 212)

    def test_is_not_authenticated(self):
        user = self.client.users.show('defunkt')
        assert_true(user.is_authenticated() is False)


class UserQueries(utils.HttpMockTestCase):
    """Test user querying """
    def test_search(self):
        eq_(repr(self.client.users.search('James Rowe')),
            '[<User: JNRowe>, <User: wooki>]')

    def test_search_by_email(self):
        user = self.client.users.search_by_email('jnrowe@gmail.com')
        eq_(repr(user), '<User: JNRowe>')


class AuthenticatedUserMethods(utils.HttpMockAuthenticatedTestCase):
    def test_follow(self):
        result = self.client.users.follow('defunkt')
        assert_true('defunkt' in result['users'])

    def test_unfollow(self):
        result = self.client.users.unfollow('defunkt')
        assert_false('defunkt' in result['users'])

    def test_is_authenticated(self):
        user = self.client.users.show('')
        assert_true(user.is_authenticated() is True)

    def test_list_keys(self):
        keys = self.client.users.list_keys()
        eq_(keys[0].id, 1337)


class AuthenticatedUserProperties(utils.HttpMockAuthenticatedTestCase):
    def test_private_data(self):
        user = self.client.users.show('')
        eq_(user.total_private_repo_count, 0)
        eq_(user.collaborators, 0)
        eq_(user.disk_usage, 66069)
        eq_(user.owned_private_repo_count, 0)
        eq_(user.private_gist_count, 7)

    def test_plan_data(self):
        user = self.client.users.show('')
        eq_(user.plan['name'], "free")
        eq_(user.plan['collaborators'], 0)
        eq_(user.plan['space'], 307200)
        eq_(user.plan['private_repos'], 0)
