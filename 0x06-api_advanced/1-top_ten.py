#!/usr/bin/python3
"""
Getting the top 10 hot posts in a subreddit
"""
import requests


def top_ten(subreddit):
    """
        function returns the top posts of a subreddit
        or "None" for an invalid subreddit
    """
    url = "https://www.reddit.com/r/{}/hot.json?limit=10".format(subreddit)
    # user agent
    headers = {'User-Agent': 'Test'}
    response = requests.get(url, headers=headers)
    titles = response.json().get('data', {}).get('children', [])
    if not titles:
        print(None)
    else:
        for hot in titles:
            print(hot['data']['title'])
