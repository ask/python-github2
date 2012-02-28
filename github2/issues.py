try:
    from urllib.parse import quote_plus  # For Python 3
except ImportError:
    from urllib import quote_plus  # NOQA

from github2.core import (GithubCommand, BaseData, Attribute, DateAttribute,
                          repr_string, requires_auth)


class Issue(BaseData):
    position = Attribute("The position of this issue in a list.")
    number = Attribute("The issue number (unique for project).")
    votes = Attribute("Number of votes for this issue.")
    body = Attribute("The full description for this issue.")
    title = Attribute("Issue title.")
    user = Attribute("The username of the user that created this issue.")
    state = Attribute("State of this issue. Can be ``open`` or ``closed``.")
    labels = Attribute("Labels associated with this issue.")
    created_at = DateAttribute("The date this issue was created.")
    closed_at = DateAttribute("The date this issue was closed.")
    updated_at = DateAttribute("The date when this issue was last updated.")
    diff_url = Attribute("URL for diff output associated with this issue.")
    patch_url = Attribute("URL for format-patch associated with this issue.")
    pull_request_url = Attribute("URL for the issue's related pull request.")

    def __repr__(self):
        return "<Issue: %s>" % repr_string(self.title)


class Comment(BaseData):
    created_at = DateAttribute("The date this comment was created.")
    updated_at = DateAttribute("The date when this comment was last updated.")
    body = Attribute("The full text of this comment.")
    id = Attribute("The comment id.")
    user = Attribute("The username of the user that created this comment.")

    def __repr__(self):
        return "<Comment: %s>" % repr_string(self.body)


class Issues(GithubCommand):
    domain = "issues"

    def search(self, project, term, state="open"):
        """Get all issues for project that match term with given state.

        .. versionadded:: 0.3.0

        :param str project: GitHub project
        :param str term: term to search issues for
        :param str state: can be either ``open`` or ``closed``.
        """
        return self.get_values("search", project, state, quote_plus(term),
                               filter="issues", datatype=Issue)

    def list(self, project, state="open"):
        """Get all issues for project with given state.

        :param str project: GitHub project
        :param str state: can be either ``open`` or ``closed``.
        """
        return self.get_values("list", project, state, filter="issues",
                               datatype=Issue)

    def list_by_label(self, project, label):
        """Get all issues for project with label.

        .. versionadded:: 0.3.0

        :param str project: GitHub project
        :param str label:  a string representing a label (e.g., ``bug``).
        """
        return self.get_values("list", project, "label", label,
                               filter="issues", datatype=Issue)

    def list_labels(self, project):
        """Get all labels for project.

        .. versionadded:: 0.3.0

        :param str project: GitHub project
        """
        return self.get_values("labels", project, filter="labels")

    def show(self, project, number):
        """Get all the data for issue by issue-number.

        :param str project: GitHub project
        :param int number: issue number in the Github database
        """
        return self.get_value("show", project, str(number),
                              filter="issue", datatype=Issue)

    @requires_auth
    def open(self, project, title, body):
        """Open up a new issue.

        :param str project: GitHub project
        :param str title: title for issue
        :param str body: body for issue
        """
        issue_data = {"title": title, "body": body}
        return self.get_value("open", project, post_data=issue_data,
                              filter="issue", datatype=Issue)

    @requires_auth
    def close(self, project, number):
        """Close an issue

        :param str project: GitHub project
        :param int number: issue number in the Github database
        """
        return self.get_value("close", project, str(number), filter="issue",
                              datatype=Issue, method="POST")

    @requires_auth
    def reopen(self, project, number):
        """Reopen a closed issue

        .. versionadded:: 0.3.0

        :param str project: GitHub project
        :param int number: issue number in the Github database
        """
        return self.get_value("reopen", project, str(number), filter="issue",
                              datatype=Issue, method="POST")

    @requires_auth
    def edit(self, project, number, title, body):
        """Edit an existing issue

        .. versionadded:: 0.3.0

        :param str project: GitHub project
        :param int number: issue number in the Github database
        :param str title: title for issue
        :param str body: body for issue
        """
        issue_data = {"title": title, "body": body}
        return self.get_value("edit", project, str(number),
                              post_data=issue_data, filter="issue",
                              datatype=Issue)

    @requires_auth
    def add_label(self, project, number, label):
        """Add a label to an issue

        :param str project: GitHub project
        :param int number: issue number in the Github database
        :param str label: label to attach to issue
        """
        return self.get_values("label/add", project, label, str(number),
                               filter="labels", method="POST")

    @requires_auth
    def remove_label(self, project, number, label):
        """Remove an existing label from an issue

        :param str project: GitHub project
        :param int number: issue number in the Github database
        :param str label: label to remove from issue
        """
        return self.get_values("label/remove", project, label, str(number),
                               filter="labels", method="POST")

    @requires_auth
    def comment(self, project, number, comment):
        """Comment on an issue.

        :param str project: GitHub project
        :param int number: issue number in the Github database
        :param str comment: comment to attach to issue
        """
        comment_data = {'comment': comment}
        return self.get_value("comment", project, str(number),
                              post_data=comment_data, filter='comment',
                              datatype=Comment)

    def comments(self, project, number):
        """View comments on an issue.

        :param str project: GitHub project
        :param int number: issue number in the Github database
        """
        return self.get_values("comments", project, str(number),
                               filter="comments", datatype=Comment)
