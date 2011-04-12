Repository
==========

.. py:currentmodule:: github2.repositories

.. autoclass:: Repository(type)

.. autoclass:: Repositories(type)

Examples
--------

Searching Repositories
''''''''''''''''''''''

    >>> repositories = github.repos.search("django")


Show Repo Info
''''''''''''''

    >>> repo = github.repos.show("schacon/grit")
    >>> repo.homepage
    "http://grit.rubyforge.org/"

List All Repositories
'''''''''''''''''''''

    # By default lists all repos for the current user.
    >>> repos = github.repos.list()

    >>> repos = github.repos.list("schacon")

Watching Repositories
'''''''''''''''''''''

    >>> github.repos.watch("schacon/grit")

    >>> github.repos.unwatch("schacon/grit")

Forking Repositories
''''''''''''''''''''

    >>> fork = github.repos.fork("schacon/grit")

Creating and Deleting Repositories
''''''''''''''''''''''''''''''''''

    >>> new_repo = github.repos.create(name, description, homepage,
    ...                                 public=True)

    >>> github.repos.delete(name)

Repository Visibility
'''''''''''''''''''''

    >>> github.repos.set_private("ask/chishop")

    >>> github.repos.set_public("ask/chishop")

Pushable repositories
'''''''''''''''''''''

    >>> pushables = github.repos.pushable()

Collaborators
'''''''''''''

    >>> collabs = github.repos.list_collaborators("ask/chishop")

    >>> github.repos.add_collaborator("ask/chishop", "schacon")

    >>> github.repos.remove_collaborator("ask/chishop", "schacon")

Watchers
''''''''

    >>> watchers = github.repos.watchers("ask/chishop")


Network
'''''''

    >>> github.repos.network("ask/chishop")

Repository Refs
'''''''''''''''

Get a list of tags

    >>> tags = github.repos.tags("ask/chishop")

Get a list of remote branches

    >>> branches = github.repos.branches("ask/chishop")
