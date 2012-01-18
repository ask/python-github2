from datetime import datetime

from nose.tools import assert_equals

import utils


class PullRequest(utils.HttpMockTestCase):
    def test_properties(self):
        pull_request = self.client.pull_requests.show('ask/python-github2', 39)
        assert_equals(pull_request.state, 'closed')
        assert_equals(pull_request.base['sha'],
                      '0786a96c80afad7bbd0747df590f649eaa46ca04')
        assert_equals(pull_request.head['sha'],
                      '5438e41d9c390f53089ed3fa0842831fafc73d8e')
        assert_equals(pull_request.issue_user['login'], 'JNRowe')
        assert_equals(pull_request.user['login'], 'JNRowe')
        assert_equals(pull_request.title, 'Datetime timezone handling.')
        assert_equals(len(pull_request.body), 1442)
        assert_equals(pull_request.position, 39.0)
        assert_equals(pull_request.number, 39.0)
        assert_equals(pull_request.votes, 0)
        assert_equals(pull_request.comments, 4)
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
                      datetime(2011, 6, 23, 9, 33, 57))
        assert_equals(pull_request.created_at,
                      datetime(2011, 6, 20, 16, 51, 24))
        assert_equals(pull_request.updated_at,
                      datetime(2011, 6, 23, 9, 28, 42))
        assert_equals(pull_request.closed_at,
                      datetime(2011, 6, 23, 9, 33, 57))
        assert_equals(len(pull_request.discussion), 13)
        assert_equals(pull_request.mergeable, True)

    def test_repr(self):
        pull_request = self.client.pull_requests.show('ask/python-github2', 39)
        assert_equals(repr(pull_request),
                      '<PullRequest: Datetime timezone...>')


class PullRequestQueries(utils.HttpMockTestCase):
    """Test pull request querying"""
    def test_list(self):
        pull_requests = self.client.pull_requests.list('ask/python-github2')
        assert_equals(len(pull_requests), 1)
        assert_equals(pull_requests[0].title,
                      'Pagination support for commits.')

    def test_list_with_page(self):
        pull_requests = self.client.pull_requests.list('robbyrussell/oh-my-zsh',
                                                       page=2)
        assert_equals(len(pull_requests), 52)
        assert_equals(pull_requests[1].title, 'Added my own custom theme')
