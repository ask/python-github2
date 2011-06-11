import _setup

from nose.tools import assert_equals

import utils


class ReprTests(utils.HttpMockTestCase):
    def test_issue_repr(self):
        issue = self.client.issues.show('ask/python-github2', 24)
        assert_equals(repr(issue),
                      '<Issue: Pagination suppor...>')
        
    def test_comment_repr(self):
        comments = self.client.issues.comments('ask/python-github2', 24)
        assert_equals(repr(comments[1]),
                      '<Comment: Sure, but I have ...>')


class IssueQueries(utils.HttpMockTestCase):
    """Test issue querying"""
    def test_search(self):
        issues = self.client.issues.search('ask/python-github2', 'timezone')
        assert_equals(len(issues), 3)
        assert_equals(issues[2].number, 39)

    def test_list(self):
        issues = self.client.issues.list('ask/python-github2')
        assert_equals(len(issues), 5)
        assert_equals(issues[-1].number, 53)

    def test_list_with_state(self):
        issues = self.client.issues.list('ask/python-github2', "closed")
        assert_equals(len(issues), 48)
        assert_equals(issues[0].number, 52)

    def test_issue_labels(self):
        labels = self.client.issues.list_labels('JNRowe/misc-overlay')
        assert_equals(len(labels), 3)
        assert_equals(labels[0], 'feature')

    def test_list_by_label(self):
        issues = self.client.issues.list_by_label('JNRowe/misc-overlay', 'bug')
        assert_equals(len(issues), 30)
        assert_equals(issues[-1].number, 328)
