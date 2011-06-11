import _setup

from nose.tools import assert_equals

import utils


class Commit(utils.HttpMockTestCase):
    def test_repr(self):
        commit_id = '1c83cde9b5a7c396a01af1007fb7b88765b9ae45'
        commit = self.client.commits.show('ask/python-github2', commit_id)
        assert_equals(repr(commit),
                      '<Commit: %s Added cache support to manage_collaborators.>' % commit_id)


class CommitsQueries(utils.HttpMockTestCase):
    """Test commit querying"""
    def test_list(self):
        commits = self.client.commits.list('JNRowe/misc-overlay')
        assert_equals(len(commits), 35)
        assert_equals(commits[0].id,
                '37233b357d1a3648434ffda8f569ce96b3bcbf53')

    def test_list_with_branch(self):
        commits = self.client.commits.list('JNRowe/misc-overlay', 'gh-pages')
        assert_equals(len(commits), 35)
        assert_equals(commits[0].id,
                '482f657443df4b701137a3025ae08476cddd2b7d')

    def test_list_with_file(self):
        commits = self.client.commits.list('JNRowe/misc-overlay',
                                           file='Makefile')
        assert_equals(len(commits), 31)
        assert_equals(commits[0].id,
                '41bcd985139189763256a8c82b8f0fcbe150eb03')

    def test_list_with_branch_and_file(self):
        commits = self.client.commits.list('JNRowe/misc-overlay', 'gh-pages',
                                           'packages/dev-python.html')
        assert_equals(len(commits), 35)
        assert_equals(commits[0].id,
                '482f657443df4b701137a3025ae08476cddd2b7d')
