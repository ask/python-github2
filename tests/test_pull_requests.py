import _setup

from nose.tools import assert_equals

import utils


class PullRequest(utils.HttpMockTestCase):
    def test_repr(self):
        pull_request = self.client.pull_requests.show('ask/python-github2', 39)
        assert_equals(repr(pull_request),
                      '<PullRequest: Datetime timezone handling.>')
