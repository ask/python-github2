from nose.tools import (assert_equals, assert_true)

import utils


class OrganizationProperties(utils.HttpMockTestCase):
    def test_is_authenticated(self):
        organization = self.client.organizations.show('github')
        assert_true(organization.is_authenticated() is False)
        organization = self.client.organizations.show('fake_org_with_auth')
        assert_true(organization.is_authenticated() is True)


class Organization(utils.HttpMockTestCase):
    def test_repr(self):
        organization = self.client.organizations.show('github')
        assert_equals(repr(organization),
                      '<Organization: github>')


class OrganizationQueries(utils.HttpMockTestCase):
    """Test organisation querying"""
    def test_public_repositories(self):
        repos = self.client.organizations.public_repositories('github')
        assert_equals(len(repos), 31)
        assert_equals(repos[2].name, 'hubahuba')

    def test_public_members(self):
        members = self.client.organizations.public_members('github')
        assert_equals(len(members), 35)
        assert_equals(members[2].name, 'Ben Burkert')


class OrganizationsEdits(utils.HttpMockAuthenticatedTestCase):
    def test_add_team(self):
        team = self.client.organizations.add_team('JNRowe-test-org',
                                                  'test_pull', 'pull')
        assert_equals(team.name, 'team_pull')
        assert_equals(team.permission, 'pull')

    def test_add_team_with_repos(self):
        projects = ['JNRowe-test-org/test1', 'JNRowe-test-org/test2']
        team = self.client.organizations.add_team('JNRowe-test-org',
                                                  'test_push', 'push', projects)

        team_repos = self.client.teams.repositories(team.id)
        assert_equals(['/'.join([x.organization, x.name]) for x in team_repos],
                      projects)
