#!/usr/bin/env python
# encoding: utf-8
"""github_manage_collaborators - add/remove collaborators to all github
projects of an account.

Typically used with company accounts where all coders should have
R/W access to all private repositories of the company account.
"""

# Created by Maximillian Dornseif on 2009-12-31 for HUDORA.
# Copyright (c) 2009 HUDORA. All rights reserved.
# BSD licensed

import logging
import sys

from optparse import OptionParser

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

    parser.set_usage('usage: %prog [options] (list|add|remove) [collaborator].'
                     '\nTry %prog --help for details.')
    parser.add_option('-d', '--debug', action='store_true',
                      help='Enables debugging mode')
    parser.add_option('-c', '--cache', default=None,
                      help='Location for network cache [default: None]')
    parser.add_option('-l', '--login',
                      help='Username to login with')
    parser.add_option('-a', '--account',
                      help='User owning the repositories to be changed ' \
                           '[default: same as --login]')
    parser.add_option('-t', '--apitoken',
                      help='API Token - can be found on the lower right of ' \
                           'https://github.com/account')

    options, args = parser.parse_args()
    if len(args) not in [1, 2]:
        parser.error('wrong number of arguments')
    if (len(args) == 1 and args[0] in ['add', 'remove']):
        parser.error('%r needs a collaborator name as second parameter\n'
                     % args[0])
    elif (len(args) == 1 and args[0] != 'list'):
        parser.error('unknown command %r. Try "list", "add" or "remove"\n'
                     % args[0])
    if (len(args) == 2 and args[0] not in ['add', 'remove']):
        parser.error('unknown command %r. Try "list", "add" or "remove"\n'
                     % args[0])
    if not options.login:
        parser.error('you must provide --login information\n')

    return options, args


def main():
    """This implements the actual program functionality"""

    options, args = parse_commandline()

    if not options.account:
        options.account = options.login

    github = github2.client.Github(username=options.login,
                                   api_token=options.apitoken,
                                   cache=options.cache)

    # PEP-308 conditional expressions are much better, but we're keeping Py2.4
    # compatibility elsewhere.
    logging.basicConfig(level=options.debug and logging.DEBUG or logging.WARN,
                        format="%(asctime)s - %(message)s",
                        datefmt="%Y-%m-%dT%H:%M:%S")
    if len(args) == 1:
        for repos in github.repos.list(options.account):
            fullreposname = github.project_for_user_repo(options.account,
                                                         repos.name)
            collabs = github.repos.list_collaborators(fullreposname)
            print_("%s: %s" % (repos.name, ' '.join(collabs)))
    elif len(args) == 2:
        command, collaborator = args
        for repos in github.repos.list(options.account):
            fullreposname = github.project_for_user_repo(options.account,
                                                         repos.name)
            if collaborator in github.repos.list_collaborators(fullreposname):
                if command == 'remove':
                    github.repos.remove_collaborator(repos.name, collaborator)
                    print_("removed %r from %r" % (collaborator, repos.name))
            else:
                if command == 'add':
                    github.repos.add_collaborator(repos.name, collaborator)
                    print_("added %r to %r" % (collaborator, repos.name))

    logging.shutdown()


if __name__ == '__main__':
    main()
