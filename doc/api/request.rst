.. Copyright (C) 2011-2012 James Rowe <jnrowe@gmail.com>

   This file is part of python-github2, is licensed under the 3-clause BSD
   License.  See the LICENSE file in the top distribution directory for the full
   license text.

.. module:: github2.request

Requests
========

.. note::
   This module contains functionality that isn't useful to general users
   of the :mod:`github2` package, but it is documented to aid contributors
   to the package.

.. autodata:: DEFAULT_GITHUB_URL

.. autodata:: SYSTEM_CERTS
.. autodata:: CURL_CERTS

.. autoexception:: GithubError

.. autoclass:: GithubRequest
   :exclude-members: GithubError
