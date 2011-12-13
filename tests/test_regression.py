import httplib2

from nose.tools import assert_equals

from github2.client import Github

import utils


def test_issue_50():
    """Erroneous init of ``Http`` with proxy setup

    See https://github.com/ask/python-github2/pull/50
    """
    utils.set_http_mock()

    client = Github(proxy_host="my.proxy.com", proxy_port=9000)
    setup_args = client.request._http.called_with
    assert_equals(type(setup_args['proxy_info']), httplib2.ProxyInfo)
    assert_equals(setup_args['proxy_info'].proxy_host, 'my.proxy.com')
    assert_equals(setup_args['proxy_info'].proxy_port, 9000)

    utils.unset_http_mock()
