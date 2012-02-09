from github2.core import (BaseData, GithubCommand, Attribute, DateAttribute,
                          requires_auth)

from github2.users import User


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
    master_branch = Attribute("Default branch, if set.")
    integration_branch = Attribute("Integration branch, if set.")
    open_issues = Attribute("List of open issues for this repository.")
    created_at = DateAttribute("Datetime the repository was created.")
    pushed_at = DateAttribute("Datetime of the last push to this repository")
    has_downloads = Attribute("If True, this repository has downloads.")
    has_wiki = Attribute("If True, this repository has a wiki.")
    has_issues = Attribute("If True, this repository has an issue tracker.")
    language = Attribute("Primary language for the repository.")
    parent = Attribute("The parent project of this fork.")
    source = Attribute("The root project of this fork")

    def _project(self):
        return self.owner + "/" + self.name
    project = property(_project)

    def __repr__(self):
        return "<Repository: %s>" % self.project


class Repositories(GithubCommand):
    domain = "repos"

    def search(self, query):
        """Get all repositories that match term.

        .. warning:
           Returns at most 100 repositories

        :param str query: term to search issues for
        """
        return self.get_values("search", query, filter="repositories",
                               datatype=Repository)

    def show(self, project):
        """Get repository object for project.

        :param str project: GitHub project
        """
        return self.get_value("show", project, filter="repository",
                              datatype=Repository)

    @requires_auth
    def pushable(self):
        """Return a list of repos you can push to that are not your own.

        .. versionadded:: 0.3.0
        """
        return self.get_values("pushable", filter="repositories",
                               datatype=Repository)

    def list(self, user=None, page=1):
        """Return a list of all repositories for a user.

        .. deprecated: 0.4.0
           Previous releases would attempt to display repositories for the
           logged-in user when ``user`` wasn't supplied.  This functionality is
           brittle and will be removed in a future release!

        :param str user: Github user name to list repositories for
        :param int page: optional page number
        """
        user = user or self.request.username
        return self.get_values("show", user, filter="repositories",
                               datatype=Repository, page=page)

    @requires_auth
    def watch(self, project):
        """Watch a project

        :param str project: GitHub project
        """
        return self.get_value("watch", project, filter='repository',
                              datatype=Repository)

    @requires_auth
    def unwatch(self, project):
        """Unwatch a project

        :param str project: GitHub project
        """
        return self.get_value("unwatch", project, filter='repository',
                              datatype=Repository)

    @requires_auth
    def fork(self, project):
        """Fork a project

        :param str project: GitHub project
        """
        return self.get_value("fork", project, filter="repository",
                              datatype=Repository)

    @requires_auth
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

    @requires_auth
    def delete(self, project):
        """Delete a repository

        :param str project: project name to delete
        """
        # Two-step delete mechanism.  We must echo the delete_token value back
        # to GitHub to actually delete a repository
        result = self.make_request("delete", project, method="POST")
        self.make_request("delete", project, post_data=result)

    @requires_auth
    def set_private(self, project):
        """Mark repository as private

        :param str project: project name to set as private
        """
        return self.make_request("set/private", project)

    @requires_auth
    def set_public(self, project):
        """Mark repository as public

        :param str project: project name to set as public
        """
        return self.make_request("set/public", project)

    def list_collaborators(self, project):
        """Lists all the collaborators in a project

        :param str project: GitHub project
        """
        return self.get_values("show", project, "collaborators",
                               filter="collaborators")

    @requires_auth
    def add_collaborator(self, project, username):
        """Adds an add_collaborator to a repo

        :param str project: Github project
        :param str username: Github user to add as collaborator
        """
        return self.make_request("collaborators", project, "add", username,
                                 method="POST")

    @requires_auth
    def remove_collaborator(self, project, username):
        """Removes an add_collaborator from a repo

        :param str project: Github project
        :param str username: Github user to add as collaborator
        """
        return self.make_request("collaborators", project, "remove",
                                 username, method="POST")

    def network(self, project):
        """Get network data for project

        :param str project: Github project
        """
        return self.get_values("show", project, "network", filter="network",
                               datatype=Repository)

    def languages(self, project):
        """Get programming language data for project

        :param str project: Github project
        """
        return self.get_values("show", project, "languages",
                               filter="languages")

    def tags(self, project):
        """Get tags for project

        :param str project: Github project
        """
        return self.get_values("show", project, "tags", filter="tags")

    def branches(self, project):
        """Get branch names for project

        :param str project: Github project
        """
        return self.get_values("show", project, "branches", filter="branches")

    def watchers(self, project):
        """Get list of watchers for project

        :param str project: Github project
        """
        return self.get_values("show", project, "watchers", filter="watchers")

    def watching(self, for_user=None, page=None):
        """Lists all the repos a user is watching

        :param str for_user: optional Github user name to list repositories for
        :param int page: optional page number
        """
        for_user = for_user or self.request.username
        return self.get_values("watched", for_user, filter="repositories",
                               datatype=Repository, page=page)

    def list_contributors(self, project):
        """Lists all the contributors in a project

        :param str project: Github project
        """
        return self.get_values("show", project, "contributors",
                               filter="contributors", datatype=User)
