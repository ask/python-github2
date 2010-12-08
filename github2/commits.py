from github2.core import BaseData, GithubCommand, Attribute, DateAttribute


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
        return "<Commit: %s %s>" % (self.id, self.message[:64])


class Commits(GithubCommand):
    domain = "commits"

    def list(self, project, branch="master", file=None, page = None):
        post_data = {}
        if page is not None:
            post_data['page'] = page
        return self.get_values("list", project, branch, file,
                               filter="commits", datatype=Commit,
                               post_data=post_data)

    def show(self, project, sha):
        return self.get_value("show", project, sha,
                              filter="commit", datatype=Commit)


