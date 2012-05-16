# Copyright (C) 2011-2012 James Rowe <jnrowe@gmail.com>
#
# This file is part of python-github2, and is made available under the 3-clause
# BSD license.  See LICENSE for the full details.

import httplib2

from nose.tools import eq_

from github2.client import Github


def test_issue_50():
    """Erroneous init of ``Http`` with proxy setup.

    See https://github.com/ask/python-github2/pull/50
    """
    client = Github(proxy_host="my.proxy.com", proxy_port=9000)
    proxy_info = client.request._http.proxy_info
    eq_(type(proxy_info), httplib2.ProxyInfo)
    eq_(proxy_info.proxy_host, 'my.proxy.com')
    eq_(proxy_info.proxy_port, 9000)
