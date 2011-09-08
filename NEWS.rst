User-visible changes
====================

.. contents::

0.5.2 - 2011-09-02
------------------

* Functions that returned `dict` objects have been deprecated, enable
  DeprecationWarning_ support to see if you're affected

.. _DeprecationWarning: http://docs.python.org/library/warnings.html

0.5.1 - 2011-06-11
------------------

* This is a bugfix release for compatibility with the latest httplib2_ release
* httplib2_ v0.7.0, or higher, is required

0.5.0 - 2011-05-24
------------------

* Support for `pull requests`_
* Simple logging_ based messages for event tracking and debugging
* Requires python-dateutil_

.. _pull requests: http://develop.github.com/p/pulls.html
.. _logging: http://docs.python.org/library/logging.html
.. _python-dateutil: http://pypi.python.org/pypi/python-dateutil

0.4.0 - 2011-05-23
------------------

* Python 3 compatibility
* The ``github_manage_collaborators`` script will be installed using
  ``entry_points``, which means there is now a run-time dependency on
  distribute_
* Support for managing `teams and organisations`_
* HTTP proxy support

.. _teams and organisations: http://develop.github.com/p/orgs.html
.. _distribute: http://pypi.python.org/pypi/distribute

0.3.0 - 2011-04-13
------------------

* Caching support, see the ``cache`` keyword of ``github.client.Github``
* OAuth2_ authentication support
* Additional ``issues`` support:

  + Searching issues with ``issues.search``
  + List issues by label with ``issues.list_by_label``
  + List all project labels with ``issues.list_labels``
  + Edit an existing issue with ``issues.edit``
  + Reopen closed issues with ``issues.reopen``

* Additional ``repos`` support

  + List non-owned projects that you have push rights to with ``repos.pushable``

* Requires httplib2_

.. _OAuth2: http://develop.github.com/p/oauth.html
.. _httplib2: http://code.google.com/p/httplib2/
