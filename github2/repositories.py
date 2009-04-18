from github2.core import BaseData, GithubCommand


class Repository(BaseData):
    attributes = ("description", "forks", "name", "watchers", "private",
                  "url", "fork", "owner", "homepage")


class Repositories(GithubCommand):
    domain = "repos"

    def search(self, query):
        return self.make_request("search", query, filter="repositories")

    def show(self, project):
        return self.get_value("show", project, filter="repository",
                              datatype=Repository)

    def list(self, for_user=None):
        for_user = for_user or self.request.username
        return self.get_values("show", for_user, filter="repositories",
                datatype=Repository)

    def watch(self, project):
        return self.make_request("watch", project)

    def unwatch(self, project):
        return self.make_request("unwatch", project)

    def fork(self, project):
        return self.get_value("fork", project, filter="repository",
                              datatype=Repository)

    def create(self, name, description=None, homepage=None, public=True):
        repo_data = {"name": name, "description": description,
                     "homepage": homepage, "public": str(int(public))}
        return self.get_value("create", post_data=repo_data,
                              filter="repository", datatype=Repository)

    def set_private(self, repo_name):
        return self.make_request("set/private", repo_name)

    def set_public(self, repo_name):
        return self.make_request("set/public", repo_name)

    def list_collaborators(self, project):
        return self.make_request("show", project, "collaborators",
                                 filter="collaborators")
                                 
    def add_collaborator(self, repo_name, username):
        return self.make_request("collaborators", repo_name, "add", username)

    def remove_collaborator(self, repo_name, username):
        return self.make_request("collaborators", repo_name, "remove",
                                 username)

    def network(self, project):
        return self.make_request("show", project, "network", filter="network")

    def tags(self, project):
        return self.make_request("show", project, "tags", filter="tags")

    def branches(self, project):
        return self.make_request("show", project, "branches",
                                 filter="branches")
