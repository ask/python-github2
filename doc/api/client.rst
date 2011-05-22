.. module:: github2.client

Creating a client
=================

.. autoclass:: github2.client.Github
   :exclude-members:
    get_network_meta, get_network_data, get_all_blobs, get_blob_info, get_tree

Examples
--------

There are three ways to authenticate to the GitHub API.  If you want to use your
username and API token, use::

    >>> from github2.client import Github
    >>> github = Github(username="ask", api_token=".......")

If you authenticated to GitHub using their `OAuth service`_, pass in the OAuth
access token::

    >>> github = Github(access_token="........")

.. note::
   You can retrieve the user data for an OAuth authenticated user with
   ``github.users.show("")``.

Or for an unauthenticated connection::

    >>> github = Github()

The package supports caching of GitHub responses by adding a ``cache`` keyword
during setup::

    >>> github = Github(username="ask", api_token=".......", cache="cache_dir")

API calls are limited by github.com to 1 per second by default.  To have the
``Github`` client enforce this and avoid rate limit errors, pass
``requests_per_second`` in::

    >>> from github2.client import Github
    >>> github = Github(username="ask", api_token=".......",
    ...                 requests_per_second=1)

If you wish to use the library with a HTTP proxy, you will require a Python
SOCKS module installed.  :pypi:`SocksiPy-branch` is the module we test with, but
various forks are available.  Pass in the ``proxy_host`` and optionally
``proxy_port`` settings to enable it.  The default for ``proxy_port``, if not
given, is 8080::

    >>> from github2.client import Github
    >>> github = Github(username="ask", api_token=".......",
    ...                 proxy_host="my.proxy.com", proxy_port=9000)

.. _OAuth service: http://develop.github.com/p/oauth.html
