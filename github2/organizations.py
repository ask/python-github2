from github2.core import BaseData, GithubCommand, Attribute, DateAttribute
from github2.users import User
from github2.teams import Team
from github2.repositories import Repository
import urllib


class Organization(BaseData):
    """ An organization """
    id = Attribute("The organization id")
    name = Attribute("The name for the organization.")
    disk_usage = Attribute("Currently used disk space")
    billing_email = Attribute("The billing email for the organization.")
    gravatar_id = Attribute("The id of the organization's gravatar image.")
    location = Attribute("Where this organization is located.")
    followers_count = Attribute("Number of users following this organization.")
    following_count = Attribute("Number of users this organization is following.")
    public_gist_count = Attribute("Number of active public gists owned by the organization.")
    public_repo_count = Attribute("Number of active public repos owned by the organization.")
    owned_private_repo_count = Attribute("Number of active private repos owned by the organization")
    total_private_repo_count = Attribute("Number of active private repos connected to the organization.")
    private_gist_count = Attribute("Number of active private gists owned by the organization.")
    plan = Attribute("The current active github plan for the organization.")
    collaborators = Attribute("Number of collaborators of the organization.")
    login = Attribute("The username for the organization.")

    def __repr__(self):
        return "<Organization: %s>" % self.login


class Organizations(GithubCommand):
    """ GithubCommand for getting an Organization """
    domain = "organizations"

    def show(self, org_name):
        """ returns an organization """
        return self.get_value(org_name, filter="organization",
            datatype=Organization)

    def teams(self, org_name):
        """ Returns the teams owned by an organization """
        return self.get_values(org_name, "teams", filter='teams', datatype=Team)

    def repositories(self, org_name):
        """ Returns the list of repos owned by an org """
        return self.get_values(org_name, "repositories", filter="repositories",
            datatype=Repository)

    def public_members(self, org_name):
        """ returns the list of public members """
        return self.get_values(org_name, "public_members", filter="users",
            datatype=User)
