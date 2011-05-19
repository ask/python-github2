Installation
------------

You can install :mod:`github2` either via the Python Package Index (PyPI) or
from source.

To install using ``pip``::

    $ pip install github2  # to install in Python's site-packages
    $ pip install --install-option="--user" github2  # to install for a single user

To install using ``easy_install``::

    $ easy_install github2

If you have downloaded a source tarball you can install it by doing the
following::

    $ python setup.py build
    # python setup.py install  # to install in Python's site-packages
    $ python setup.py install --user  # to install for a single user

:mod:`github2` depends on :pypi:`httplib2`, an excellent package by Joe
Gregorio for handling HTTP sessions.  :pypi:`simplejson` is also required when
using :mod:`github2` with Python 2.4 or 2.5.  If you install via ``pip`` or
``easy_install`` the dependencies should be installed automatically for you.
:pypi:`SocksiPy-branch` is an optional dependency if proxy support is needed.
