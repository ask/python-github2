# Copyright (C) 2009-2012 Adam Vandenberg <flangy@gmail.com>
#                         Asheesh Laroia <asheesh@openhatch.org>
#                         Ask Solem <askh@modwheel.net>
#                         Chris Vale <crispywalrus@gmail.com>
#                         Daniel Greenfeld <pydanny@gmail.com>
#                         Evan Broder <broder@mit.edu>
#                         James Rowe <jnrowe@gmail.com>
#                         Jeremy Dunck <jdunck@gmail.com>
#                         Josh Weinberg <daemoncollector@gmail.com>
#                         Mark Paschal <markpasc@markpasc.org>
#                         Maximillian Dornseif <m.dornseif@hudora.de>
#                         Michael Basnight <mbasnight@gmail.com>
#                         Patryk Zawadzki <patrys@pld-linux.org>
#                         Rick Harris <rick.harris@rackspace.com>
#                         Sameer Al-Sakran <sameer@whitelabellabs.com>
#                         Vincent Driessen <vincent@datafox.nl>
#                         modocache <modocache@gmail.com>
#
# This file is part of python-github2, and is made available under the 3-clause
# BSD license.  See LICENSE for the full details.

import datetime
import logging
import re
import sys
import time

try:
    # For Python 3
    from http.client import responses
except ImportError:  # For Python 2.5-2.7
    try:
        from httplib import responses  # NOQA
    except ImportError:  # For Python 2.4
        from BaseHTTPServer import BaseHTTPRequestHandler as _BHRH
        responses = dict([(k, v[0]) for k, v in _BHRH.responses.items()])  # NOQA
try:
    import json as simplejson  # For Python 2.6+
except ImportError:
    import simplejson  # NOQA
from os import (getenv, path)
try:
    # For Python 3
    from urllib.parse import (parse_qs, quote, urlencode, urlsplit, urlunsplit)
except ImportError:
    from urlparse import (urlsplit, urlunsplit)  # NOQA
    try:
        from urlparse import parse_qs  # NOQA
    except ImportError:
        from cgi import parse_qs  # NOQA
    from urllib import urlencode, quote  # NOQA

import httplib2


#: Hostname for API access
DEFAULT_GITHUB_URL = "https://github.com"

#: Logger for requests module
LOGGER = logging.getLogger('github2.request')

# Fetch actual path for httplib2's default cert bundle, for distributions that
# symlink their system certs
_HTTPLIB2_BUNDLE = path.realpath(path.dirname(httplib2.CA_CERTS))
#: Whether github2 is using the system's certificates for SSL connections
SYSTEM_CERTS = not _HTTPLIB2_BUNDLE.startswith(path.dirname(httplib2.__file__))
CA_CERTS = None
#: Whether github2 is using the cert's from the file given in $CURL_CA_BUNDLE
CURL_CERTS = False
if not SYSTEM_CERTS and sys.platform.startswith('linux'):
    for cert_file in ['/etc/ssl/certs/ca-certificates.crt',
                      '/etc/pki/tls/certs/ca-bundle.crt']:
        if path.exists(cert_file):
            CA_CERTS = cert_file
            SYSTEM_CERTS = True
            break
elif not SYSTEM_CERTS and sys.platform.startswith('freebsd'):
    if path.exists('/usr/local/share/certs/ca-root-nss.crt'):
        CA_CERTS = '/usr/local/share/certs/ca-root-nss.crt'
        SYSTEM_CERTS = True
elif path.exists(getenv('CURL_CA_BUNDLE', '')):
    CA_CERTS = getenv('CURL_CA_BUNDLE')
    CURL_CERTS = True
if not SYSTEM_CERTS and not CURL_CERTS:
    CA_CERTS = path.join(path.dirname(path.abspath(__file__)),
                         "DigiCert_High_Assurance_EV_Root_CA.crt")


# Common missing entries from the HTTP status code dict, basically anything
# GitHub reports that isn't basic HTTP/1.1.
responses[422] = 'Unprocessable Entity'


def charset_from_headers(headers):
    """Parse charset from headers.

    :param httplib2.Response headers: Request headers
    :return: Defined encoding, or default to ASCII

    """
    match = re.search("charset=([^ ;]+)", headers.get('content-type', ""))
    if match:
        charset = match.groups()[0]
    else:
        charset = "ascii"
    return charset


class GithubError(Exception):

    """An error occurred when making a request to the GitHub API."""


class HttpError(RuntimeError):

    """A HTTP error occured when making a request to the GitHub API."""

    def __init__(self, message, content, code):
        """Create a HttpError exception.

        :param str message: Exception string
        :param str content: Full content of HTTP request
        :param int code: HTTP status code

        """
        self.args = (message, content, code)
        self.message = message
        self.content = content
        self.code = code
        if code in responses:
            self.code_reason = responses[code]
        else:
            self.code_reason = "<unknown status code>"
            LOGGER.warning('Unknown HTTP status %r, please file an issue',
                           code)


class GithubRequest(object):

    """Make an API request.

    :see: :class:`github2.client.Github`

    """

    url_format = "%(github_url)s/api/%(api_version)s/%(api_format)s"
    api_version = "v2"
    api_format = "json"
    GithubError = GithubError

    def __init__(self, username=None, api_token=None, url_prefix=None,
                 requests_per_second=None, access_token=None,
                 cache=None, proxy_host=None, proxy_port=None,
                 github_url=None):
        self.username = username
        self.api_token = api_token
        self.access_token = access_token
        self.url_prefix = url_prefix
        if github_url is None:
            self.github_url = DEFAULT_GITHUB_URL
        else:
            self.github_url = github_url
        if requests_per_second is None:
            self.delay = 0
        else:
            self.delay = 1.0 / requests_per_second
        self.last_request = datetime.datetime(1900, 1, 1)
        if not self.url_prefix:
            self.url_prefix = self.url_format % {
                "github_url": self.github_url,
                "api_version": self.api_version,
                "api_format": self.api_format,
            }
        if proxy_host is None:
            self._http = httplib2.Http(cache=cache)
        else:
            proxy_info = httplib2.ProxyInfo(httplib2.socks.PROXY_TYPE_HTTP,
                                            proxy_host, proxy_port)
            self._http = httplib2.Http(proxy_info=proxy_info, cache=cache)
        self._http.ca_certs = CA_CERTS
        if SYSTEM_CERTS:
            LOGGER.info('Using system certificates in %r', CA_CERTS)
        elif CURL_CERTS:
            LOGGER.info("Using cURL's certificates in %r", CA_CERTS)
        else:
            LOGGER.warning('Using bundled certificate for HTTPS connections')

    def encode_authentication_data(self, extra_post_data):
        post_data = []
        if self.access_token:
            post_data.append(("access_token", self.access_token))
        elif self.username and self.api_token:
            post_data.append(("login", self.username))
            post_data.append(("token", self.api_token))
        for key, value in extra_post_data.items():
            if isinstance(value, list):
                for elem in value:
                    post_data.append((key, elem))
            else:
                post_data.append((key, value))
        return urlencode(post_data)

    def get(self, *path_components):
        path_components = filter(None, path_components)
        return self.make_request("/".join(path_components))

    def post(self, *path_components, **extra_post_data):
        path_components = filter(None, path_components)
        return self.make_request("/".join(path_components), extra_post_data,
            method="POST")

    def put(self, *path_components, **extra_post_data):
        path_components = filter(None, path_components)
        return self.make_request("/".join(path_components), extra_post_data,
            method="PUT")

    def delete(self, *path_components, **extra_post_data):
        path_components = filter(None, path_components)
        return self.make_request("/".join(path_components), extra_post_data,
            method="DELETE")

    def make_request(self, path, extra_post_data=None, method="GET"):
        if self.delay:
            since_last = (datetime.datetime.utcnow() - self.last_request)
            if since_last.days == 0 and since_last.seconds < self.delay:
                duration = self.delay - since_last.seconds
                LOGGER.warning("delaying API call %g second(s)", duration)
                time.sleep(duration)

        extra_post_data = extra_post_data or {}
        url = "/".join([self.url_prefix, quote(path)])
        result = self.raw_request(url, extra_post_data, method=method)

        if self.delay:
            self.last_request = datetime.datetime.utcnow()
        return result

    def raw_request(self, url, extra_post_data, method="GET"):
        scheme, netloc, path, query, fragment = urlsplit(url)
        post_data = None
        headers = self.http_headers
        method = method.upper()
        if extra_post_data or method == "POST":
            post_data = self.encode_authentication_data(extra_post_data)
            headers["Content-Length"] = str(len(post_data))
        else:
            query = self.encode_authentication_data(parse_qs(query))
        url = urlunsplit((scheme, netloc, path, query, fragment))
        response, content = self._http.request(url, method, post_data, headers)
        if LOGGER.isEnabledFor(logging.DEBUG):
            logging.debug("URL: %r POST_DATA: %r RESPONSE_TEXT: %r", url,
                          post_data, content)
        if response.status >= 400:
            raise HttpError("Unexpected response from github.com %d: %r"
                            % (response.status, content), content,
                            response.status)
        json = simplejson.loads(content.decode(charset_from_headers(response)))
        if json.get("error"):
            raise self.GithubError(json["error"][0]["error"])

        return json

    @property
    def http_headers(self):
        return {
            "User-Agent": "pygithub2 v1",
            "Accept": "application/json",
        }
