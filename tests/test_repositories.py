import datetime

from nose.tools import assert_equals

import utils


class Repo(utils.HttpMockTestCase):
    def test_repr(self):
        repo = self.client.repos.show('JNRowe/misc-overlay')
        assert_equals(repr(repo), '<Repository: JNRowe/misc-overlay>')


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
        assert_equals(repo.open_issues, 13)
        assert_equals(repo.created_at,
                      datetime.datetime(2009, 5, 2, 7, 32, 50))
        assert_equals(repo.pushed_at,
                      datetime.datetime(2011, 8, 11, 11, 46, 23))
        assert_equals(repo.has_downloads, True)
        assert_equals(repo.has_wiki, True)
        assert_equals(repo.has_issues, True)
        assert_equals(repo.language, 'Python')

    def test_fork_properties(self):
        repo = self.client.repos.show('JNRowe/python-github2')
        assert_equals(repo.forks, 0)
        assert_equals(repo.fork, True)
        assert_equals(repo.parent, 'ask/python-github2')
        assert_equals(repo.source, 'ask/python-github2')


class RepoQueries(utils.HttpMockTestCase):
    """Test repository querying"""
    def test_search(self):
        repos = self.client.repos.search('surfraw')
        assert_equals(len(repos), 8)
        assert_equals(repos[0].owner, 'JNRowe')

    def test_list(self):
        repos = self.client.repos.list('JNRowe')
        assert_equals(len(repos), 48)
        assert_equals(repos[0].name, 'bfm')

    def test_list_with_page(self):
        repos = self.client.repos.list('tekkub', page=2)
        assert_equals(len(repos), 37)
        assert_equals(repos[0].name, 'OhSnap')

    def test_watching(self):
        repos = self.client.repos.watching('JNRowe')
        assert_equals(len(repos), 90)
        assert_equals(repos[0].name, 'nerdtree')

    def test_watching_with_page(self):
        repos = self.client.repos.watching('tekkub', page=2)
        assert_equals(len(repos), 39)
        assert_equals(repos[0].name, 'Buffoon')

    def test_contributors(self):
        contributors = self.client.repos.list_contributors('ask/python-github2')
        assert_equals(len(contributors), 29)
        assert_equals(contributors[1].name, 'Ask Solem Hoel')

    def test_list_collaborators(self):
        collaborators = self.client.repos.list_collaborators('ask/python-github2')
        assert_equals(len(collaborators), 4)
        assert_equals(collaborators[2], 'JNRowe')

    def test_languages(self):
        languages = self.client.repos.languages('JNRowe/misc-overlay')
        assert_equals(len(languages), 2)
        assert_equals(languages['Python'], 11194)

    def test_tags(self):
        tags = self.client.repos.tags('ask/python-github2')
        assert_equals(len(tags), 7)
        assert_equals(tags['0.4.1'],
                      '96b0a41dd249c521323700bc11a0a721a7c9e642')

    def test_branches(self):
        branches = self.client.repos.branches('ask/python-github2')
        assert_equals(len(branches), 1)
        assert_equals(branches['master'],
                      '1c83cde9b5a7c396a01af1007fb7b88765b9ae45')

    def test_watchers(self):
        watchers = self.client.repos.watchers('ask/python-github2')
        assert_equals(len(watchers), 143)
        assert_equals(watchers[0], 'ask')


class AuthenticatedRepoQueries(utils.HttpMockAuthenticatedTestCase):
    def test_pushable(self):
        repos = self.client.repos.pushable()
        assert_equals(len(repos), 1)
        assert_equals(repos[0].name, 'python-github2')
