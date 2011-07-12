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
