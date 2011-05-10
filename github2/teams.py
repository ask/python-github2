from github2.core import BaseData, GithubCommand, Attribute, DateAttribute
from github2.repositories import Repository
from github2.users import User

class Team(BaseData):
    id = Attribute("The team id")
    name = Attribute("Name of the team")
    permission = Attribute("Permissions of the team")

    def __repr__(self):
        return "<Team: %s>" % self.name

class Teams(GithubCommand):
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

    def repositories(self, team_id):
        """Get list of all team members

        :param int team_id: team to get information for
        """
        return self.get_values(str(team_id), "repositories",
                               filter="repositories", datatype=Repository)

    def add_repository(self, team_id, repository):
        """Add a repository to a team

        :param int team_id: team to add repository to
        :param str repository: GitHub project
        """
        if isinstance(repository, Repository):
            repository = repository.project
        return self.make_request(str(team_id), "repositories", method="POST",
                                 post_data={'name': repository},
                                 filter="repositories", datatype=Repository)

    def remove_repository(self, team_id, repository):
        """Remove a repository to a team

        :param int team_id: team to remove project from
        :param str repository: GitHub project
        """
        if isinstance(repository, Repository):
            repository = repository.project
        return self.make_request(str(team_id), "repositories", method="DELETE",
                                 post_data={'name': repository},
                                 filter="repositories", datatype=Repository)
