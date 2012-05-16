# -*- coding: utf-8 -*-
# Copyright (C) 2009-2012 Ask Solem <askh@modwheel.net>
#                         James Rowe <jnrowe@gmail.com>
#                         Sameer Al-Sakran <sameer@whitelabellabs.com>
#                         Stéphane Angel <s.angel@twidi.com>
#
# This file is part of python-github2, and is made available under the 3-clause
# BSD license.  See LICENSE for the full details.

try:
    from urllib.parse import quote_plus  # For Python 3
except ImportError:
    from urllib import quote_plus  # NOQA

from github2.core import (BaseData, GithubCommand, DateAttribute, Attribute,
                          enhanced_by_auth, requires_auth)


class Key(BaseData):

    """SSH key container."""

    id = Attribute('The key id')
    key = Attribute('The SSH key data')
    title = Attribute('The title for the SSH key')

    def __repr__(self):
        return "<Key: %s>" % self.id


class User(BaseData):

    """GitHub user container."""

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
        """Test for user authentication.

        :return bool: ``True`` if user is authenticated

       """
        return self.plan is not None

    def __repr__(self):
        return "<User: %s>" % self.login


class Users(GithubCommand):

    """GitHub API user functionality."""

    domain = "user"

    def search(self, query):
        """Search for users.

        .. warning:
           Returns at most 100 users

        :param str query: term to search for

        """
        return self.get_values("search", quote_plus(query), filter="users",
                               datatype=User)

    def search_by_email(self, query):
        """Search for users by email address.

        :param str query: email to search for

        """
        return self.get_value("email", query, filter="user", datatype=User)

    @enhanced_by_auth
    def show(self, username):
        """Get information on GitHub user.

        if ``username`` is ``None`` or an empty string information for the
        currently authenticated user is returned.


        """
        return self.get_value("show", username, filter="user", datatype=User)

    def followers(self, username):
        """Get list of GitHub user's followers.

        :param str username: GitHub user name

        """
        return self.get_values("show", username, "followers", filter="users")

    def following(self, username):
        """Get list of users a GitHub user is following.

        :param str username: GitHub user name

        """
        return self.get_values("show", username, "following", filter="users")

    @requires_auth
    def follow(self, other_user):
        """Follow a GitHub user.

        :param str other_user: GitHub user name

        """
        return self.get_values("follow", other_user, method="POST")

    @requires_auth
    def unfollow(self, other_user):
        """Unfollow a GitHub user.

        :param str other_user: GitHub user name

        """
        return self.get_values("unfollow", other_user, method="POST")

    @requires_auth
    def list_keys(self):
        """Get list of SSH keys for the authenticated user."""
        return self.get_values('keys', filter='public_keys', datatype=Key)

    @requires_auth
    def add_key(self, key, title=''):
        """Add a SSH key for the authenticated user.

        :param str key: SSH key identifier
        :param str title: Optional title for the SSH key

        """
        return self.get_values("key/add",
                               post_data={'key': key, 'title': title},
                               method="POST", filter='public_keys',
                               datatype=Key)

    @requires_auth
    def remove_key(self, key_id):
        """Remove a SSH key for the authenticated user.

        :param int key_id: SSH key's GitHub identifier

        """
        return self.get_values('key/remove', post_data={'id': str(key_id)},
                               filter='public_keys', datatype=Key)
