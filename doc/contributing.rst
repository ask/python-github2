Contributing
============

Patches for :mod:`github2` are most welcome!

Forks on GitHub_ and patches attached to issues are both great ways to
contribute.  If you're comfortable with ``git`` using a fork hosted on GitHub is
probably the simpler solution, both for the package maintainers and you as a
contributor.

Following the simple guidelines below makes it easier to review and integrate
your changes:

* :pep:`8`, the Python style guide, should be followed where possible
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
   Unfortunately test coverage isn't as high as one would hope, patches to
   increase test coverage are greatly appreciated!

The preferred way to run the package's tests is with :pypi:`nose`.
``nosetests``, nose's command-line test runner, provides excellent reporting
options and its additional features make it invaluable, see the nose_
documentation for usage information.

There is a :pypi:`tox` configuration file included in the repository, you can
use it to run the tests against multiple Python versions with a single command.
The configuration file also includes targets for testing the documentation.  The
tox_ documentation includes a fantastic number of examples on how to use it, and
advice on adding new testing targets.

Notes
-----

:mod:`github2` supports Python 2.4-3.2, so some attention to compatibility
between Python releases needs to be made when writing code.

The official Python docs provide a fantastically useful `index of changes`_
between versions.

.. note::
   If you don't have access to multiple releases of Python it is still possible
   to contribute.  However, it may take a little longer to merge your pull
   request if additional work needs to be done to make the code compatible with
   all the supported Python releases.

Test specific concerns
''''''''''''''''''''''

The :mod:`unittest` module received a massive upgrade in Python 2.7, including
some very useful new functionality.  However, retaining compatibility with older
Python versions is very important, so this new functionality can't be used.
Some specific issues to bear in mind are listed below.

Many assertions, such as :meth:`~unittest.TestCase.assertIn` and
:meth:`~unittest.TestCase.assertGreater`, only exist from 2.7, and can't be used.
The simple workaround is to evaluate an expression to test with
:meth:`~unittest.TestCase.assertTrue`

The incredibly useful functions for skipping tests(:func:`~unittest.skip`) and
marking expected failures(:func:`~unittest.expectedFailure`) were only added in
2.7, and unfortunately can't be used.

.. todo::
   Add topic branches and pull request usage examples, but most git users are
   likely to be comfortable with these already

.. _GitHub: https://github.com/ask/python-github2/
.. _Sphinx: http://sphinx.pocoo.org/
.. _autodoc: http://sphinx.pocoo.org/ext/autodoc.html#module-sphinx.ext.autodoc
.. _nose: http://somethingaboutorange.com/mrl/projects/nose/
.. _tox: http://pypi.python.org/pypi/tox/
.. _index of changes: http://docs.python.org/whatsnew/index.html
