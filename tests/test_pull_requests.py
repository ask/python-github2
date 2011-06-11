import _setup

from nose.tools import assert_equals

import utils


class PullRequest(utils.HttpMockTestCase):
    def test_repr(self):
        pull_request = self.client.pull_requests.show('ask/python-github2', 39)
        assert_equals(repr(pull_request),
                      '<PullRequest: Datetime timezone handling.>')


class PullRequestQueries(utils.HttpMockTestCase):
    """Test pull request querying"""
    def test_list(self):
        pull_requests = self.client.pull_requests.list('ask/python-github2')
        assert_equals(len(pull_requests), 2)
        assert_equals(pull_requests[0].title, 'Datetime timezone handling.')
