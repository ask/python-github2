.. module:: github2.pull_requests

Pull requests
=============

See the official GitHub API v2 documentation for `pull requests`_.

.. _pull_requests: http://develop.github.com/p/pulls.html

.. autoclass:: PullRequest(type)

.. autoclass:: PullRequests(type)

Examples
--------

Listing pull requests
'''''''''''''''''''''

    >>> results = github.pull_requests.list("ask/python-github2")

By default the first page of results is returned, you can return further results
with the ``page`` parameter:

    >>> results = github.pull_requests.list("ask/python-github2", page=2)

View a pull request
'''''''''''''''''''

    >>> request = github.pull_requests.show("ask/python-github2", 28)
    >>> pull.body
    'This implements the github API pull requests functionality. '

Open pull request
'''''''''''''''''

To open a new pull request against the ``ask/python-github2`` project::

    >>> pull = github.pull_requests.create("ask/python-github2", "master",
    ...                                    "JNRowe:my_new_branch",
    ...                                    title="Fancy features")
    >>> pull.number
    4

This creates a pull request for changes in ``JNRowe``'s ``my_new_branch`` and
asks for it to be merged to ``ask``'s ``master`` branch.

To attach code to an existing issue and make it a pull request::

    >>> pull = github.pull_requests.create("ask/python-github2", "master",
    ...                                    "JNRowe:my_new_branch",
    ...                                    issue=4)

.. note::

   You can use any ``tree-ish`` for the ``head`` argument, you are not
   restricted to symbolic references.
