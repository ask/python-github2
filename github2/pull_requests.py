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
    comments = Attribute("Any comments made on this request.")
    diff_url = Attribute("The URL to the unified diff.")
    patch_url = Attribute("The URL to the downloadable patch.")
    labels = Attribute("A list of labels attached to the pull request.")
    html_url = Attribute("The URL to the pull request.")
    issue_created_at = DateAttribute("The date the issue for this pull request was opened.", format='commit')
    issue_updated_at = DateAttribute("The date the issue for this pull request was last updated.", format='commit')
    created_at = DateAttribute("The date when this pull request was created.", format='commit')
    updated_at = DateAttribute("The date when this pull request was last updated.", format='commit')

    def __repr__(self):
        return "<PullRequest: %s>" % self.html_url


class PullRequests(GithubCommand):
    domain = "pulls"

    def new(self, repo, base, head, title=None, body=None, issue=None):
        """ Create a new pull request """
        post_data = {"base": base, "head": head}
        if issue:
            post_data["issue"] = issue
        elif title and body:
            post_data["title"] = title
            post_data["body"] = body
        pull_request_data = [("pull[%s]" % k, v) for k, v in post_data.items()]
        return self.get_value(repo, post_data=dict(pull_request_data),
            filter="pull", datatype=PullRequest)

    def show(self, repo, number):
        """ Show a single pull request """
        return self.get_value(repo, str(number), filter="pull", datatype=PullRequest)

    def list(self, repo, state=None):
        """ List all pull requests for a repo """
        return self.get_values(repo, state, filter="pulls", datatype=PullRequest)
