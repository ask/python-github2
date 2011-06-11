Solving problems
================

The client object, :class:`~github2.client.Github`, supports a ``debug`` keyword
argument that is invaluable for troubleshooting.  Enabling the ``debug``
functionality will produce output on :data:`sys.stderr` in certain situations.

Request data
''''''''''''

With ``debug`` enabled a message will be produced every time an API request is
made.

    >>> github = Github(debug=True)
    >>> user = github.users.show("JNRowe")
    URL:[https://github.com/api/v2/json/user/show/JNRowe]
    POST_DATA:None
    RESPONSE_TEXT: [{"user":{"gravatar_id":"e40de1eb6e8a74cb96b3f07f3994f155","company":null,"name":"James Rowe","created_at":"2009/03/08 14:53:38 -0700","location":"Cambridge, UK","public_repo_count":41,"public_gist_count":64,"blog":"http://jnrowe.github.com/","following_count":5,"id":61381,"type":"User","permission":null,"followers_count":6,"login":"JNRowe","email":"jnrowe@gmail.com"}}]
    >>> user.gravatar_id
    u'e40de1eb6e8a74cb96b3f07f3994f155'

In the message you can see the URL that was accessed, here
``https://github.com/api/v2/json/user/show/JNRowe``.  You'll also see any HTTP
``post`` method data that was sent, in this case there was none.  And the full
response from GitHub, here the user data of JNRowe.

It has no other affect on the code.

Rate limiting
'''''''''''''

If rate limiting is enabled, with the ``requests_per_second`` when creating a
:class:`~github2.client.Github` object, then you'll see a message when a request
has been delayed.

    >>> github = Github(requests_per_second=0.2, debug=True)
    >>> user = github.users.show("JNRowe")
    >>> user = github.users.show("JNRowe")
    delaying API call 4.99773

Here we have defined a rate limit of one call every five seconds, and doing so
has imposed an almost 5 second delay before completing the second request.