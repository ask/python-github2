==================================================================================
python-github2 - Github API v2 library for Python.
==================================================================================

:Authors:
    Ask Solem (askh@opera.com)
:Version: 0.1.2

This is an experimental python library implementing all of the features
available in version 2 of the `Github API`_.

*Note* This software is not finished. And is likely to change in the near future.

.. _`Github API`: http://develop.github.com/

Introduction
------------

You should read the developer documentation for the `Github API`_ first.

Installation
=============

You can install ``python-github2`` either via the Python Package Index (PyPI)
or from source.

To install using ``pip``,::

    $ pip install python-github2

To install using ``easy_install``,::

    $ easy_install python-github2

If you have downloaded a source tarball you can install it
by doing the following,::

    $ python setup.py build
    # python setup.py install # as root

Creating a request
==================

    >>> from github2.client import Github
    >>> github = Github(username="ask", api_token=".......")

Users
=====

Searching
---------

    >>> results = github.users.search("foo")

Getting User Information
------------------------

    >>> user = github.users.show("ask")
    >>> user.name
    "Ask Solem"

Getting User Network
---------------------

    >>> github.users.followers("ask")
    ['greut', 'howiworkdaily', 'emanchado', 'webiest']

    >>> github.users.following("ask")
    ['sverrejoh',
    'greut',
    'jezdez',
    'bradleywright',
    'ericflo',
    'howiworkdaily',
    'emanchado',
    'traviscline',
    'russell']

Following Network
------------------

    >>> github.users.follow("jezdez")

    >>> github.users.unfollow("jezdez")

Issues
======

List a Projects Issues
----------------------

    >>> github.issues.list("ask/chishop", state="open")
    >>> github.issues.list("ask/chishop", state="closed")

View an Issue
-------------

    >>> issue = github.issues.show("ask/chishop", 1)
    >>> issue.title
    'Should not be able to upload same version twice.'

Open and Close Issues
---------------------

    >>> new_issue = github.issues.open("ask/chishop", title="New bug",
    ...                                body="This is a test bug")
    >>> new_issue.number
    2

    >>> github.issues.close("ask/chishop", new_issue.number)


Add and Remove Labels
---------------------

    >>> github.issues.add_label("ask/chishop", 2, "important")

    >>> github.issues.remove_label("ask/chishop", 2, "important")


Network
=======

Network Meta
-------------

    >>> github.get_network_meta("ask/chishop")

Network Data
------------

    >>> github.get_network_data("schacon/simplegit",
    ...     nethash="fa8fe264b926cdebaab36420b6501bd74402a6ff")


Repository
==========

Searching Repositories
----------------------

    >>> repositories = github.repos.search("django")


Show Repo Info
--------------

    >>> repo = github.repos.show("schacon/grit")
    >>> repo.homepage
    "http://grit.rubyforge.org/"

List All Repositories
---------------------

    # By default lists all repos for the current user.
    >>> repos = github.repos.list()

    >>> repos = github.repos.list("schacon")

Watching Repositories
---------------------

    >>> github.repos.watch("schacon/grit")

    >>> github.repos.unwatch("schacon/grit")

Forking Repositories
--------------------

    >>> fork = github.repos.fork("schacon/grit")

Creating and Deleting Repositories
----------------------------------

    >>> new_repo = github.repos.create(name, description, homepage,
    ...                                 public=True)

    >>> github.repos.delete(name)

Repository Visibility
---------------------

    >>> github.repos.set_private("ask/chishop")

    >>> github.repos.set_public("ask/chishop")

Collaborators
-------------

    >>> collabs = github.repos.list_collaborators("ask/chishop")

    >>> github.repos.add_collaborator("ask/chishop", "schacon")
    
    >>> github.repos.remove_collaborator("ask/chishop", "schacon")

Network
-------

    >>> github.repos.network("ask/chishop")

Repository Refs
---------------

    Get a list of tags

    >>> tags = github.repos.tags("ask/chishop")

    Get a list of remote branches

    >>> branches = github.repos.branches("ask/chishop") 


Commit
======

Listing Commits on a Branch
----------------------------

    >>> commits = github.commits.list("mojombo/grit", "master")


Listing Commits for a File
--------------------------

    >>> commits = github.commits.list("mojombo/grit", "master",
    ...                               file="grit.gemspec")

Showing a Specific Commit
-------------------------

    >>> commit = github.commits.show("mojombo/grit",
    ...             sha="5071bf9fbfb81778c456d62e111440fdc776f76c")
    

Object
======

Trees
-----

    >>> tree = github.get_tree(project, tree_sha)

Blobs
-----

    >>> blob = github.get_blob_info(project, tree_sha, path)


License
=======

This software is licensed under the ``New BSD License``. See the ``LICENSE``
file in the top distribution directory for the full license text.

.. # vim: syntax=rst expandtab tabstop=4 shiftwidth=4 shiftround
