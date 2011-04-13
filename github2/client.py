from github2.request import GithubRequest
from github2.issues import Issues
from github2.repositories import Repositories
from github2.users import Users
from github2.commits import Commits


class Github(object):

    def __init__(self, username=None, api_token=None, debug=False,
        requests_per_second=None, access_token=None, cache=None):
        """
        An interface to GitHub's API:
            http://develop.github.com/

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
        """

        self.debug = debug
        self.request = GithubRequest(username=username, api_token=api_token,
                                     debug=self.debug,
                                     requests_per_second=requests_per_second,
                                     access_token=access_token, cache=cache)
        self.issues = Issues(self.request)
        self.users = Users(self.request)
        self.repos = Repositories(self.request)
        self.commits = Commits(self.request)

    def project_for_user_repo(self, user, repo):
        """Return Github identifier for a user's repository

        :param str user: repository owner
        :param str repo: repository name
        """
        return "/".join([user, repo])

    def get_all_blobs(self, project, tree_sha):
        """Get a list of all blobs for a specific tree

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
