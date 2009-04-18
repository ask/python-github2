from github2.core import GithubCommand, BaseData

class Issue(BaseData):
    attributes = ("position", "number", "votes", "body", "title",
                  "created_at", "updated_at", "user", "state")
    date_attributes = ("created_at", "updated_at")


class Issues(GithubCommand):
    domain = "issues"

    def list(self, project, state="open"):
        """Get all issues for project' with state'.

        ``project`` is a string with the project owner username and repository
        name separated by ``/`` (e.g. ``ask/pygithub2``).
        ``state`` can be either ``open`` or ``closed``.
        """
        return self.get_values("list", project, state, filter="issues",
                               datatype=Issue)

    def show(self, project, number):
        """Get all the data for issue by issue-number."""
        return self.get_value("show", project, str(number),
                              filter="issue", datatype=Issue)

    def open(self, project, title, body):
        """Open up a new issue."""
        issue_data = {"title": title, "body": body}
        return self.get_value("open", project, post_data=issue_data,
                              filter="issue", datatype=Issue)

    def close(self, project, number):
        return self.get_value("close", project, str(number), filter="issue",
                              datatype=Issue)

    def add_label(self, project, number, label):
        return self.make_request("label/add", project, label, str(number),
                                 filter="labels")

    def remove_label(self, project, number, label):
        return self.make_request("label/remove", project, label, str(number),
                                 filter="labels")
