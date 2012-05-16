# Copyright (C) 2011-2012 James Rowe <jnrowe@gmail.com>
#                         Patryk Zawadzki <patrys@pld-linux.org>
#                         Rok Garbas <rok@garbas.si>
#
# This file is part of python-github2, and is made available under the 3-clause
# BSD license.  See LICENSE for the full details.

from github2.core import (BaseData, GithubCommand, Attribute, DateAttribute,
                          requires_auth)
from github2.repositories import Repository
from github2.teams import Team
from github2.users import User


class Organization(BaseData):

    """Organization container.

    .. versionadded:: 0.4.0

    """

    id = Attribute("The organization id.")
    name = Attribute("The full name of the organization.")
    blog = Attribute("The organization's blog.")
    location = Attribute("Location of the organization.")
    gravatar_id = Attribute("Gravatar ID.")
    login = Attribute("The login username.")
    email = Attribute("The organization's e-mail address.")
    company = Attribute("The organization's company name.")
    created_at = DateAttribute("The date the organization was created.",
                               format="commit")
    following_count = Attribute("Number of users the organization is "
                                "following.")
    followers_count = Attribute("Number of users following this organization.")
    public_gist_count = Attribute("Organization's number of active public "
                                  "gists.")
    public_repo_count = Attribute("Organization's number of active "
                                  "repositories.")
    permission = Attribute("Permissions within this organization.")
    plan = Attribute("GitHub plan for this organization.")

    def is_authenticated(self):
        return self.plan is not None

    def __repr__(self):
        return "<Organization: %s>" % self.login


class Organizations(GithubCommand):

    """GitHub API organizations functionality.

    .. versionadded:: 0.4.0

    """

    domain = "organizations"

    def show(self, organization):
        """Get information on organization.

        :param str organization: organization to show

        """
        return self.get_value(organization, filter="organization",
                              datatype=Organization)

    def list(self):
        """Get list of all of your organizations."""
        return self.get_values('', filter="organizations",
                               datatype=Organization)

    def repositories(self, organization=''):
        """Get list of all repositories in an organization.

        If organization is not given, or is empty, then this will list
        repositories for all organizations the authenticated user belongs to.

        :param: str organization: organization to list repositories for

        """
        return self.get_values(organization, 'repositories',
                               filter="repositories", datatype=Repository)

    def public_repositories(self, organization):
        """Get list of public repositories in an organization.

        :param str organization: organization to list public repositories for

        """
        return self.get_values(organization, 'public_repositories',
                               filter="repositories", datatype=Repository)

    def public_members(self, organization):
        """Get list of public members in an organization.

        :param str organization: organization to list members for

        """
        return self.get_values(organization, 'public_members', filter="users",
                               datatype=User)

    def teams(self, organization):
        """Get list of teams in an organization.

        :param str organization: organization to list teams for

        """
        return self.get_values(organization, 'teams', filter="teams",
                               datatype=Team)

    @requires_auth
    def add_team(self, organization, name, permission='pull', projects=None):
        """Add a team to an organization.

        :param str organization: organization to add team to
        :param str team: name of team to add
        :param str permission: permissions for team(push, pull or admin)
        :param list projects: optional GitHub projects for this team

        """
        team_data = {'team[name]': name, 'team[permission]': permission}
        if projects:
            team_data['team[repo_names][]'] = projects
        return self.get_value(organization, 'teams', post_data=team_data,
                              method='POST', filter='team', datatype=Team)
