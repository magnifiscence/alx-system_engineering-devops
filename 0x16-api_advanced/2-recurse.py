#!/usr/bin/python3
"""Gather data from an API"""
import requests


def recurse(subreddit, hot_list=[], after=None):
    """
    Queries the Reddit API and returns a list containing the titles of all hot
    articles for a given subreddit. If no results are found for the given
    subreddit, the function should return None.
    """
    url = f"https://www.reddit.com/r/{subreddit}/hot.json"
    headers = {'User-Agent': 'My user Agent 1.0'}
    params = {'after': after, 'limit': 100}

    response = requests.get(url, headers=headers, params=params,
                            allow_redirects=False)

    if response.status_code == 200:
        data = response.json().get('data', {})
        children = data.get('children', [])
        for child in children:
            post = child.get('data', {})
            title = post.get('title', '')
            hot_list.append(title)
        after = data.get('after', None)
        if after is not None:
            recurse(subreddit, hot_list, after)
        return hot_list
    else:
        return None
