Reporting bugs
==============

If you think you've found a bug, or inconsistency, in :mod:`github2` please
`report an issue`_.

.. note::
   Please don't report bugs via email, this limits who can work on a bug or
   suggest solutions to a bug.  It also makes it impossible for other users to
   search the database of known bugs, which can often lead to duplicated
   effort.

We also use the issue tracker to track feature requests and ideas.  Having all
this information in a single place makes it easier for new contributors to jump
in.

When is a bug not a bug
-----------------------

With packages, such as :mod:`github2`, that wrap external resources it can be
hard to track down the actual cause of a bug.  The first step when you've found
a bug should be to test it directly, to rule out a temporary problem with GitHub
or a deficiency in the API.

You can check which URLs your code is requesting by enabling
:data:`~logging.DEBUG` level output in your logger, see the
:mod:`python:logging` documentation for details.

If the bug you've found is outside the reach of this project an issue should be
opened in GitHub's `API support forum`_.  It doesn't hurt to `report an issue`_
in this project's issue tracker, and you may find someone knows a workaround for
the problem until GitHub's crack team of developers can fix the problem.

Anatomy of a good bug report
----------------------------

Filing a good report makes it easier to fix bugs, and making it easier to work
on your bug means it is likely to be fixed much faster!

A good bug report will have the following:

* A descriptive title
* A full Python traceback of the error, if there is one
* The version of :mod:`github2` you are using [#]_
* A minimal test-case to reproduce the error
* A list of solutions you've already tried

Simon Tatham wrote aa fantastic essay titled `How to Report Bugs Effectively`_,
with some excellent tips on filing good bug reports.

.. [#] The value of :data:`github2.__version__` if you're using an official
   release, or the output of :command:`git describe` if you're using the git
   repository directly.

.. _report an issue: https://github.com/ask/python-github2/issues/
.. _API support forum: http://support.github.com/discussions/api
.. _How to Report Bugs Effectively: http://www.chiark.greenend.org.uk/~sgtatham/bugs.html
