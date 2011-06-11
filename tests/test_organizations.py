import _setup

from nose.tools import assert_equals

import utils


class Organization(utils.HttpMockTestCase):
    def test_repr(self):
        organization = self.client.organizations.show('github')
        assert_equals(repr(organization),
                      '<Organization: github>')


class OrganizationQueries(utils.HttpMockTestCase):
    """Test organisation querying"""
    def test_public_repositories(self):
        repos = self.client.organizations.public_repositories('github')
        assert_equals(len(repos), 26)
        assert_equals(repos[2].name, 'hubahuba')

    def test_public_members(self):
        members = self.client.organizations.public_members('github')
        assert_equals(len(members), 33)
        assert_equals(members[2].name, 'Ben Burkert')
