import _setup

from nose.tools import assert_equals

import utils


class PullRequest(utils.HttpMockTestCase):
    def test_repr(self):
        pull_request = self.client.pull_requests.show('ask/python-github2', 39)
        assert_equals(repr(pull_request),
                      '<PullRequest: Datetime timezone...>')


class PullRequestQueries(utils.HttpMockTestCase):
    """Test pull request querying"""
    def test_list(self):
        pull_requests = self.client.pull_requests.list('ask/python-github2')
        assert_equals(len(pull_requests), 1)
        assert_equals(pull_requests[0].title, 'Pagination support for commits.')

    def test_list_with_page(self):
        pull_requests = self.client.pull_requests.list('robbyrussell/oh-my-zsh',
                                                       page=2)
        assert_equals(len(pull_requests), 52)
        assert_equals(pull_requests[1].title, 'Added my own custom theme')
