.. module:: github2.issues

Issues
======

.. note::

   See the official GitHub API v2 documentation for issues_.

.. _issues: http://develop.github.com/p/issues.html

.. autoclass:: Issue(type)

.. autoclass:: Comment(type)

.. autoclass:: Issues(type)

Examples
--------

List a Projects Issues
''''''''''''''''''''''

    >>> github.issues.list("ask/chishop", state="open")
    >>> github.issues.list("ask/chishop", state="closed")

Search a Projects Issues
''''''''''''''''''''''''

    >>> issues = github.issues.search("ask/chishop", "version twice")
    >>> issues[0].title
    'Upload hangs on attempted second file.'

    >>> github.issues.search("ask/chishop", term="authorization",
    ...                      state="closed")

View an Issue
'''''''''''''

    >>> issue = github.issues.show("ask/chishop", 1)
    >>> issue.title
    'Should not be able to upload same version twice.'

View Comments on an Issue
'''''''''''''''''''''''''

    >>> comments = github.issues.comments("ask/chishop", 5)
    >>> comments[0].body
    'Fix merged into /ask branch.'

Open and Close Issues
'''''''''''''''''''''

    >>> new_issue = github.issues.open("ask/chishop", title="New bug",
    ...                                body="This is a test bug")
    >>> new_issue.number
    2

    >>> github.issues.close("ask/chishop", new_issue.number)
    >>> github.issues.reopen("ask/chishop", new_issue.number)

List Labels
'''''''''''

    >>> github.issues.list_labels("ask/chisop")
    [u'TODO', u'ask']
    >>> github.issues.list_by_label("ask/chishop", "TODO")
    [<Issue: Should not be able to upload same version twice.>]

Add and Remove Labels
'''''''''''''''''''''

    >>> github.issues.add_label("ask/chishop", 2, "important")

    >>> github.issues.remove_label("ask/chishop", 2, "important")

Edit an Issue
'''''''''''''

    >>> github.issues.edit("ask/chishop", 3, title="New title",
    ...                    body="New body")
