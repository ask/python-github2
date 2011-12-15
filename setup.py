#!/usr/bin/env python
# -*- coding: utf-8 -*-
import codecs
import sys

from setuptools import setup, find_packages

import github2


install_requires = ['httplib2 >= 0.7.0', ]
# simplejson is included in the standard library since Python 2.6 as json.
if sys.version_info[:2] < (2, 6):
    install_requires.append('simplejson >= 2.0.9')

if sys.version_info >= (3,):
    install_requires.append('python-dateutil >= 2.0')
else:
    install_requires.append('python-dateutil < 2.0')

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
    include_package_data=True,
    package_data={'': ['*.crt', ], },
    entry_points={
        'console_scripts': [
            'github_manage_collaborators = github2.bin.manage_collaborators:main',
            'github_search_repos = github2.bin.search_repos:main',
        ],
    },
    install_requires=install_requires,
    zip_safe=True,
    test_suite="nose.collector",
    tests_require=['nose'],
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: BSD License",
        "Operating System :: OS Independent",
        "Programming Language :: Python",
        "Programming Language :: Python :: 2",
        "Programming Language :: Python :: 2.4",
        "Programming Language :: Python :: 2.5",
        "Programming Language :: Python :: 2.6",
        "Programming Language :: Python :: 2.7",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.1",
        "Programming Language :: Python :: 3.2",
        "Topic :: Software Development",
        "Topic :: Software Development :: Libraries",
    ],
)
