Installation
------------

You can install ``python-github2`` either via the Python Package Index (PyPI) or
from source.

To install using ``pip``::

    $ pip install github2

To install using ``easy_install``::

    $ easy_install github2

If you have downloaded a source tarball you can install it by doing the
following::

    $ python setup.py build
    $ python setup.py install --user  # to install for a single user
    # python setup.py install  # to install in Python's site-packages

``python-github2`` depends on httplib2_, an excellent package by Joe Gregorio
for handling HTTP sessions.  simplejson_ is also required when using
``python-github2`` with Python 2.4 or 2.5.  If you install via ``pip`` or
``easy_install`` the dependencies should be installed automatically for you.

.. _httplib2: http://code.google.com/p/httplib2/
.. _simplejson: http://pypi.python.org/pypi/simplejson/
