.. Copyright (C) 2011-2012 James Rowe <jnrowe@gmail.com>

   This file is part of python-github2, is licensed under the 3-clause BSD
   License.  See the LICENSE file in the top distribution directory for the full
   license text.

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
