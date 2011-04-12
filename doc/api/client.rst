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

If you authenticated to GitHub using their OAuth service, pass in the OAuth
access token::

    >>> github = Github(access_token="........")

Or for an unauthenticated connection::

    >>> github = Github()

The package supports caching of GitHub responses by adding a ``cache`` keyword
during setup::

    >>> github = Github(username="ask", api_token=".......", cache="cache_dir")

API calls are limited by github.com to 1 per second by default.  To have the
Github client enforce this and avoid rate limit errors, pass requests_per_second
in::

    >>> from github2.client import Github
    >>> github = Github(username="ask", api_token=".......",
    ...                 requests_per_second=1)
