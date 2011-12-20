from datetime import datetime

from nose.tools import assert_equals

import utils


class Issue(utils.HttpMockTestCase):
    def test_properties(self):
        issue = self.client.issues.show('ask/python-github2', 24)
        assert_equals(issue.position, 24.0)
        assert_equals(issue.number, 24)
        assert_equals(issue.votes, 0)
        assert_equals(len(issue.body), 164)
        assert_equals(issue.title, 'Pagination support for commits.')
        assert_equals(issue.user, 'svetlyak40wt')
        assert_equals(issue.state, 'open')
        assert_equals(issue.labels, [])
        assert_equals(issue.created_at, datetime(2010, 12, 8, 23, 50, 26))
        assert_equals(issue.closed_at, None)
        assert_equals(issue.updated_at, datetime(2011, 1, 4, 16, 26, 7))
        assert_equals(issue.diff_url,
                      'https://github.com/ask/python-github2/pull/24.diff')
        assert_equals(issue.patch_url,
                      'https://github.com/ask/python-github2/pull/24.patch')
        assert_equals(issue.pull_request_url,
                      'https://github.com/ask/python-github2/pull/24')

    def test_issue_repr(self):
        issue = self.client.issues.show('ask/python-github2', 24)
        assert_equals(repr(issue),
                      '<Issue: Pagination suppor...>')


class Comment(utils.HttpMockTestCase):
    def test_properties(self):
        comments = self.client.issues.comments('ask/python-github2', 24)
        comment = comments[0]
        assert_equals(comment.created_at, datetime(2010, 12, 9, 22, 37, 26))
        assert_equals(comment.updated_at, datetime(2010, 12, 9, 22, 37, 26))
        assert_equals(len(comment.body), 267)
        assert_equals(comment.id, 601871)
        assert_equals(comment.user, 'nvie')

    def test_comment_repr(self):
        comments = self.client.issues.comments('ask/python-github2', 24)
        assert_equals(repr(comments[1]),
                      '<Comment: Sure, but I have ...>')


class IssueQueries(utils.HttpMockTestCase):
    """Test issue querying"""
    def test_search(self):
        issues = self.client.issues.search('ask/python-github2', 'timezone',
                                           'closed')
        assert_equals(len(issues), 2)
        assert_equals(issues[1].number, 39)

    def test_list(self):
        issues = self.client.issues.list('ask/python-github2')
        assert_equals(len(issues), 4)
        assert_equals(issues[-1].number, 58)

    def test_list_with_state(self):
        issues = self.client.issues.list('ask/python-github2', "closed")
        assert_equals(len(issues), 55)
        assert_equals(issues[0].number, 59)

    def test_issue_labels(self):
        labels = self.client.issues.list_labels('JNRowe/misc-overlay')
        assert_equals(len(labels), 4)
        assert_equals(labels[0], 'feature')

    def test_list_by_label(self):
        issues = self.client.issues.list_by_label('JNRowe/misc-overlay', 'bug')
        assert_equals(len(issues), 30)
        assert_equals(issues[-1].number, 328)
