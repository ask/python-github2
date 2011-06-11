import _setup

from nose.tools import assert_equals

import utils


class ReprTests(utils.HttpMockTestCase):
    def test_issue_repr(self):
        issue = self.client.issues.show('ask/python-github2', 24)
        assert_equals(repr(issue),
                      '<Issue: Pagination support for commits.>')
        
    def test_comment_repr(self):
        comments = self.client.issues.comments('ask/python-github2', 24)
        assert_equals(repr(comments[1]),
                      '<Comment: Sure, but I have another idea.\r\n\r\nList methods could return not >')
