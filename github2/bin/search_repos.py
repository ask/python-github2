#! /usr/bin/env python
# coding: utf-8
"""github_search_repos - search for repositories on GitHub"""


import logging
import sys

from optparse import OptionParser
from textwrap import wrap

import github2.client


#: Running under Python 3
PY3K = sys.version_info[0] == 3 and True or False


def print_(text):
    """Python 2 & 3 compatible print function

    We support <2.6, so can't use __future__.print_function"""
    if PY3K:
        print(text)
    else:
        sys.stdout.write(text + '\n')


def parse_commandline():
    """Parse the comandline and return parsed options."""

    parser = OptionParser()
    parser.description = __doc__

    parser.set_usage('usage: %prog [options] <term>')
    parser.add_option('-d', '--debug', action='store_true',
                      help='Enables debugging mode')
    parser.add_option('-c', '--cache', default=None,
                      help='Location for network cache [default: None]')

    options, args = parser.parse_args()
    if len(args) != 1:
        parser.error('wrong number of arguments')

    return options, args[0]


def main():
    """This implements the actual program functionality"""
    return_value = 0

    options, term = parse_commandline()

    github = github2.client.Github(cache=options.cache)

    # PEP-308 conditional expressions are much better, but we're keeping Py2.4
    # compatibility elsewhere.
    logging.basicConfig(level=options.debug and logging.DEBUG or logging.WARN,
                        format="%(asctime)s - %(message)s",
                        datefmt="%Y-%m-%dT%H:%M:%S")

    repos = github.repos.search(term)
    if not repos:
        print_('No repos found!')
        return_value = 255
    else:
        for repo in repos:
            print(repo.project)
            if repo.description:
                print_('\n'.join(wrap(repo.description, initial_indent='    ',
                                     subsequent_indent='    ')))

    logging.shutdown()
    return return_value


if __name__ == '__main__':
    sys.exit(main())
