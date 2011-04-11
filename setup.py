#!/usr/bin/env python
# -*- coding: utf-8 -*-
import codecs
import sys

try:
    from setuptools import setup, find_packages
except ImportError:
    from ez_setup import use_setuptools
    use_setuptools()
    from setuptools import setup, find_packages

import github2


install_requires = ['httplib2', ]
# simplejson is included in the standard library since Python 2.6 as json.
if sys.version_info[:2] < (2, 6):
    install_requires.append('simplejson >= 2.0.9')


setup(
    name='github2',
    version=github2.__version__,
    description=github2.__doc__,
    author=github2.__author__,
    author_email=github2.__contact__,
    url=github2.__homepage__,
    license='BSD',
    platforms=["any"],
    packages=find_packages(exclude=['ez_setup', 'tests']),
    scripts=['github2/bin/github_manage_collaborators'],
    install_requires=install_requires,
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: BSD License",
        "Operating System :: OS Independent",
        "Programming Language :: Python",
        "Programming Language :: Python :: 2",
        "Programming Language :: Python :: 2.4",
        "Programming Language :: Python :: 2.5",
        "Programming Language :: Python :: 2.6",
        "Programming Language :: Python :: 2.7",
        "Topic :: Software Development",
        "Topic :: Software Development :: Libraries",
    ],
    long_description=codecs.open('README.rst', "r", "utf-8").read(),
)
