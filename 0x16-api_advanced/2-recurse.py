#!/usr/bin/python3
"""
Below is a recursive function that queries the Reddit API
and returns a list containing the titles of all hot
articles for a given subreddit
"""


import requests


def recurse(subreddit, hot_list=[]):
    """ Recursive functin that returns list """

    url = f"https://www.reddit.com/r/{subreddit}/hot.json"
    headers = {'User-Agent': 'by u/UniqueAgent-007'}
    response = requests.get(url, headers=headers)

    if response.status_code == 200:
        data = response.json()
        if 'data' in data and 'children' in data['data'] and len(data['data']['children']) > 0:
            posts = data['data']['children']
            for post in posts:
                hot_list.append(post['data']['title'])
            return hot_list
        else:
            return None
    else:
        return None
