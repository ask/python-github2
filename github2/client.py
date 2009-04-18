from github2.request import GithubRequest

class GithubData(object):
    def __init__(self, **kwargs):
        for attr_name in self.attributes:
            if attr_name in kwargs:
                setattr(self, attr_name, kwargs[attr_name])
            else:
                setattr(self, attr_name, None)

    def to_dict(self):
        dict_ = {}
        for attr_name in self.attributes:
            attr_value = getattr(self, attr_name, None)
            if attr_value is not None:
                dict_[attr_name] = attr_value
        return dict_


class Issue(GithubData):
    attributes = ("position", "number", "votes", "body", "title",
                  "created_at", "updated_at", "user", "state")

class User(GithubData):
    attributes = ("id", "login", "name", "company", "location", "email",
                  "blog", "following_count", "followers_count",
                  "public_gist_count", "public_repo_count",
                  "total_private_repo_count", "collaborators", "disk_usage",
                  "owned_private_repo_count", "private_gist_count",
                  "plan")

    def is_authenticated(self):
        return self.plan is not None


class GithubCommand(object):

    def __init__(self, request):
        self.request = request

    def make_request(self, command, *args, **kwargs):
        filter = kwargs.get("filter")
        post_data = kwargs.get("post_data")
        if post_data:
            response = self.request.post(self.domain, command, *args,
                                         **post_data)
        else:
            response = self.request.get(self.domain, command, *args)
        if filter:
            return response[filter]
        return response


class Users(GithubCommand):
    domain = "user"

    def search(self, query):
        return self.make_request("search", query, filter="users")

    def show(self, username):
        user_data = self.make_request("show", username, filter="user")
        return User(**user_data)

    def followers(self, username):
        return self.make_request("show", username, "followers")

    def following(self, username):
        return self.make_request("show", username, "following")

    def follow(self, other_user):
        return self.make_request("follow", other_user)

    def unfollow(self, other_user):
        return self.make_request("unfollow", other_user)

class Issues(GithubCommand):
    domain = "issues"

    def list(self, project, state="open"):
        """Get all issues for project' with state'.

        ``project`` is a string with the project owner username and repository
        name separated by ``/`` (e.g. ``ask/pygithub2``).
        ``state`` can be either ``open`` or ``closed``.
        """
        return [Issue(**issue)
                    for issue in self.make_request("list", project, state,
                                                   filter="issues")]

    def show(self, project, number):
        """Get all the data for issue by issue-number."""
        issue_data = self.make_request("show", project, str(number),
                                       filter="issue")
        return Issue(**issue_data)

    def open(self, project, title, body):
        """Open up a new issue."""
        issue_data = {"title": title, "body": body}
        r = self.make_request("open", project, post_data=issue_data,
                              filter="issue")
        return Issue(**r)

    def close(self, project, number):
        issue_data = self.make_request("close", project, str(number),
                                        filter="issue")
        return Issue(**issue_data)

    def add_label(self, project, number, label):
        return self.make_request("label/add", project, label, str(number),
                                 filter="labels")

    def remove_label(self, project, number, label):
        return self.make_request("label/remove", project, label, str(number),
                                 filter="labels")
class Github(object):

    def __init__(self, username, api_token):
        self.request = GithubRequest(username=username, api_token=api_token)
        self.issues = Issues(self.request)
        self.users = Users(self.request)

    def project_for_user_repo(self, user, repo):
        return "/".join([user, repo])

