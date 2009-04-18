from github2.request import GithubRequest


class BaseDataType(type):

    def __new__(cls, name, bases, attrs):
        super_new = super(BaseDataType, cls).__new__

        attributes = attrs.pop("attributes", tuple())
        attrs.update(dict([(attr_name, None)
                        for attr_name in attributes]))

        def constructor(self, **kwargs):
            for attr_name, attr_value in kwargs.items():
                if attr_name not in attributes:
                    raise TypeError("%s.__init__() doesn't support the "
                                    "%s argument." % ( cls_name, attr_name))
                setattr(self, attr_name, attr_value)
        attrs["__init__"] = constructor

        def to_dict(self):
            dict_ = {}
            for attr_name in self.attributes:
                attr_value = getattr(self, attr_name, None)
                if attr_value is not None:
                    dict_[attr_name] = attr_value
            return dict_
        attrs["to_dict"] = to_dict

        return super_new(cls, name, bases, attrs)


class BaseData(object):
    __metaclass__ = BaseDataType


class Issue(BaseData):
    attributes = ("position", "number", "votes", "body", "title",
                  "created_at", "updated_at", "user", "state")


class User(BaseData):
    attributes = ("id", "login", "name", "company", "location",
                  "email", "blog", "following_count", "followers_count",
                  "public_gist_count", "public_repo_count",
                  "total_private_repo_count", "collaborators",
                  "disk_usage", "owned_private_repo_count",
                  "private_gist_count", "plan")

    def is_authenticated(self):
        return self.plan is not None


class Repository(BaseData):
    attributes = ("description", "forks", "name", "watchers", "private",
                  "url", "fork", "owner", "homepage")


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
        return self.make_request("show", username, "followers", filter="users")

    def following(self, username):
        return self.make_request("show", username, "following", filter="users")

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

class Repositories(GithubCommand):
    domain = "repos"

    def search(self, query):
        return self.make_request("search", query, filter="repositories")

    def show(self, project):
        repo_data = self.make_request("show", project, filter="repository")
        return Repository(**repo_data)

    def list(self, for_user=None):
        for_user = for_user or self.request.username
        return [Repository(**repo_data)
                    for repo_data in self.make_request("show", for_user,
                                                       filter="repositories")]

    def watch(self, project):
        return self.make_request("watch", project)

    def unwatch(self, project):
        return self.make_request("unwatch", project)

    def fork(self, project):
        new_repo_data = self.make_request("fork", project,
                                          filter="repository")
        return Repository(**new_repo_data)

    def create(self, name, description=None, homepage=None, public=True):
        repo_data = {"name": name, "description": description,
                     "homepage": homepage, "public": str(int(public))}
        new_repo_data = self.make_request("create", post_data=repo_data,
                                          filter="repository")
        return Repository(**new_repo_data)

    def set_private(self, repo_name):
        return self.make_request("set/private", repo_name)

    def set_public(self, repo_name):
        return self.make_request("set/public", repo_name)

    def list_collaborators(self, project):
        return self.make_request("show", project, "collaborators",
                                 filter="collaborators")
                                 
    def add_collaborator(self, repo_name, username):
        return self.make_request("collaborators", repo_name, "add", username)

    def remove_collaborator(self, repo_name, username):
        return self.make_request("collaborators", repo_name, "remove",
                                 username)

    def network(self, project):
        return self.make_request("show", project, "network", filter="network")

    def tags(self, project):
        return self.make_request("show", project, "tags", filter="tags")

    def branches(self, project):
        return self.make_request("show", project, "branches",
                                 filter="branches")


class Github(object):

    def __init__(self, username, api_token):
        self.request = GithubRequest(username=username, api_token=api_token)
        self.issues = Issues(self.request)
        self.users = Users(self.request)
        self.repos = Repositories(self.request)

    def project_for_user_repo(self, user, repo):
        return "/".join([user, repo])

