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
    Hint: No authentication is necessary for most features of the Reddit API.
    If you’re getting errors related to Too Many Requests,
    ensure you’re setting a custom User-Agent.
    NOTE: Invalid subreddits may return a redirect to search results.
    Ensure that you are not following redirects.
    """
    url = "https://www.reddit.com/r/{}/about.json".format(subreddit)
    headers = {'User-Agent': 'My User Agent 1.0'}

    response = requests.get(url, headers=headers, allow_redirects=False)
    if response.status_code >= 300:
        return 0
    else:
        r = response.json()
        subscribers = response.get('data', {}).get('subscribers')
        if not subscribers:
            return 0
        return subscribers
