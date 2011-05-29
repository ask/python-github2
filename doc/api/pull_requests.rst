Pull requests
=============

.. py:currentmodule:: github2.pull_requests

.. autoclass:: PullRequest(type)

.. autoclass:: PullRequests(type)

Examples
--------

Listing pull requests
'''''''''''''''''''''

    >>> results = github.pull_requests.list("ask/python-github2")

View a pull request
'''''''''''''''''''

    >>> request = github.pull_requests.show("ask/python-github2", 28)
    >>> pull.body
    'This implements the github API pull requests functionality. '

Open pull request
'''''''''''''''''

To open a new pull request::

    >>> pull = github.pull_requests.create("ask/python-github2", "master",
    ...                                    "JNRowe:my_new_branch",
    ...                                    title="Fancy features")
    >>> pull.number
    4

To attach code to an existing issue::

    >>> pull = github.pull_requests.create("ask/python-github2", "master",
    ...                                    "JNRowe:my_new_branch",
    ...                                    issue=4)
