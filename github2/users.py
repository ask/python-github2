from github2.core import BaseData, GithubCommand


class User(BaseData):
    attributes = ("id", "login", "name", "company", "location",
                  "email", "blog", "following_count", "followers_count",
                  "public_gist_count", "public_repo_count",
                  "total_private_repo_count", "collaborators",
                  "disk_usage", "owned_private_repo_count",
                  "private_gist_count", "plan")

    def is_authenticated(self):
        return self.plan is not None


class Users(GithubCommand):
    domain = "user"

    def search(self, query):
        return self.make_request("search", query, filter="users")

    def show(self, username):
        return self.get_value("show", username, filter="user", datatype=User)

    def followers(self, username):
        return self.make_request("show", username, "followers", filter="users")

    def following(self, username):
        return self.make_request("show", username, "following", filter="users")

    def follow(self, other_user):
        return self.make_request("follow", other_user)

    def unfollow(self, other_user):
        return self.make_request("unfollow", other_user)
