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

    r = requests.get(url, headers=headers, allow_redirects=False).json()
    subscribers = r.get('data').get('subscribers')
    if not subscribers:
        return 0
    return subscribers
