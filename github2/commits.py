from github2.core import BaseData, GithubCommand


class Commit(BaseData):
    attributes = ("message", "parents", "url", "author", "id",
                  "committed_date", "authored_date", "tree", "committer",
                  "added", "removed", "modified")
    date_attributes = ("committed_date", "authored_date")


class Commits(GithubCommand):
    domain = "commits"

    def list(self, project, branch="master", file=None):
        return self.get_values("list", project, branch, file,
                               filter="commits", datatype=Commit)

    def show(self, project, sha):
        return self.get_value("show", project, sha,
                              filter="commit", datatype=Commit)


