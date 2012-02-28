Release HOWTO
=============

.. highlight:: sh

..
  Much of this stuff is automated locally, but I'm describing the process for
  other people who will not have access to the same release tools I use.  The
  first thing I recommend that you do is find/write a tool that allows you to
  automate all of this, or you're going to miss important steps at some point.

Test
----

In the general case tests can be run via :pypi:`nose`'s :pypi:`distribute`
integration::

    $ ./setup.py nosetests

When preparing a release it is important to check that :mod:`github2` works with
all currently supported Python versions, and that the documentation is correct.
To that end you can use :pypi:`tox` to run the full testsuite::

    $ tox -v

This will test :mod:`github2` with Python 2.4 → 3.2, check that the ``reST``
syntax is valid and also that the :pypi:`sphinx` documentation builds correctly.
You can run a subset of these options too, see the ``tox`` documentation for
more information.

Prepare release
---------------

With the tests passing, perform the following steps

* Update the version data in :file:`github2/_version.py`, and also the
  reference in :file:`README.rst`
* Update :file:`NEWS.rst`, if there are any user visible changes
* Commit the release notes and version changes
* Create a signed tag for the release
* Push the changes, including the new tag, to the GitHub repository

Update PyPI
-----------

..
  This is the section you're especially likely to get wrong at some point if you
  try to handle all of this manually ;)

Create and upload the new release tarballs to PyPI::

    $ ./setup.py sdist --formats=bztar,gztar register upload --sign

You should also update the hosted documentation too::

    $ ./setup.py build_sphinx && ./setup.py upload_docs

Fetch the uploaded tarballs, and check for errors.

You should also perform test installations from PyPI, to check the experience
:mod:`github2` users will have.

.. highlight:: python
