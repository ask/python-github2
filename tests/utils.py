# Copyright (C) 2011-2012 James Rowe <jnrowe@gmail.com>
#
# This file is part of python-github2, and is made available under the 3-clause
# BSD license.  See LICENSE for the full details.

import os
import sys
import unittest

from email import message_from_file

import httplib2

from mock import Mock

from github2.client import Github
from github2.request import charset_from_headers


if sys.version_info[0] == 2:
    bytes = lambda x, enc: x


ORIG_REQUEST_METHOD = httplib2.Http.request


def request_mock(uri, method='GET', body=None, headers=None,
              redirections=5, connection_type=None):
    """Http mock side effect that returns saved entries.

    Implementation tests should never span network boundaries.

    """

    file = os.path.join("tests/data", httplib2.safename(uri))
    if os.path.exists(file):
        response = message_from_file(open(file))
        headers = httplib2.Response(response)
        body = bytes(response.get_payload(), charset_from_headers(headers))
        return (headers, body)
    else:
        return (httplib2.Response({"status": "404"}),
                "Resource %r unavailable from test data store" % file)


class HttpMockTestCase(unittest.TestCase):
    def setUp(self):
        """Prepare test fixtures.

        `httplib2.Http` is patched to return cached entries via
        :class:`HttpMock`.

        :attr:`client` is an unauthenticated :obj:`Github` object for easy use
        in tests.

        """
        httplib2.Http.request = Mock(spec_set=httplib2.Http.request,
                                     side_effect=request_mock)
        self.client = Github()

    def tearDown(self):
        """Remove test fixtures.

        `httplib2.Http` is returned to its original state.

        """
        httplib2.Http.request = ORIG_REQUEST_METHOD


class HttpMockAuthenticatedTestCase(HttpMockTestCase):
    def setUp(self):
        """Prepare test fixtures.

        :see: :class:`HttpMockTestCase`

        :attr:`client` is an authenticated :obj:`Github` object for easy use
        in tests.

        """
        httplib2.Http.request = Mock(spec_set=httplib2.Http.request,
                                     side_effect=request_mock)
        self.client = Github(access_token='xxx')
