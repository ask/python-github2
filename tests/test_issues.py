# Copyright (C) 2011-2012 James Rowe <jnrowe@gmail.com>
#
# This file is part of python-github2, and is made available under the 3-clause
# BSD license.  See LICENSE for the full details.

from datetime import datetime

from nose.tools import eq_

import utils


class Issue(utils.HttpMockTestCase):
    def test_properties(self):
        issue = self.client.issues.show('ask/python-github2', 24)
        eq_(issue.position, 24.0)
        eq_(issue.number, 24)
        eq_(issue.votes, 0)
        eq_(len(issue.body), 164)
        eq_(issue.title, 'Pagination support for commits.')
        eq_(issue.user, 'svetlyak40wt')
        eq_(issue.state, 'open')
        eq_(issue.labels, [])
        eq_(issue.created_at, datetime(2010, 12, 8, 23, 50, 26))
        eq_(issue.closed_at, None)
        eq_(issue.updated_at, datetime(2011, 1, 4, 16, 26, 7))
        eq_(issue.diff_url,
            'https://github.com/ask/python-github2/pull/24.diff')
        eq_(issue.patch_url,
            'https://github.com/ask/python-github2/pull/24.patch')
        eq_(issue.pull_request_url,
            'https://github.com/ask/python-github2/pull/24')

    def test_issue_repr(self):
        issue = self.client.issues.show('ask/python-github2', 24)
        eq_(repr(issue), '<Issue: Pagination suppor...>')


class Comment(utils.HttpMockTestCase):
    def test_properties(self):
        comments = self.client.issues.comments('ask/python-github2', 24)
        comment = comments[0]
        eq_(comment.created_at, datetime(2010, 12, 9, 22, 37, 26))
        eq_(comment.updated_at, datetime(2010, 12, 9, 22, 37, 26))
        eq_(len(comment.body), 267)
        eq_(comment.id, 601871)
        eq_(comment.user, 'nvie')

    def test_comment_repr(self):
        comments = self.client.issues.comments('ask/python-github2', 24)
        eq_(repr(comments[1]), '<Comment: Sure, but I have ...>')


class IssueQueries(utils.HttpMockTestCase):

    """Test issue querying."""

    def test_search(self):
        issues = self.client.issues.search('ask/python-github2', 'timezone',
                                           'closed')
        eq_(len(issues), 2)
        eq_(issues[1].number, 39)

    def test_list(self):
        issues = self.client.issues.list('ask/python-github2')
        eq_(len(issues), 4)
        eq_(issues[-1].number, 58)

    def test_list_with_state(self):
        issues = self.client.issues.list('ask/python-github2', "closed")
        eq_(len(issues), 55)
        eq_(issues[0].number, 59)

    def test_issue_labels(self):
        labels = self.client.issues.list_labels('JNRowe/misc-overlay')
        eq_(len(labels), 4)
        eq_(labels[0], 'feature')

    def test_list_by_label(self):
        issues = self.client.issues.list_by_label('JNRowe/misc-overlay', 'bug')
        eq_(len(issues), 30)
        eq_(issues[-1].number, 328)
