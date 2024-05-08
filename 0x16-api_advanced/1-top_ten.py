#!/usr/bin/python3
"""
Function that queries the Reddit API and
returns the number of subscribers
"""

import requests


def top_ten(subreddit):
    """ Function that queries the Reddit API """

    url = f"https://www.reddit.com/r/{subreddit}/about.json"
    headers = {'User-Agent': 'by u/UniqueAgent-007'}
    response = requests.get(url, headers=headers)
    
    if response.status_code == 200:
        data = response.json()
        if 'data' in data and 'children' in data['data']:
            posts = data['data']['children']
            for post in posts:
                print(post['data']['title'])
        else:
            print("No posts found for this subreddit.")
    else:
        print("None")
