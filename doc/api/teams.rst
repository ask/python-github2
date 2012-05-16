.. Copyright (C) 2011-2012 James Rowe <jnrowe@gmail.com>

   This file is part of python-github2, is licensed under the 3-clause BSD
   License.  See the LICENSE file in the top distribution directory for the full
   license text.

.. module:: github2.teams

Teams
=====

.. note::

   See the official GitHub API v2 documentation for `organizations and teams`_.

.. _organizations and teams: http://develop.github.com/p/teams.html

.. autoclass:: Team(type)

.. autoclass:: Teams(type)

Examples
--------

Fetch Teams Info
''''''''''''''''

    >>> team = github.teams.show(56855)
    >>> team[0].name
    u'Owners'

    >>> github.teams.members(56855)
    [<User: JNRowe>]

    >>> repos = github.teams.repositories(56855)
    >>> repos[0].name
    u'org_repo_test'
