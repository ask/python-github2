from github2.request import GithubRequest
from github2.issues import Issues
from github2.repositories import Repositories
from github2.users import Users
from github2.commits import Commits

class Github(object):

    def __init__(self, username, api_token):
        self.request = GithubRequest(username=username, api_token=api_token)
        self.issues = Issues(self.request)
        self.users = Users(self.request)
        self.repos = Repositories(self.request)
        self.commits = Commits(self.request)

    def project_for_user_repo(self, user, repo):
        return "/".join([user, repo])

