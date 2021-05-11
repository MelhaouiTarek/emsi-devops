#!/usr/bin/python3
"""
Getting the top 10 hot posts in a subreddit
"""
import requests


def recurse(subreddit,hot_list=[],new="end" ):
    """
        function returns the all hot posts of a subreddit recursively
    """
    url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
    # setting user agent
    headers = {'User-Agent': 'Test'}

    if new != "end":
        url = url + "?after={}".format(new)
    
    response = requests.get(url, headers=headers, allow_redirects=False)
    titles = response.json()['data']['children']
    if not titles:
        return None
    else:
        for post in titles:
            hot_list.append(post['data']['title'])
    #adds next 25 posts 
    new=response.json().get('data').get('after')
    if not new:
        return hot_list
    return (recurse(subreddit,hot_list,new))
        
