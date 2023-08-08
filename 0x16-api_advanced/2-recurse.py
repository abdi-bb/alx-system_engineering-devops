#!/usr/bin/python3
'''
Module: '2-recurse'
'''

import requests


def recurse(subreddit, hot_list=[], count=0, after=None):
    '''Returns a list containing the titles of
    all hot articles for a given subreddit
    '''
    url = f'https://www.reddit.com/r/{subreddit}/hot.json'
    headers = {'User-Agent': 'MyWebApp'}
    params = {'count': count, 'after': after}

    hot_posts = requests.get(
            url,
            headers=headers,
            params=params,
            allow_redirects=False
            )
    if hot_posts.status_code >= 400:
        return None
    for child in hot_posts.json().get('data').get('children'):
        new_hot_list = hot_list + child.get('data').get('title')

    json_hot_posts = hot_posts.json()
    if not json_hot_posts.get('data').get('after'):
        return new_hot_list
    return recurse(
            subreddit,
            new_hot_list,
            json_hot_list.get('data').get('count'),
            json_hot_list.get('data').get('after')
            )
