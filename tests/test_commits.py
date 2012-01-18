from datetime import datetime

from nose.tools import assert_equals

import utils


class CommitProperties(utils.HttpMockTestCase):
    """Test commit property handling"""
    commit_id = '1c83cde9b5a7c396a01af1007fb7b88765b9ae45'

    def test_commit(self):
        commit = self.client.commits.show('ask/python-github2', self.commit_id)
        assert_equals(commit.message,
                      'Added cache support to manage_collaborators.')
        assert_equals(commit.parents,
                      [{"id": '7d1c855d2f44a55e4b90b40017be697cf70cb4a0'}])
        assert_equals(commit.url,
                      '/ask/python-github2/commit/%s' % self.commit_id)
        assert_equals(commit.author['login'], 'JNRowe')
        assert_equals(commit.id, self.commit_id)
        assert_equals(commit.committed_date,
                      datetime(2011, 6, 6, 16, 13, 50))
        assert_equals(commit.authored_date, datetime(2011, 6, 6, 16, 13, 50))
        assert_equals(commit.tree, 'f48fcc1a0b8ea97f3147dc42cf7cdb6683493e94')
        assert_equals(commit.committer['login'], 'JNRowe')
        assert_equals(commit.added, None)
        assert_equals(commit.removed, None)
        assert_equals(commit.modified[0]['filename'],
                      'github2/bin/manage_collaborators.py')

    def test_repr(self):
        commit = self.client.commits.show('ask/python-github2', self.commit_id)
        assert_equals(repr(commit),
                      '<Commit: %s Added cache suppo...>' % self.commit_id[:8])


class CommitsQueries(utils.HttpMockTestCase):
    """Test commit querying"""

    def test_list(self):
        commits = self.client.commits.list('JNRowe/misc-overlay')
        assert_equals(len(commits), 35)
        assert_equals(commits[0].id,
                '4de0834d58b37ef3020c49df43c95649217a2def')

    def test_list_with_page(self):
        commits = self.client.commits.list('JNRowe/jnrowe-misc', page=2)
        assert_equals(len(commits), 35)
        assert_equals(commits[0].id,
                '1f5ad2c3206bafc4aca9e6ce50f5c605befdb3d6')

    def test_list_with_branch(self):
        commits = self.client.commits.list('JNRowe/misc-overlay', 'gh-pages')
        assert_equals(len(commits), 35)
        assert_equals(commits[0].id,
                '025148bdaa6fb6bdac9c3522d481fadf1c0a456f')

    def test_list_with_file(self):
        commits = self.client.commits.list('JNRowe/misc-overlay',
                                           file='Makefile')
        assert_equals(len(commits), 35)
        assert_equals(commits[0].id,
                'fc12b924d34dc38c8ce76d27a866221faa88cb72')

    def test_list_with_branch_and_file(self):
        commits = self.client.commits.list('JNRowe/misc-overlay', 'gh-pages',
                                           'packages/dev-python.html')
        assert_equals(len(commits), 35)
        assert_equals(commits[0].id,
                '025148bdaa6fb6bdac9c3522d481fadf1c0a456f')
