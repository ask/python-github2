.. Copyright (C) 2011-2012 James Rowe <jnrowe@gmail.com>

   This file is part of python-github2, is licensed under the 3-clause BSD
   License.  See the LICENSE file in the top distribution directory for the full
   license text.

.. module:: github2.organizations

Organizations
=============

.. note::

   See the official GitHub API v2 documentation for `organizations and teams`_.

.. _organizations and teams: http://develop.github.com/p/orgs.html

.. autoclass:: Organization(type)

.. autoclass:: Organizations(type)

Examples
--------

Fetch Organizations Info
''''''''''''''''''''''''

    >>> org = github.organizations.show("JNRowe-test-only")
    >>> org.created_at
    datetime.datetime(2011, 5, 10, 11, 37, 27)

    >>> repos = github.organizations.public_repositories(org.login)

    >>> users = github.organizations.public_members(org.login)

    >>> teams = github2.organizations.teams(org.login)


Fetch Authenticated User's Organizations Data
'''''''''''''''''''''''''''''''''''''''''''''

    >>> orgs = github.organizations.list()

    >>> repos = github.organizations.repositories()
