from nose.tools import assert_equals

import utils


class TeamEdits(utils.HttpMockAuthenticatedTestCase):
    def test_add_member(self):
        users = self.client.teams.add_member(121990, 'JNRowe')
        assert_equals(users[0].login, 'JNRowe')
