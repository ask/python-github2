from github2.core import (BaseData, GithubCommand, Attribute, DateAttribute,
                          repr_string)


class Commit(BaseData):
    message = Attribute("Commit message.")
    parents = Attribute("List of parents for this commit.")
    url = Attribute("Canonical URL for this commit.")
    author = Attribute("Author metadata (dict with name/email.)")
    id = Attribute("Commit ID.")
    committed_date = DateAttribute("Date committed.", format="commit")
    authored_date = DateAttribute("Date authored.", format="commit")
    tree = Attribute("Tree SHA for this commit.")
    committer = Attribute("Comitter metadata (dict with name/email.)")

    added = Attribute("(If present) Datastructure representing what's been "
                      "added since last commit.")
    removed = Attribute("(if present) Datastructure representing what's been "
                        "removed since last commit.")
    modified = Attribute("(If present) Datastructure representing what's "
                         "been modified since last commit.")

    def __repr__(self):
        return "<Commit: %s %s>" % (self.id[:8], repr_string(self.message))


class Commits(GithubCommand):
    domain = "commits"

    def list(self, project, branch="master", file=None, page=1):
        """List commits on a project

        .. warning::
           Not all projects use ``master`` as their default branch, you can
           check the value of the ``Repo(project).master_branch`` attribute to
           determine the default branch of a given repository.

        :param str project: project name
        :param str branch: branch name, or ``master`` if not given
        :param str file: optional file filter
        :param int page: optional page number
        """
        return self.get_values("list", project, branch, file, filter="commits",
                               datatype=Commit, page=page)

    def show(self, project, sha):
        """Get a specific commit

        :param str project: project name
        :param str sha: commit id
        """
        return self.get_value("show", project, sha,
                              filter="commit", datatype=Commit)
