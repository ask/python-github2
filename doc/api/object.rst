.. currentmodule:: github2.client

Object
======

See the official GitHub API v2 documentation for objects_.

.. _objects: http://develop.github.com/p/object.html

.. automethod:: Github.get_all_blobs

.. automethod:: Github.get_blob_info

.. automethod:: Github.get_tree

Examples
--------

Trees
'''''

    >>> tree = github.get_tree(project, tree_sha)

Blobs
'''''

    >>> blob = github.get_blob_info(project, tree_sha, path)

All Blobs
'''''''''

    >>> blobs = github.get_all_blobs(project, tree_sha)
