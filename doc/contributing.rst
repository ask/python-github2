Contributing
============

Patches for :mod:`github2` are most welcome!

Forks on GitHub_ and patches attached to issues are both great ways to
contribute.  If you're comfortable with ``git`` using a fork hosted on GitHub is
probably the simpler solution, both for the package maintainers and you as a
contributor.

Following the simple guidelines below makes it easier to review and integrate
your changes:

* `PEP 8`_, the Python style guide, should be followed where possible
* Adding documentation for new methods and classes is very important
* Testing your changes with multiple Python versions is fantastically useful, it
  is all too easy to use functionality that exists in only specific Python
  versions

The documentation format used in the code's docstrings is Sphinx_
autodoc_-compatible.  If you're not comfortable with the format, a close
approximation is good enough.  It is often easier to fix broken formatting than
write documentation from scratch.

Documentation patches and the addition of new examples are as equally
appreciated as patches to code.

Tests
-----

.. note::
   Unfortunately there aren't many tests for ``python-github`` at the moment,
   any patches to increase test coverage are greatly appreciated

The preferred way to run the package's tests is with nose_.  ``nosetests``
provides excellent reporting options and its additional features make it
invaluable, see the nose_ documentation for usage information.

There is a tox_ configuration file included in the repository, you can use it to
run the tests against multiple Python versions with a single command.  The
configuration file also includes targets for testing the documentation.  The
tox_ documentation includes a fantastic number of examples on how to use it, or
add new testing targets.

.. todo::
   Add topic branches and pull request usage examples, but most git users are
   likely to be comfortable with these already

.. _GitHub: https://github.com/ask/python-github2/
.. _PEP 8: http://www.python.org/dev/peps/pep-0008/
.. _Sphinx: http://sphinx.pocoo.org/
.. _autodoc: http://sphinx.pocoo.org/ext/autodoc.html#module-sphinx.ext.autodoc
.. _nose: http://somethingaboutorange.com/mrl/projects/nose/
.. _tox: http://pypi.python.org/pypi/tox/
