from github2.core import BaseData, GithubCommand, Attribute, requires_auth
from github2.repositories import Repository
from github2.users import User


class Team(BaseData):
    """.. versionadded:: 0.4.0"""
    id = Attribute("The team id")
    name = Attribute("Name of the team")
    permission = Attribute("Permissions of the team")

    def __repr__(self):
        return "<Team: %s>" % self.name


class Teams(GithubCommand):
    """.. versionadded:: 0.4.0"""
    domain = "teams"

    def show(self, team_id):
        """Get information on team_id

        :param int team_id: team to get information for
        """
        return self.get_value(str(team_id), filter="team", datatype=Team)

    def members(self, team_id):
        """Get list of all team members

        :param int team_id: team to get information for
        """
        return self.get_values(str(team_id), "members", filter="users",
                               datatype=User)

    @requires_auth
    def add_member(self, team_id, username):
        """Add a new member to a team

        :param int team_id: team to add new member to
        :param str username: GitHub username to add to team
        """
        return self.get_values(str(team_id), 'members', method='POST',
                               post_data={'name': username}, filter='users',
                               datatype=User)

    def repositories(self, team_id):
        """Get list of all team repositories

        :param int team_id: team to get information for
        """
        return self.get_values(str(team_id), "repositories",
                               filter="repositories", datatype=Repository)

    @requires_auth
    def add_project(self, team_id, project):
        """Add a project to a team

        :param int team_id: team to add repository to
        :param str project: GitHub project
        """
        if isinstance(project, Repository):
            project = project.project
        return self.get_values(str(team_id), "repositories", method="POST",
                               post_data={'name': project},
                               filter="repositories", datatype=Repository)

    @requires_auth
    def remove_project(self, team_id, project):
        """Remove a project to a team

        :param int team_id: team to remove project from
        :param str project: GitHub project
        """
        if isinstance(project, Repository):
            project = project.project
        return self.get_values(str(team_id), "repositories", method="DELETE",
                               post_data={'name': project},
                               filter="repositories", datatype=Repository)
