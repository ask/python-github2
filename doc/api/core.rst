.. module:: github2.core

Core
====

.. note::
   This module contains functionality that isn't useful to general users
   of the :mod:`github2` package, but it is documented to aid contributors
   to the package.

.. autodata:: NAIVE(bool)

   Set to ``False`` for timezone-aware :class:`datetime.datetime` objects

.. autodata:: GITHUB_TZ(datetime.tzinfo)

   Timezone used in output from GitHub API, currently defined as
   ``America/Los_Angeles`` in the Olson database

.. autofunction:: string_to_datetime

.. autofunction:: datetime_to_ghdate
.. autofunction:: datetime_to_commitdate
.. autofunction:: datetime_to_isodate

.. autofunction:: requires_auth
.. autofunction:: enhanced_by_auth

.. autofunction:: doc_generator

.. autofunction:: repr_string

.. autoclass:: GithubCommand

.. autoclass:: Attribute

.. autoclass:: DateAttribute(help, format)

.. autoclass:: BaseData()
