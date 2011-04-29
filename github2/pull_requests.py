from github2.core import BaseData, GithubCommand, Attribute, DateAttribute

class PullRequest(BaseData):
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
    issue_created_at = DateAttribute("The date the issue for this pull request was opened.",
                                     format='iso')
    issue_updated_at = DateAttribute("The date the issue for this pull request was last updated.",
                                     format='iso')
    created_at = DateAttribute("The date when this pull request was created.",
                               format='iso')
    updated_at = DateAttribute("The date when this pull request was last updated.",
                               format='iso')
    closed_at = DateAttribute("The date when this pull request was closed",
                              format='iso')
    discussion = Attribute("Discussion thread for the pull request.")

    def __repr__(self):
        return "<PullRequest: %s>" % self.html_url


class PullRequests(GithubCommand):
    domain = "pulls"

    def new(self, project, base, head, title=None, body=None, issue=None):
        """ Create a new pull request """
        post_data = {"base": base, "head": head}
        if issue:
            post_data["issue"] = issue
        elif title:
            post_data["title"] = title
            if body:
                post_data["body"] = body
        pull_request_data = [("pull[%s]" % k, v) for k, v in post_data.items()]
        return self.get_value(project, post_data=dict(pull_request_data),
            filter="pull", datatype=PullRequest)

    def show(self, project, number):
        """ Show a single pull request """
        return self.get_value(project, str(number), filter="pull",
                              datatype=PullRequest)

    def list(self, project, state="open"):
        """ List all pull requests for a project """

        return self.get_values(project, state, filter="pulls",
                               datatype=PullRequest)
