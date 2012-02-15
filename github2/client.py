from github2.request import GithubRequest
from github2.issues import Issues
from github2.repositories import Repositories
from github2.users import Users
from github2.commits import Commits
from github2.organizations import Organizations
from github2.teams import Teams
from github2.pull_requests import PullRequests


class Github(object):

    def __init__(self, username=None, api_token=None, requests_per_second=None,
                 access_token=None, cache=None, proxy_host=None,
                 proxy_port=8080, github_url=None):
        """
        An interface to GitHub's API:
            http://develop.github.com/

        .. versionadded:: 0.2.0
           The ``requests_per_second`` parameter
        .. versionadded:: 0.3.0
           The ``cache`` and ``access_token`` parameters
        .. versionadded:: 0.4.0
           The ``proxy_host`` and ``proxy_port`` parameters
        .. versionadded:: 0.7.0
           The ``github_url`` parameter

        :param str username: your own GitHub username.
        :param str api_token: can be found at https://github.com/account
            (while logged in as that user):
        :param str access_token: can be used when no ``username`` and/or
            ``api_token`` is used.  The ``access_token`` is the OAuth access
            token that is received after successful OAuth authentication.
        :param float requests_per_second: indicate the API rate limit you're
            operating under (1 per second per GitHub at the moment),
            or None to disable delays.  The default is to disable delays (for
            backwards compatibility).
        :param str cache: a directory for caching GitHub responses.
        :param str proxy_host: the hostname for the HTTP proxy, if needed.
        :param str proxy_port: the hostname for the HTTP proxy, if needed (will
            default to 8080 if a proxy_host is set and no port is set).
        :param str github_url: the hostname to connect to, for GitHub
            Enterprise support
        """

        self.request = GithubRequest(username=username, api_token=api_token,
                                     requests_per_second=requests_per_second,
                                     access_token=access_token, cache=cache,
                                     proxy_host=proxy_host,
                                     proxy_port=proxy_port,
                                     github_url=github_url)
        self.issues = Issues(self.request)
        self.users = Users(self.request)
        self.repos = Repositories(self.request)
        self.commits = Commits(self.request)
        self.organizations = Organizations(self.request)
        self.teams = Teams(self.request)
        self.pull_requests = PullRequests(self.request)

    def project_for_user_repo(self, user, repo):
        """Return Github identifier for a user's repository

        :param str user: repository owner
        :param str repo: repository name
        """
        return "/".join([user, repo])

    def get_all_blobs(self, project, tree_sha):
        """Get a list of all blobs for a specific tree

        .. versionadded:: 0.3.0

        :param str project: GitHub project
        :param str tree_sha: object ID of tree
        """
        blobs = self.request.get("blob/all", project, tree_sha)
        return blobs.get("blobs")

    def get_blob_info(self, project, tree_sha, path):
        """Get the blob for a file within a specific tree

        :param str project: GitHub project
        :param str tree_sha: object ID of tree
        :param str path: path within tree to fetch blob for
        """
        blob = self.request.get("blob/show", project, tree_sha, path)
        return blob.get("blob")

    def get_tree(self, project, tree_sha):
        """Get tree information for a specifc tree

        :param str project: GitHub project
        :param str tree_sha: object ID of tree
        """
        tree = self.request.get("tree/show", project, tree_sha)
        return tree.get("tree", [])

    def get_network_meta(self, project):
        """Get Github metadata associated with a project

        :param str project: GitHub project
        """
        return self.request.raw_request("/".join([self.request.github_url,
                                                  project,
                                                  "network_meta"]), {})

    def get_network_data(self, project, nethash, start=None, end=None):
        """Get chunk of Github network data

        :param str project: GitHub project
        :param str nethash: identifier provided by ``get_network_meta``
        :param int start: optional start point for data
        :param int stop: optional end point for data
        """
        data = {"nethash": nethash}
        if start:
            data["start"] = start
        if end:
            data["end"] = end

        return self.request.raw_request("/".join([self.request.github_url,
                                                  project,
                                                  "network_data_chunk"]),
                                                  data)
