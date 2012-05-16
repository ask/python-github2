# Copyright (C) 2011-2012 James Rowe <jnrowe@gmail.com>
#
# This file is part of python-github2, and is made available under the 3-clause
# BSD license.  See LICENSE for the full details.

from datetime import datetime

from nose.tools import (eq_, assert_true)

import utils


class OrganizationProperties(utils.HttpMockTestCase):
    def test_properties(self):
        organization = self.client.organizations.show('github')
        eq_(organization.id, 9919)
        eq_(organization.name, 'GitHub')
        eq_(organization.blog, 'https://github.com/about')
        eq_(organization.location, 'San Francisco, CA')
        eq_(organization.gravatar_id, '61024896f291303615bcd4f7a0dcfb74')
        eq_(organization.login, 'github')
        eq_(organization.email, 'support@github.com')
        eq_(organization.company, None)
        eq_(organization.created_at, datetime(2008, 5, 10, 21, 37, 31))
        eq_(organization.following_count, 0)
        eq_(organization.followers_count, 591)
        eq_(organization.public_gist_count, 0)
        eq_(organization.public_repo_count, 31)
        eq_(organization.permission, None)
        eq_(organization.plan, None)

    def test_is_authenticated(self):
        organization = self.client.organizations.show('github')
        assert_true(organization.is_authenticated() is False)
        organization = self.client.organizations.show('fake_org_with_auth')
        assert_true(organization.is_authenticated() is True)


class Organization(utils.HttpMockTestCase):
    def test_repr(self):
        organization = self.client.organizations.show('github')
        eq_(repr(organization), '<Organization: github>')


class OrganizationQueries(utils.HttpMockTestCase):
    """Test organisation querying"""
    def test_public_repositories(self):
        repos = self.client.organizations.public_repositories('github')
        eq_(len(repos), 31)
        eq_(repos[2].name, 'hubahuba')

    def test_public_members(self):
        members = self.client.organizations.public_members('github')
        eq_(len(members), 35)
        eq_(members[2].name, 'Ben Burkert')


class OrganizationsEdits(utils.HttpMockAuthenticatedTestCase):
    def test_add_team(self):
        team = self.client.organizations.add_team('JNRowe-test-org',
                                                  'test_pull', 'pull')
        eq_(team.name, 'team_pull')
        eq_(team.permission, 'pull')

    def test_add_team_with_repos(self):
        projects = ['JNRowe-test-org/test1', 'JNRowe-test-org/test2']
        team = self.client.organizations.add_team('JNRowe-test-org',
                                                  'test_push', 'push',
                                                  projects)

        team_repos = self.client.teams.repositories(team.id)
        eq_(['/'.join([x.organization, x.name]) for x in team_repos], projects)
