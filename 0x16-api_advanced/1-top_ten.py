#!/usr/bin/python3
"""
This module hosts top_ten function
"""
import requests


def top_ten(subreddit):
    """
    function that queries the Reddit API and prints the titles of the
    first 10 hot posts listed for a given subreddit.
    If not a valid subreddit, print None.
    NOTE: Invalid subreddits may return a redirect to search results.
    Ensure that you are not following redirects.
    """
    url = 'https://www.reddit.com/r/{}/hot.json?limit=10'.format(subreddit)
    headers = {'User-Agent': 'My User Agent 1.0'}

    response = requests.get(url, headers=headers, allow_redirects=False)
    if response.status_code == 404:
        print ("None")
    else:
        for post in response.json().get('data').get('children'):
            print(post.get('data').get('title'))
