.. module:: github2.commits

Commit
======

.. note::

   See the official GitHub API v2 documentation for commits_.

.. _commits: http://develop.github.com/p/commits.html

.. autoclass:: Commit(type)

.. autoclass:: Commits(type)

Examples
--------

Listing Commits on a Branch
'''''''''''''''''''''''''''

    >>> commits = github.commits.list("mojombo/grit", "master")

By default the first page of results is returned, you can return further results
with the ``page`` parameter:

    >>> commits = github.commits.list("mojombo/grit", "master", page=2)

Listing Commits for a File
''''''''''''''''''''''''''

    >>> commits = github.commits.list("mojombo/grit", "master",
    ...                               file="grit.gemspec")

Showing a Specific Commit
'''''''''''''''''''''''''

    >>> commit = github.commits.show("mojombo/grit",
    ...             sha="5071bf9fbfb81778c456d62e111440fdc776f76c")
