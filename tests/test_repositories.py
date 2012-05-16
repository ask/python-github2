# coding: utf-8
# Copyright (C) 2011-2012 James Rowe <jnrowe@gmail.com>
#                         Stéphane Angel <s.angel@twidi.com>
#
# This file is part of python-github2, and is made available under the 3-clause
# BSD license.  See LICENSE for the full details.

import datetime

from nose.tools import eq_

import utils


class Repo(utils.HttpMockTestCase):
    def test_repr(self):
        repo = self.client.repos.show('JNRowe/misc-overlay')
        eq_(repr(repo), '<Repository: JNRowe/misc-overlay>')


class RepoProperties(utils.HttpMockTestCase):

    """Test repository property handling."""

    def test_repo(self):
        repo = self.client.repos.show('JNRowe/misc-overlay')

        eq_(repo.name, 'misc-overlay')
        eq_(repo.description, 'Gentoo overlay -- miscellaneous packages')
        eq_(repo.url, 'https://github.com/JNRowe/misc-overlay')
        eq_(repo.owner, 'JNRowe')
        eq_(repo.homepage, 'http://jnrowe.github.com/misc-overlay/')

        eq_(repo.project, 'JNRowe/misc-overlay')

    def test_meta(self):
        repo = self.client.repos.show('JNRowe/misc-overlay')
        eq_(repo.forks, 0)
        eq_(repo.watchers, 5)
        eq_(repo.private, False)
        eq_(repo.fork, False)
        eq_(repo.master_branch, None)
        eq_(repo.integration_branch, None)
        eq_(repo.open_issues, 13)
        eq_(repo.created_at, datetime.datetime(2009, 5, 2, 7, 32, 50))
        eq_(repo.pushed_at, datetime.datetime(2011, 8, 11, 11, 46, 23))
        eq_(repo.has_downloads, True)
        eq_(repo.has_wiki, True)
        eq_(repo.has_issues, True)
        eq_(repo.language, 'Python')

    def test_fork_properties(self):
        repo = self.client.repos.show('JNRowe/python-github2')
        eq_(repo.forks, 0)
        eq_(repo.fork, True)
        eq_(repo.parent, 'ask/python-github2')
        eq_(repo.source, 'ask/python-github2')


class RepoQueries(utils.HttpMockTestCase):
    """Test repository querying"""
    def test_search(self):
        repos = self.client.repos.search('surfraw')
        eq_(len(repos), 8)
        eq_(repos[0].owner, 'JNRowe')

    def test_list(self):
        repos = self.client.repos.list('JNRowe')
        eq_(len(repos), 48)
        eq_(repos[0].name, 'bfm')

    def test_list_with_page(self):
        repos = self.client.repos.list('tekkub', page=2)
        eq_(len(repos), 37)
        eq_(repos[0].name, 'OhSnap')

    def test_watching(self):
        repos = self.client.repos.watching('JNRowe')
        eq_(len(repos), 90)
        eq_(repos[0].name, 'nerdtree')

    def test_watching_with_page(self):
        repos = self.client.repos.watching('tekkub', page=2)
        eq_(len(repos), 39)
        eq_(repos[0].name, 'Buffoon')

    def test_contributors(self):
        contributors = self.client.repos.list_contributors('ask/python-github2')
        eq_(len(contributors), 29)
        eq_(contributors[1].name, 'Ask Solem Hoel')

    def test_list_collaborators(self):
        collaborators = self.client.repos.list_collaborators('ask/python-github2')
        eq_(len(collaborators), 4)
        eq_(collaborators[2], 'JNRowe')

    def test_languages(self):
        languages = self.client.repos.languages('JNRowe/misc-overlay')
        eq_(len(languages), 2)
        eq_(languages['Python'], 11194)

    def test_tags(self):
        tags = self.client.repos.tags('ask/python-github2')
        eq_(len(tags), 7)
        eq_(tags['0.4.1'], '96b0a41dd249c521323700bc11a0a721a7c9e642')

    def test_branches(self):
        branches = self.client.repos.branches('ask/python-github2')
        eq_(len(branches), 1)
        eq_(branches['master'], '1c83cde9b5a7c396a01af1007fb7b88765b9ae45')

    def test_watchers(self):
        watchers = self.client.repos.watchers('ask/python-github2')
        eq_(len(watchers), 143)
        eq_(watchers[0], 'ask')


class AuthenticatedRepoQueries(utils.HttpMockAuthenticatedTestCase):
    def test_pushable(self):
        repos = self.client.repos.pushable()
        eq_(len(repos), 1)
        eq_(repos[0].name, 'python-github2')
