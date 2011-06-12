import _setup

from datetime import datetime

from nose.tools import assert_equals

import utils


class PullRequest(utils.HttpMockTestCase):
    def test_properties(self):
        pull_request = self.client.pull_requests.show('ask/python-github2', 39)
        assert_equals(pull_request.state, 'open')
        assert_equals(pull_request.base['sha'],
                      '6a79f43f174acd3953ced69263c06d311a6bda56')
        assert_equals(pull_request.head['sha'],
                      'a31cfb70343d3ac9d6330e6328008c0bc690a5a1')
        assert_equals(pull_request.issue_user['login'], 'JNRowe')
        assert_equals(pull_request.user['login'], 'JNRowe')
        assert_equals(pull_request.title, 'Datetime timezone handling.')
        assert_equals(len(pull_request.body), 1442)
        assert_equals(pull_request.position, 39.0)
        assert_equals(pull_request.number, 39.0)
        assert_equals(pull_request.votes, 0)
        assert_equals(pull_request.comments, 3)
        assert_equals(pull_request.diff_url,
                      'https://github.com/ask/python-github2/pull/39.diff')
        assert_equals(pull_request.patch_url,
                      'https://github.com/ask/python-github2/pull/39.patch')
        assert_equals(pull_request.labels, [])
        assert_equals(pull_request.html_url,
                      'https://github.com/ask/python-github2/pull/39')
        assert_equals(pull_request.issue_created_at,
                      datetime(2011, 4, 18, 15, 25, 47))
        assert_equals(pull_request.issue_updated_at,
                      datetime(2011, 5, 29, 15, 37, 8))
        assert_equals(pull_request.created_at,
                      datetime(2011, 4, 30, 12, 37, 40))
        assert_equals(pull_request.updated_at,
                      datetime(2011, 6, 7, 13, 56, 50))
        assert_equals(pull_request.closed_at, None)
        assert_equals(len(pull_request.discussion), 13)
        assert_equals(pull_request.mergeable, False)

    def test_repr(self):
        pull_request = self.client.pull_requests.show('ask/python-github2', 39)
        assert_equals(repr(pull_request),
                      '<PullRequest: Datetime timezone...>')


class PullRequestQueries(utils.HttpMockTestCase):
    """Test pull request querying"""
    def test_list(self):
        pull_requests = self.client.pull_requests.list('ask/python-github2')
        assert_equals(len(pull_requests), 2)
        assert_equals(pull_requests[0].title, 'Datetime timezone handling.')
