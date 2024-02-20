#!/usr/bin/python3
"""
This module hosts recurse function
"""
import requests


def recurse(subreddit, hot_list=[], after="tmp"):
    """
    a recursive function that queries the Reddit API and returns a list
    containing the titles of all hot articles for a given subreddit.
    If no results are found for the given subreddit,
    the function should return None.
    Hint: The Reddit API uses pagination for separating pages of responses.
    """
    url = 'https://www.reddit.com/r/{}/hot.json'.format(subreddit)
    headers = {'User-Agent': 'My User Agent 1.0'}
    if after != "tmp":
        url = url + "?after={}".format(after)
    response = requests.get(url, headers=headers).json()
    hot_articles = response.get('data', {}).get('children', [])
    if not hot_articles:
        return None
    for post in hot_articles:
        hot_list.append(post.get('data').get('title'))
    after = response.get('data').get('after')
    if not after:
        return hot_list
    return (recurse(subreddit, hot_list, after))
