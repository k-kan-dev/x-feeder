import os
import sys
from datetime import datetime
from typing import Dict, List, Union

from dateutil import parser
from dotenv import load_dotenv
import requests

sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))

from .error import (
    InvalidXGetUserIdException,
    InvalidXGetTweetsException,
    InvalidRequestTooManyRequestsException
)


class X:

    def __init__(self,
                 ):
        self.bearer_token = os.getenv("X_BEARER_TOKEN")
        self.headers = {
            "Authorization": f"Bearer {self.bearer_token}",
            "User-Agent": "v2UserTweetsPython"
        }

    def get_user_id(self,
                    username : str
                    ):
        """ get user_id using X API

        Args:
            username (str):
                account name in X
        Returns:
            user_id (str)
                user id in X
        """
        url = f"https://api.twitter.com/2/users/by/username/{username}"
        res = requests.get(url, headers = self.headers)

        if res.status_code == 200:
            user_data = res.json()
            return user_data.get("data", {}).get("id")
        elif res.status_code == 429:
            raise InvalidRequestTooManyRequestsException(res.text)
        else:
            raise InvalidXGetUserIdException(res.text)

    def get_tweets(self,
                   user_id : str,
                   max_results : int = 10
                   ) -> List[Dict[str, Union[str, datetime]]]:
        """ get tweets using X API

        Args:
            user_id (str):
                user id in X
            max_results (int, optional):
                max num of tweets. Defaults to 10.

        Returns:
            tweets_summary (List[Dict[str, Union[str, datetime]]]):
                [
                    {
                        "tweeted_time" : (datetime),
                        "tweet_url" : (str)
                    }
                ]
        """
        tweets_summary = []

        # 1. getting tweets using API
        params = {
            "max_results" : max_results,
            "tweet.fields" : "created_at,id"
        }
        url = f"https://api.twitter.com/2/users/{user_id}/tweets"
        res = requests.get(
            url,
            headers = self.headers,
            params = params
        )

        # 2. check
        if res.status_code == 200:
            # 3. format
            tweets = res.json().get("data", [])

            for tweet in tweets:
                tweeted_time_obj = parser.parse(tweet["created_at"])
                tweet_id = tweet["id"]
                tweet_url = f"https://x.com/ToF_JP/status/{tweet_id}"
                tweets_summary.append(
                    {
                        "tweeted_time" : tweeted_time_obj,
                        "tweet_url" : tweet_url,
                        "twwet_id" : tweet_id
                    }
                )
        elif res.status_code == 429:
            raise InvalidRequestTooManyRequestsException(res.text)
        else:
            raise InvalidXGetTweetsException(res.text)

        return tweets_summary

if __name__ == "__main__":
    """ as test

        test

    """
    load_dotenv("./xfeeder/config/.env")
    x = X()
    user_id = x.get_user_id(
        username="ToF_JP"
    )
    tweets = x.get_tweets(
        user_id = user_id,
        max_results = 5
    )
    print(tweets)
