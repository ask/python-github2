# Copyright (C) 2011-2012 James Rowe <jnrowe@gmail.com>
#
# This file is part of python-github2, and is made available under the 3-clause
# BSD license.  See LICENSE for the full details.

from datetime import datetime

from nose.tools import eq_

import utils


class PullRequest(utils.HttpMockTestCase):
    def test_properties(self):
        pull_request = self.client.pull_requests.show('ask/python-github2', 39)
        eq_(pull_request.state, 'closed')
        eq_(pull_request.base['sha'],
                      '0786a96c80afad7bbd0747df590f649eaa46ca04')
        eq_(pull_request.head['sha'],
                      '5438e41d9c390f53089ed3fa0842831fafc73d8e')
        eq_(pull_request.issue_user['login'], 'JNRowe')
        eq_(pull_request.user['login'], 'JNRowe')
        eq_(pull_request.title, 'Datetime timezone handling.')
        eq_(len(pull_request.body), 1442)
        eq_(pull_request.position, 39.0)
        eq_(pull_request.number, 39.0)
        eq_(pull_request.votes, 0)
        eq_(pull_request.comments, 4)
        eq_(pull_request.diff_url,
            'https://github.com/ask/python-github2/pull/39.diff')
        eq_(pull_request.patch_url,
            'https://github.com/ask/python-github2/pull/39.patch')
        eq_(pull_request.labels, [])
        eq_(pull_request.html_url,
            'https://github.com/ask/python-github2/pull/39')
        eq_(pull_request.issue_created_at, datetime(2011, 4, 18, 15, 25, 47))
        eq_(pull_request.issue_updated_at, datetime(2011, 6, 23, 9, 33, 57))
        eq_(pull_request.created_at, datetime(2011, 6, 20, 16, 51, 24))
        eq_(pull_request.updated_at, datetime(2011, 6, 23, 9, 28, 42))
        eq_(pull_request.closed_at, datetime(2011, 6, 23, 9, 33, 57))
        eq_(len(pull_request.discussion), 13)
        eq_(pull_request.mergeable, True)

    def test_repr(self):
        pull_request = self.client.pull_requests.show('ask/python-github2', 39)
        eq_(repr(pull_request), '<PullRequest: Datetime timezone...>')


class PullRequestQueries(utils.HttpMockTestCase):
    """Test pull request querying"""
    def test_list(self):
        pull_requests = self.client.pull_requests.list('ask/python-github2')
        eq_(len(pull_requests), 1)
        eq_(pull_requests[0].title, 'Pagination support for commits.')

    def test_list_with_page(self):
        pull_requests = self.client.pull_requests.list('robbyrussell/oh-my-zsh',
                                                       page=2)
        eq_(len(pull_requests), 52)
        eq_(pull_requests[1].title, 'Added my own custom theme')
