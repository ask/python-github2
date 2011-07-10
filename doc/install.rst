Installation
------------

You can install :mod:`github2` either via the Python Package Index (PyPI) or
from source.

To install using :pypi:`pip`::

    $ pip install github2  # to install in Python's site-packages
    $ pip install --install-option="--user" github2  # to install for a single user

To install using :pypi:`easy_install <setuptools>`::

    $ easy_install github2

If you have downloaded a source tarball you can install it by doing the
following::

    $ python setup.py build
    # python setup.py install  # to install in Python's site-packages
    $ python setup.py install --user  # to install for a single user

:mod:`github2` depends on :pypi:`httplib2`, an excellent package by Joe Gregorio
for handling HTTP sessions.  :pypi:`python-dateutil` is used for its date
handling [#]_.  :pypi:`simplejson` is also required when using :mod:`github2`
with Python 2.4 or 2.5.  If you install via :pypi:`pip` or :pypi:`easy_install
<setuptools>` the dependencies should be installed automatically for you.

.. [#] You must use :pypi:`python-dateutil` 1.x when working with Python 2.x,
       the latest 2.x releases are for Python 3.x installations only.
