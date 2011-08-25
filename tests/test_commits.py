import _setup

from nose.tools import assert_equals

import utils


class Commit(utils.HttpMockTestCase):
    def test_repr(self):
        commit_id = '1c83cde9b5a7c396a01af1007fb7b88765b9ae45'
        commit = self.client.commits.show('ask/python-github2', commit_id)
        assert_equals(repr(commit),
                      '<Commit: %s Added cache suppo...>' % commit_id[:8])


class CommitsQueries(utils.HttpMockTestCase):
    """Test commit querying"""
    def test_list(self):
        commits = self.client.commits.list('JNRowe/misc-overlay')
        assert_equals(len(commits), 35)
        assert_equals(commits[0].id,
                '4de0834d58b37ef3020c49df43c95649217a2def')

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
