# Copyright (C) 2011-2012 James Rowe <jnrowe@gmail.com>
#
# This file is part of python-github2, and is made available under the 3-clause
# BSD license.  See LICENSE for the full details.

from datetime import datetime

from nose.tools import eq_

import utils


class CommitProperties(utils.HttpMockTestCase):

    """Test commit property handling."""

    commit_id = '1c83cde9b5a7c396a01af1007fb7b88765b9ae45'

    def test_commit(self):
        commit = self.client.commits.show('ask/python-github2', self.commit_id)
        eq_(commit.message, 'Added cache support to manage_collaborators.')
        eq_(commit.parents,
            [{"id": '7d1c855d2f44a55e4b90b40017be697cf70cb4a0'}])
        eq_(commit.url, '/ask/python-github2/commit/%s' % self.commit_id)
        eq_(commit.author['login'], 'JNRowe')
        eq_(commit.id, self.commit_id)
        eq_(commit.committed_date, datetime(2011, 6, 6, 16, 13, 50))
        eq_(commit.authored_date, datetime(2011, 6, 6, 16, 13, 50))
        eq_(commit.tree, 'f48fcc1a0b8ea97f3147dc42cf7cdb6683493e94')
        eq_(commit.committer['login'], 'JNRowe')
        eq_(commit.added, None)
        eq_(commit.removed, None)
        eq_(commit.modified[0]['filename'],
            'github2/bin/manage_collaborators.py')

    def test_repr(self):
        commit = self.client.commits.show('ask/python-github2', self.commit_id)
        eq_(repr(commit),
            '<Commit: %s Added cache suppo...>' % self.commit_id[:8])


class CommitsQueries(utils.HttpMockTestCase):

    """Test commit querying"""

    def test_list(self):
        commits = self.client.commits.list('JNRowe/misc-overlay')
        eq_(len(commits), 35)
        eq_(commits[0].id, '4de0834d58b37ef3020c49df43c95649217a2def')

    def test_list_with_page(self):
        commits = self.client.commits.list('JNRowe/jnrowe-misc', page=2)
        eq_(len(commits), 35)
        eq_(commits[0].id, '1f5ad2c3206bafc4aca9e6ce50f5c605befdb3d6')

    def test_list_with_branch(self):
        commits = self.client.commits.list('JNRowe/misc-overlay', 'gh-pages')
        eq_(len(commits), 35)
        eq_(commits[0].id, '025148bdaa6fb6bdac9c3522d481fadf1c0a456f')

    def test_list_with_file(self):
        commits = self.client.commits.list('JNRowe/misc-overlay',
                                           file='Makefile')
        eq_(len(commits), 35)
        eq_(commits[0].id, 'fc12b924d34dc38c8ce76d27a866221faa88cb72')

    def test_list_with_branch_and_file(self):
        commits = self.client.commits.list('JNRowe/misc-overlay', 'gh-pages',
                                           'packages/dev-python.html')
        eq_(len(commits), 35)
        eq_(commits[0].id, '025148bdaa6fb6bdac9c3522d481fadf1c0a456f')
