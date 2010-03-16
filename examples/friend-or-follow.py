import sys
import optparse
from subprocess import Popen, PIPE

from github2.client import Github

ITEM_FMT = "* %s (%s)"
URL_USER_FMT = "http://github.com/%s"

OPTION_LIST = (
    optparse.make_option('-t', '--api-token',
            default=None, action="store", dest="api_token", type="str",
            help="Github API token. Default is to find this from git config"),
    optparse.make_option('-u', '--api-user',
            default=None, action="store", dest="api_user", type="str",
            help="Github Username. Default is to find this from git config"),
)
BY_LOWER = lambda value: value.lower()


class FriendOrFollow(object):
    # Caching api calls
    _followers = None
    _following = None

    def __init__(self, username=None, api_user=None, api_token=None):
        self.api_user = api_user or self.git_config_get("github.user")
        self.api_token = api_token or self.git_config_get("github.token")
        self.username = username or self.api_user
        print("U:(%s) T:(%s) F:(%s)" % (self.api_user, self.api_token,
            self.username))
        self.client = Github(self.api_user, self.api_token)

    def get_friends(self):
        return sorted((user for user in self.following
                        if user in self.followers), key=BY_LOWER)

    def get_following(self):
        return sorted((user for user in self.following
                        if user not in self.followers), key=BY_LOWER)

    def get_fans(self):
        return sorted((user for user in self.followers
                        if user not in self.following), key=BY_LOWER)

    def users_with_urls(self, users):
        return ((user, URL_USER_FMT % user)
                    for user in users)

    def git_config_get(self, key):
        pipe = Popen(["git", "config", "--get", key], stdout=PIPE)
        return pipe.communicate()[0].strip()

    @property
    def followers(self):
        if self._followers is None:
            self._followers = self.client.users.followers(self.username)
        return self._followers

    @property
    def following(self):
        if self._following is None:
            self._following = self.client.users.following(self.username)
        return self._following


def parse_options(arguments):
    parser = optparse.OptionParser(option_list=OPTION_LIST)
    options, values = parser.parse_args(arguments)
    return options, values


def format_output(*data):
    headify = lambda title: "\n".join([title, "=" * len(title)])
    itemify = lambda item: ITEM_FMT % item

    def format_section(header, items):
        return "\n".join(["\n%s\n" % headify(header)] +
                         [itemify(item) for item in items])

    return "\n".join(format_section(*section)
                            for section in data)


def main():
    options, values = parse_options(sys.argv[1:])
    username = values and values[0] or None
    f = FriendOrFollow(username=username, **vars(options))
    print(format_output(
            ("Friends", f.users_with_urls(f.get_friends())),
            ("Following", f.users_with_urls(f.get_following())),
            ("Fans", f.users_with_urls(f.get_fans()))))

if __name__ == "__main__":
    main()
