# Copyright (C) 2011-2012 James Rowe <jnrowe@gmail.com>
#
# This file is part of python-github2, and is made available under the 3-clause
# BSD license.  See LICENSE for the full details.

from nose.tools import assert_equals

import utils


class TeamEdits(utils.HttpMockAuthenticatedTestCase):
    def test_add_member(self):
        users = self.client.teams.add_member(121990, 'JNRowe')
        assert_equals(users[0].login, 'JNRowe')
