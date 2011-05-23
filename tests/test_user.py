import _setup

import datetime

from nose.tools import (assert_equals, assert_false, assert_true)

import utils


class UserProperties(utils.HttpMockTestCase):
    """Test user property handling"""
    def test_user(self):
        user = self.client.users.show('defunkt')
        assert_equals(user.blog, 'http://chriswanstrath.com/')
        assert_equals(user.company, 'GitHub')
        assert_equals(user.email, 'chris@wanstrath.com')
        assert_equals(user.location, 'San Francisco')
        assert_equals(user.login, 'defunkt')
        assert_equals(user.name, 'Chris Wanstrath')

    def test_meta(self):
        user = self.client.users.show('defunkt')
        assert_equals(user.created_at,
                      datetime.datetime(2007, 10, 19, 22, 24, 19))
        assert_equals(user.followers_count, 2593)
        assert_equals(user.following_count, 212)
        assert_equals(user.gravatar_id, 'b8dbb1987e8e5318584865f880036796')
        assert_equals(user.id, 2)
        assert_equals(user.public_gist_count, 277)
        assert_equals(user.public_repo_count, 90)

    def test_followers(self):
        assert_equals(len(self.client.users.followers('defunkt')), 2593)

    def test_following(self):
        assert_equals(len(self.client.users.following('defunkt')), 212)

    def test_is_authenticated(self):
        user = self.client.users.show('defunkt')
        assert_true(user.is_authenticated() is False)
        user = self.client.users.show('fake_jnrowe_with_auth')
        assert_true(user.is_authenticated() is True)

    def test_private_data(self):
        user = self.client.users.show('fake_jnrowe_with_auth')
        assert_equals(user.total_private_repo_count, 0)
        assert_equals(user.collaborators, 0)
        assert_equals(user.disk_usage, 66069)
        assert_equals(user.owned_private_repo_count, 0)
        assert_equals(user.private_gist_count, 7)

    def test_plan_data(self):
        user = self.client.users.show('fake_jnrowe_with_auth')
        assert_equals(user.plan['name'], "free")
        assert_equals(user.plan['collaborators'], 0)
        assert_equals(user.plan['space'], 307200)
        assert_equals(user.plan['private_repos'], 0)


class UserQueries(utils.HttpMockTestCase):
    """Test user querying """
    def test_search(self):
        assert_equals(repr(self.client.users.search('James Rowe')),
                      '[<User: JNRowe>, <User: wooki>]')

    def test_search_by_email(self):
        user = self.client.users.search_by_email('jnrowe@gmail.com')
        assert_equals(repr(user), '<User: JNRowe>')


class UserMethods(utils.HttpMockTestCase):
    def test_follow(self):
        result = self.client.users.follow('defunkt')
        assert_true('defunkt' in result['users'])

    def test_unfollow(self):
        result = self.client.users.unfollow('defunkt')
        assert_false('defunkt' in result['users'])
