#!/usr/bin/python3
"""
module that hosts the function number_of_subscribers
"""
import requests


def number_of_subscribers(subreddit):
    """
    queries the Reddit API and returns the number of subscribers
    (not active users, total subscribers) for a given subreddit.
    If an invalid subreddit is given, the function should return 0.
    """
    url = "https://www.reddit.com/r/{}/about.json".format(subreddit)
    headers = {'User-Agent': 'My User Agent 1.0'}

    response = requests.get(url, headers=headers, allow_redirects=False)
    if response.status_code == 404:
        return 0
    subscribers = response.json().get('data').get('subscribers')
    return subscribers
