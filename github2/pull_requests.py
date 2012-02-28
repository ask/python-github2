from github2.core import (BaseData, GithubCommand, Attribute, DateAttribute,
                          repr_string)


class PullRequest(BaseData):
    """Pull request encapsulation

    .. versionadded:: 0.5.0
    """
    state = Attribute("The pull request state")
    base = Attribute("The base repo")
    head = Attribute("The head of the pull request")
    issue_user = Attribute("The user who created the pull request.")
    user = Attribute("The owner of the repo.")
    title = Attribute("The text of the pull request title.")
    body = Attribute("The text of the body.")
    position = Attribute("Floating point position of the pull request.")
    number = Attribute("Number of this request.")
    votes = Attribute("Number of votes for this request.")
    comments = Attribute("Number of comments made on this request.")
    diff_url = Attribute("The URL to the unified diff.")
    patch_url = Attribute("The URL to the downloadable patch.")
    labels = Attribute("A list of labels attached to the pull request.")
    html_url = Attribute("The URL to the pull request.")
    issue_created_at = DateAttribute("The date the issue for this pull "
                                     "request was opened.", format='iso')
    issue_updated_at = DateAttribute("The date the issue for this pull "
                                     "request was last updated.", format='iso')
    created_at = DateAttribute("The date when this pull request was created.",
                               format='iso')
    updated_at = DateAttribute("The date when this pull request was last "
                               "updated.", format='iso')
    closed_at = DateAttribute("The date when this pull request was closed",
                              format='iso')
    discussion = Attribute("Discussion thread for the pull request.")
    mergeable = Attribute("Whether the pull request can be merge cleanly")

    def __repr__(self):
        return "<PullRequest: %s>" % repr_string(self.title)


class PullRequests(GithubCommand):
    """Operations on pull requests

    .. versionadded:: 0.5.0
    """
    domain = "pulls"

    def create(self, project, base, head, title=None, body=None, issue=None):
        """Create a new pull request

        Pull requests can be created from scratch, or attached to an existing
        issue.  If an ``issue`` parameter is supplied the pull request is
        attached to that issue, else a new pull request is created.

        :param str project: the Github project to send the pull request to
        :param str base: branch changes should be pulled into
        :param str head: branch of the changes to be pulled
        :param str title: title for pull request
        :param str body: optional body for pull request
        :param str issue: existing issue to attach pull request to
        """
        post_data = {"base": base, "head": head}
        if issue:
            post_data["issue"] = issue
        elif title:
            post_data["title"] = title
            if body:
                post_data["body"] = body
        else:
            raise TypeError("You must either specify a title for the "
                            "pull request or an issue number to which the "
                            "pull request should be attached.")
        pull_request_data = [("pull[%s]" % k, v) for k, v in post_data.items()]
        return self.get_value(project, post_data=dict(pull_request_data),
                              filter="pull", datatype=PullRequest)

    def show(self, project, number):
        """Show a single pull request

        :param str project: Github project
        :param int number: pull request number in the Github database
        """
        return self.get_value(project, str(number), filter="pull",
                              datatype=PullRequest)

    def list(self, project, state="open", page=1):
        """List all pull requests for a project

        :param str project: Github project
        :param str state: can be either ``open`` or ``closed``
        :param int page: optional page number
        """
        return self.get_values(project, state, filter="pulls",
                               datatype=PullRequest, page=page)
