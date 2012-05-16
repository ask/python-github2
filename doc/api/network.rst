.. Copyright (C) 2011-2012 James Rowe <jnrowe@gmail.com>

   This file is part of python-github2, is licensed under the 3-clause BSD
   License.  See the LICENSE file in the top distribution directory for the full
   license text.

.. currentmodule:: github2.client

Network
=======

.. automethod:: Github.get_network_meta

.. automethod:: Github.get_network_data

Examples
--------

Network Meta
''''''''''''

    >>> github.get_network_meta("ask/chishop")

Network Data
''''''''''''

    >>> github.get_network_data("schacon/simplegit",
    ...     nethash="fa8fe264b926cdebaab36420b6501bd74402a6ff")
