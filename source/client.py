#!/usr/bin/python
import base64
import json
import requests


class Client(object):
    """Class Client."""

    _consumer_key = ""
    _consumer_secret = ""
    _auth_url = "https://api.twitter.com/oauth2/token"
    _search_url = "https://api.twitter.com/1.1/search/tweets.json"

    def __init__(self, id):
        """Init."""
        self._id = id

    def _get_access_token(self):
        """Get access token."""
        _key = "%s:%s" % (self._consumer_key, self._consumer_secret)

        _key = _key.encode("ascii")
        _key = base64.b64encode(_key)
        _key = _key.decode("ascii")

        _headers = {
            "Authorization": "Basic " + _key,
            "Content-Type": "application/x-www-form-urlencoded;charset=UTF-8"
        }

        _data = {
            "grant_type": "client_credentials"
        }

        r = requests.post(self._auth_url, headers=_headers, data=_data)

        return r

    def get_tweets_json(self, search,
                        lang=None,
                        result_type=None,
                        count=None):
        """Get tweets."""
        _access_token = self._get_access_token().json()['access_token']

        _headers = {
            "Authorization": "Bearer " + _access_token
        }

        _params = {
            "q": search,
            "lang": lang,
            "result_type": result_type,
            "count": count
        }

        r = requests.get(self._search_url, headers=_headers, params=_params)

        return json.loads(r.content)
