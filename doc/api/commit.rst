.. module:: github2.commits

Commit
======

.. autoclass:: Commit(type)

.. autoclass:: Commits(type)

Examples
--------

Listing Commits on a Branch
'''''''''''''''''''''''''''

    >>> commits = github.commits.list("mojombo/grit", "master")


Listing Commits for a File
''''''''''''''''''''''''''

    >>> commits = github.commits.list("mojombo/grit", "master",
    ...                               file="grit.gemspec")

Showing a Specific Commit
'''''''''''''''''''''''''

    >>> commit = github.commits.show("mojombo/grit",
    ...             sha="5071bf9fbfb81778c456d62e111440fdc776f76c")
