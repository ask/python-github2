Teams
=====

.. currentmodule:: github2.teams

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
