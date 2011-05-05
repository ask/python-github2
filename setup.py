#!/usr/bin/env python
# -*- coding: utf-8 -*-
import codecs
import sys

from setuptools import setup, find_packages

import github2


install_requires = ['httplib2', ]

long_description = (codecs.open('README.rst', "r", "utf-8").read()
    + "\n" + codecs.open('NEWS.rst', "r", "utf-8").read())

setup(
    name='github2',
    version=github2.__version__,
    description=github2.__doc__,
    long_description=long_description,
    author=github2.__author__,
    author_email=github2.__contact__,
    url=github2.__homepage__,
    license='BSD',
    keywords="git github api",
    platforms=["any"],
    packages=find_packages(exclude=['tests']),
#    scripts=['github2/bin/github_manage_collaborators'],
#    setup_requires=["sphinxcontrib-cheeseshop"],
    install_requires=install_requires,
    zip_safe=True,
    test_suite="tests",
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: BSD License",
        "Operating System :: OS Independent",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3.0",
        "Programming Language :: Python :: 3.1",
        "Programming Language :: Python :: 3.2",
        "Topic :: Software Development",
        "Topic :: Software Development :: Libraries",
    ],
)
