User-visible changes
====================

.. contents::

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
