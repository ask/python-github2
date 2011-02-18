from github2.core import BaseData, GithubCommand, Attribute
from github2.repositories import Repository
from github2.teams import Team
from github2.users import User
import urllib


class Organization(BaseData):
    id = Attribute("The team id")
    name = Attribute("The full name of the organization")
    blog = Attribute("The users blog")
    location = Attribute("Location of the user")
    gravatar_id = Attribute("Gravatar ID")
    login = Attribute("The login username")
    email = Attribute("The users e-mail address")

    def is_authenticated(self):
        return self.plan is not None

    def __repr__(self):
        return "<Organization: %s>" % (self.login)


class Organizations(GithubCommand):
    domain = "organizations"

    def show(self, organization):
        return self.get_value(organization, filter="organization",
                              datatype=Organization)

    def list(self):
        """Return a list of all of your organizations.
        """
        return self.get_values('', filter="organizations",
                               datatype=Organization)

    def repositories(self):
        """Return a list of all repositories in organizations you are
        a member of.
        """
        return self.get_values('repositories', filter="repositories",
                               datatype=Repository)

    def public_repositories(self, organization):
        """Return a list of public repositories in an organization.
        """
        return self.get_values(organization, 'public_repositories',
                               filter="repositories", datatype=Repository)

    def public_members(self, organization):
        """Return a list of public members in an organization.
        """
        return self.get_values(organization, 'public_members',
                               filter="users", datatype=User)

    def teams(self, organization):
        """Return a list of teams in an organization.
        """
        return self.get_values(organization, 'teams',
                               filter="teams", datatype=Team)
