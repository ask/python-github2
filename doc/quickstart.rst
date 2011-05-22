Quickstart
==========

Once :mod:`github2` is :doc:`installed <install>` we can open an interactive
Python session and perform some basic tasks to familiarise ourselves with the
package.

Create an unauthenticated client object::

    >>> github = Github()

.. note::
   Creating an unauthenticated client object means we can play with the API
   without fear of creating or deleting data on our account.

See how many followers the :mod:`github2` project has::

    >>> len(github.repos.watchers("ask/python-github2"))
    129

Read the description of the ``python-github2`` project::

    >>> repo = github.repos.show("ask/python-github2")
    >>> repo.description

We can take advantage of Python's :func:`dir` to explore the package a
little more::

    >>> filter(lambda s: not s.startswith("_"), dir(github.users))
    ['domain', 'follow', 'followers', 'following', 'get_value', 'get_values',
     'make_request', 'request', 'search', 'search_by_email', 'show',
     'unfollow']

For more information on specific functionality see the :doc:`api/index`, and the
copious examples contained within.
