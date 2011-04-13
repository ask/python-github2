Object
======

.. py:currentmodule:: github2.client

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
