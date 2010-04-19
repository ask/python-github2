#!/usr/bin/env python
# -*- coding: utf-8 -*-
import codecs

try:
    from setuptools import setup, find_packages
except ImportError:
    from ez_setup import use_setuptools
    use_setuptools()
    from setuptools import setup, find_packages

import github2

setup(
    name='github2',
    version=github2.__version__,
    description=github2.__doc__,
    author=github2.__author__,
    author_email=github2.__contact__,
    url=github2.__homepage__,
    platforms=["any"],
    packages=find_packages(exclude=['ez_setup']),
    scripts=['github2/bin/github_manage_collaborators'],
    install_requires=[
    ],
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Operating System :: OS Independent",
        "Programming Language :: Python",
    ],
    long_description=codecs.open('README.rst', "r", "utf-8").read(),
)
