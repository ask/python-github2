#!/usr/bin/python
from ConfigParser import SafeConfigParser
from github2.client import Github
from xml.etree import ElementTree as et
import argparse
import datetime
import getpass
import logging
import os.path
import sys
#logging.basicConfig(level=logging.DEBUG)

CLOSING_MESSAGE = """It is necessary to fix all email addresses
to correspond to bugzilla users.

Also, for importxml.pl to succeed you have to have switched on
 * move-enabled
 * moved-default-product
 * moved-default-component
"""

def _xml_indent(elem, level=0):
    i = "\n" + level * "  "
    if len(elem) != 0:
        if not (elem.text and elem.text.strip()):
            elem.text = i + "  "
        for e in elem:
            _xml_indent(e, level + 1)
        if not (e.tail and e.tail.strip()):
            e.tail = i
    else:
        if level and not(elem.tail and elem.tail.strip()):
            elem.tail = i


def load_default_configuration():
    config = {}
    conf_pars = SafeConfigParser({
        'user': getpass.getuser(),
        'api_key': None
    })
    conf_pars.read(os.path.expanduser("~/.githubrc"))
    config['git_user'] = conf_pars.get('github', 'user')
    config['git_api_token'] = conf_pars.get('github', 'api_key')

    desc = """Export issues from a Github Issue Tracker.
    The result is file which can be imported into Bugzilla with importxml.pl."""
    parser = argparse.ArgumentParser(description=desc)
    parser.add_argument("-u", "--github_user", metavar="USER",
      action="store", dest="github_user", default=None,
      help="GitHub user name")
    parser.add_argument("-A", "--github_api_key", metavar="API_KEY",
      action="store", dest="github_api_key", default=None,
      help="GitHub API key")
    parser.add_argument("-p", "--product", required=True,
      action="store", dest="bz_product", default=None,
      help="GitHub user name")
    parser.add_argument("-c", "--component", required=True,
      action="store", dest="bz_component", default=None,
      help="GitHub user name")
    parser.add_argument("repo", nargs="?",
            help="name of the github repo")
    options = parser.parse_args()

    if options.github_user:
        config['git_user'] = options.github_user
    if options.github_api_key:
        config['git_api_token'] = options.github_api_key

    config['repo'] = options.repo
    config['bz_product'] = options.bz_product
    config['bz_component'] = options.bz_component

    return config

def make_comment(body, who, when):
    """
    <!ELEMENT long_desc (who, bug_when, work_time?, thetext)>
    <!ATTLIST long_desc
          encoding (base64) #IMPLIED
          isprivate (0|1) #IMPLIED
    >
    """
    out = et.Element("long_desc", attrib={'isprivate': '0'})
    et.SubElement(out, "who").text = who
    et.SubElement(out, "bug_when").text = when
    et.SubElement(out, "thetext").text = body
    return out


def format_time(in_time):
    """
    in_time is datetime.datetime
    example: 2011-11-08 22:10:00 +0100
    """
    return in_time.strftime("%Y-%m-%d %H:%M:%S %z")


def file_issue(ghub, cnf, iss):
    me_user = '%s@github.com' % cnf['git_user']
    labels = ""
    if len(iss.labels) > 0:
        labels = str(iss.labels)
    created_at = format_time(iss.created_at)
    updated_at = format_time(iss.updated_at)
    if iss.closed_at and (iss.closed_at > iss.updated_at):
        closed_at = format_time(iss.closed_at)
    else:
        closed_at = updated_at
    status_conversion = {
        'open': 'NEW',
        'closed': 'RESOLVED'
    }

    issue_xml = et.Element("bug")
    et.SubElement(issue_xml, 'bug_id').text = str(iss.number)
    et.SubElement(issue_xml, 'creation_ts').text = created_at
    et.SubElement(issue_xml, 'short_desc').text = iss.title
    et.SubElement(issue_xml, 'delta_ts').text = closed_at
    et.SubElement(issue_xml, 'reporter_accessible').text = '1'
    et.SubElement(issue_xml, 'cclist_accessible').text = '1'
    et.SubElement(issue_xml, 'classification_id').text = '' # FIXME ????
    et.SubElement(issue_xml, 'classification').text = '' # FIXME ??? same as product in RH BZ
    et.SubElement(issue_xml, 'product').text = cnf['bz_product']
    et.SubElement(issue_xml, 'component').text = cnf['bz_component']
    et.SubElement(issue_xml, 'version').text = '0.0' # there are no versions in github ... BTW, BIG MISTAKE
    et.SubElement(issue_xml, 'rep_platform').text = ''
    et.SubElement(issue_xml, 'op_sys').text = ''
    et.SubElement(issue_xml, 'bug_status').text = status_conversion[iss.state]
    et.SubElement(issue_xml, 'status_whiteboard').text = labels
    et.SubElement(issue_xml, 'priority').text = ''
    et.SubElement(issue_xml, 'bug_severity').text = ''
    et.SubElement(issue_xml, 'votes').text = iss.votes
    et.SubElement(issue_xml, 'everconfirmed').text = ''
    et.SubElement(issue_xml, 'reporter').text = iss.user
    et.SubElement(issue_xml, 'assigned_to').text = me_user

    issue_xml.append(make_comment(iss.body, iss.user, created_at))
    for comment in ghub.issues.comments(cnf['repo'], iss.number):
        issue_xml.append(make_comment(comment.body, comment.user,
            format_time(comment.updated_at)))

    all_additional_items = ""
    for item in ("position", "diff_url", "patch_url", "pull_request_url"):
        all_additional_items += "%s:%s\n" % (item, getattr(iss, item))
    if len(all_additional_items.strip()) > 0:
        issue_xml.append(make_comment(all_additional_items,
            me_user, format(datetime.datetime.now())))

    return issue_xml


def main(conf):
    """
    Export your open github issues into a csv format for
    pivotal tracker import
    """

    github = Github(username=conf['git_user'],
        api_token=conf['git_api_token'])

    out_xml = et.Element("bugzilla", attrib={
            'version': '3.4.14',
            'urlbase': 'http://github.com',
            'maintainer': 'mcepl@redhat.com',
            'exporter': '%s@github.com' % conf['git_user'] # FIXME ^^^
        })

    for state in ('open', 'closed'):
        for issue in github.issues.list(conf['repo'], state=state):
            subelement_xml = file_issue(github, conf, issue)
            out_xml.append(subelement_xml)

    _xml_indent(out_xml)
    print et.tostring(out_xml, "utf-8")

    logging.info(CLOSING_MESSAGE)

if __name__ == '__main__':
    config = load_default_configuration()
    main(config)
