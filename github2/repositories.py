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
        """Get all repositories that match term.

        :param str query: term to search issues for
        """
        return self.make_request("search", query, filter="repositories")

    def show(self, project):
        """Get repository object for project.

        :param str project: GitHub project
        """
        return self.get_value("show", project, filter="repository",
                              datatype=Repository)
    def pushable(self):
        """Return a list of repos you can push to that are not your own."""
        return self.get_values("pushable", filter="repositories", datatype=Repository)


    def list(self, for_user=None):
        """Return a list of all repositories for a user.

        If no user is given, repositoris for the currently logged in user are
        returned.

        :param str for_user: optional Github user name to list repositories for
        """
        for_user = for_user or self.request.username
        return self.get_values("show", for_user, filter="repositories",
                               datatype=Repository)

    def watch(self, project):
        """Watch a project

        :param str project: GitHub project
        """
        return self.make_request("watch", project)

    def unwatch(self, project):
        """Unwatch a project

        :param str project: GitHub project
        """
        return self.make_request("unwatch", project)

    def fork(self, project):
        """Fork a project

        :param str project: GitHub project
        """
        return self.get_value("fork", project, filter="repository",
                              datatype=Repository)

    def create(self, project, description=None, homepage=None, public=True):
        """Create a repository

        :param str project: new project name
        :param str description: optional project description
        :param str homepage: optional project homepage
        :param bool public: whether to make a public project
        """
        repo_data = {"name": project, "description": description,
                     "homepage": homepage, "public": str(int(public))}
        return self.get_value("create", post_data=repo_data,
                              filter="repository", datatype=Repository)

    def delete(self, project):
        """Delete a repository

        :param str project: project name to delete
        """
        # Two-step delete mechanism.  We must echo the delete_token value back
        # to GitHub to actually delete a repository
        result = self.make_request("delete", project, method="POST")
        self.make_request("delete", project, post_data=result)

    def set_private(self, project):
        """Mark repository as private

        :param str project: project name to set as private
        """
        return self.make_request("set/private", project)

    def set_public(self, project):
        """Mark repository as public

        :param str project: project name to set as public
        """
        return self.make_request("set/public", project)

    def list_collaborators(self, project):
        """Lists all the collaborators in a project

        :param str project: GitHub project
        """
        return self.make_request("show", project, "collaborators",
                                 filter="collaborators")

    def add_collaborator(self, project, username):
        """Adds an add_collaborator to a repo

        Do not prefix repo_name with the user owning the repo like you do in
        list_collaborators()

        :param str project: Github project
        :param str username: Github user to add as collaborator
        """
        return self.make_request("collaborators", project, "add", username)

    def remove_collaborator(self, project, username):
        """Removes an add_collaborator from a repo

        Do not prefix repo_name with the user owning the repo like you do in
        list_collaborators()

        :param str project: Github project
        :param str username: Github user to add as collaborator
        """
        return self.make_request("collaborators", project, "remove",
                                 username, method="POST")

    def network(self, project):
        """Get network data for project

        :param str project: Github project
        """
        return self.make_request("show", project, "network", filter="network")

    def languages(self, project):
        """Get programming language data for project

        :param str project: Github project
        """
        return self.make_request("show", project, "languages",
                                 filter="languages")

    def tags(self, project):
        """Get tags for project

        :param str project: Github project
        """
        return self.make_request("show", project, "tags", filter="tags")

    def branches(self, project):
        """Get branch names for project

        :param str project: Github project
        """
        return self.make_request("show", project, "branches",
                                 filter="branches")

    def watchers(self, project):
        """Get list of watchers for project

        :param str project: Github project
        """
        return self.make_request("show", project, "watchers",
                                 filter="watchers")

    def watching(self, for_user=None):
        """Lists all the repos a user is watching

        :param str for_user: optional Github user name to list repositories for
        """
        for_user = for_user or self.request.username
        return self.get_values("watched", for_user, filter="repositories",
                               datatype=Repository)

    def list_contributors(self, project):
        """Lists all the contributors in a project

        :param str project: Github project
        """
        return self.make_request("show", project, "contributors",
                           filter="contributors")
