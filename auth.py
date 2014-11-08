#!/usr/bin/env python3

import sys

from pocket import Pocket

consumer_key = sys.argv[1]

redirect_uri = "http://tumbolia.org/"

request_token = Pocket.get_request_token(
    consumer_key=consumer_key, redirect_uri=redirect_uri)

auth_url = Pocket.get_auth_url(
    code=request_token, redirect_uri=redirect_uri)

user_credentials = Pocket.get_credentials(
    consumer_key=consumer_key, code=request_token)

print(user_credentials['access_token'])
