#!/usr/bin/python3
"""
Getting number of subscribers for a subreddit
"""
import requests


def number_of_subscribers(subreddit):
    """
        function returns number of subscribers or 0 if invalid subreddit
    """
    url = "https://www.reddit.com/r/{}/about.json".format(subreddit)
    #user agent
    headers = {'User-Agent': 'Test'}

    response = requests.get(url, headers=headers).json()
    subs = response.get('data',{}).get('subscribers',{})
    
    if not subs:
        return 0
    return subs
