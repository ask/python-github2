from github2.core import BaseData, GithubCommand, Attribute, DateAttribute

class Repository(BaseData):
    name = Attribute("Name of repository.")
    description = Attribute("Repository description.")
    forks = Attribute("Number of forks of this repository.")
    watchers = Attribute("Number of people watching this repository.")
    private = Attribute("If True, the repository is private.")
    url = Attribute("Canonical URL to this repository")
    fork = Attribute("If True, this is a fork of another repository.")
    owner = Attribute("Username of the user owning this repository.")
    homepage = Attribute("Homepage for this project.")
    open_issues = Attribute("List of open issues for this repository.")
    created_at = DateAttribute("Datetime the repository was created.")
    pushed_at = DateAttribute("Datetime of the last push to this repository")
    has_downloads = Attribute("If True, this repository has downloads.")
    has_wiki = Attribute("If True, this repository has a wiki.")
    has_issues = Attribute("If True, this repository has an issue tracker.")

    def _project(self):
        return self.owner + "/" + self.name
    project = property(_project)

    def __repr__(self):
        return "<Repository: %s>" % (self._project())


class Repositories(GithubCommand):
    domain = "repos"

    def search(self, query):
        return self.make_request("search", query, filter="repositories")

    def show(self, project):
        return self.get_value("show", project, filter="repository",
                              datatype=Repository)
    def pushable(self):
        """
        Return a list of repos you can push to that are not your own.
        """
        return self.get_values("pushable", filter="repositories", datatype=Repository)


    def list(self, for_user=None):
        """Return a list of all repositories for a user.

        If no user is given, repositoris for the currently logged in user are
        returned.
        """
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

    def delete(self, name):
        return self.make_request("delete", name)

    def set_private(self, repo_name):
        return self.make_request("set/private", repo_name)

    def set_public(self, repo_name):
        return self.make_request("set/public", repo_name)

    def list_collaborators(self, project):
        """Lists all the collaborators in a project (user/repro)."""
        return self.make_request("show", project, "collaborators",
                                 filter="collaborators")

    def add_collaborator(self, repo_name, username):
        """Adds an add_collaborator to a repro.

        Do not prefix repro_name with the user owning the repro like you
        do in list_collaborators()"""
        return self.make_request("collaborators", repo_name, "add", username)

    def remove_collaborator(self, repo_name, username):
        """Removes an add_collaborator from a repro.

        Do not prefix repro_name with the user owning the repro like you
        do in list_collaborators()"""
        return self.make_request("collaborators", repo_name, "remove",
                                 username, method="POST")

    def network(self, project):
        return self.make_request("show", project, "network", filter="network")

    def languages(self, project):
        return self.make_request("show", project, "languages",
                                 filter="languages")

    def tags(self, project):
        return self.make_request("show", project, "tags", filter="tags")

    def branches(self, project):
        return self.make_request("show", project, "branches",
                                 filter="branches")

    def watchers(self, project):
        return self.make_request("show", project, "watchers",
                                 filter="watchers")

    def watching(self, for_user=None):
        """Lists all the repos a user is watching."""
        for_user = for_user or self.request.username
        return self.get_values("watched", for_user, filter="repositories",
                               datatype=Repository)

    def list_contributors(self, project):
        """Lists all the contributors in a project (user/repo)."""
        return self.make_request("show", project, "contributors",
                           filter="contributors")
