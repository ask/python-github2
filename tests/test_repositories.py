import _setup

import datetime

from nose.tools import (assert_equals, assert_false, assert_true)

import utils


class RepoProperties(utils.HttpMockTestCase):
    """Test repository property handling"""
    def test_repo(self):
        repo = self.client.repos.show('JNRowe/misc-overlay')

        assert_equals(repo.name, 'misc-overlay')
        assert_equals(repo.description,
                      'Gentoo overlay -- miscellaneous packages')
        assert_equals(repo.url, 'https://github.com/JNRowe/misc-overlay')
        assert_equals(repo.owner, 'JNRowe')
        assert_equals(repo.homepage, 'http://jnrowe.github.com/misc-overlay/')

        assert_equals(repo.project, 'JNRowe/misc-overlay')

    def test_meta(self):
        repo = self.client.repos.show('JNRowe/misc-overlay')
        assert_equals(repo.forks, 0)
        assert_equals(repo.watchers, 5)
        assert_equals(repo.private, False)
        assert_equals(repo.fork, False)
        assert_equals(repo.master_branch, None)
        assert_equals(repo.integration_branch, None)
        assert_equals(repo.open_issues, 6)
        assert_equals(repo.created_at,
                      datetime.datetime(2009, 5, 2, 7, 32, 50))
        assert_equals(repo.pushed_at,
                      datetime.datetime(2011, 5, 22, 0, 24, 15))
        assert_equals(repo.has_downloads, True)
        assert_equals(repo.has_wiki, True)
        assert_equals(repo.has_issues, True)
        assert_equals(repo.language, 'Python')
