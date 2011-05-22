from github2.core import BaseData, GithubCommand, DateAttribute, Attribute
import urllib


class User(BaseData):
    id = Attribute("The user id")
    login = Attribute("The login username")
    name = Attribute("The users full name")
    company = Attribute("Name of the company the user is associated with")
    location = Attribute("Location of the user")
    email = Attribute("The users e-mail address")
    blog = Attribute("The users blog")
    following_count = Attribute("Number of other users the user is following")
    followers_count = Attribute("Number of users following this user")
    public_gist_count = Attribute(
                            "Number of active public gists owned by the user")
    public_repo_count = Attribute(
                        "Number of active repositories owned by the user")
    total_private_repo_count = Attribute("Number of private repositories")
    collaborators = Attribute("Number of collaborators")
    disk_usage = Attribute("Currently used disk space")
    owned_private_repo_count = Attribute("Number of privately owned repos")
    private_gist_count = Attribute(
        "Number of private gists owned by the user")
    plan = Attribute("Current active github plan")
    created_at = DateAttribute("The date this user was registered",
                               format="user")

    def is_authenticated(self):
        """Test for user auththenication

        :return bool: ``True`` if user is authenticated"""
        return self.plan is not None

    def __repr__(self):
        return "<User: %s>" % (self.login)


class Users(GithubCommand):
    domain = "user"

    def search(self, query):
        """Search for users

        :param str query: term to search for
        """
        return self.get_values("search", urllib.quote_plus(query),
                               filter="users", datatype=User)

    def search_by_email(self, query):
        """Search for users by email address

        :param str query: email to search for
        """
        return self.get_value("email", query, filter="user", datatype=User)

    def show(self, username):
        """Get information on Github user

        if ``username`` is ``None`` or an empty string information for the
        currently authenticated user is returned.

        :param str username: Github user name
        """
        return self.get_value("show", username, filter="user", datatype=User)

    def followers(self, username):
        """Get list of Github user's followers

        :param str username: Github user name
        """
        return self.make_request("show", username, "followers", filter="users")

    def following(self, username):
        """Get list of users a Github user is following

        :param str username: Github user name
        """
        return self.make_request("show", username, "following", filter="users")

    def follow(self, other_user):
        """Follow a Github user

        :param str other_user: Github user name
        """
        return self.make_request("follow", other_user)

    def unfollow(self, other_user):
        """Unfollow a Github user

        :param str other_user: Github user name
        """
        return self.make_request("unfollow", other_user)
