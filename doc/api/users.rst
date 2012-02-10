.. module:: github2.users

Users
=====

.. note::

   See the official GitHub API v2 documentation for users_.

.. _users: http://develop.github.com/p/teams.html

.. autoclass:: User(type)

.. autoclass:: Users(type)

.. autoclass:: Key(type)

Examples
--------

Searching
'''''''''

    >>> results = github.users.search("foo")

Getting User Information
''''''''''''''''''''''''

    >>> user = github.users.show("ask")
    >>> user.name
    "Ask Solem"

Getting User Network
''''''''''''''''''''

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
'''''''''''''''''

    >>> github.users.follow("jezdez")

    >>> github.users.unfollow("jezdez")
