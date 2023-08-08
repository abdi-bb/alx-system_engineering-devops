#!/usr/bin/python3
'''
Module: '1-top_ten'
'''

import requests


def top_ten(subreddit):
    '''Returns the ten hot posts of a given subreddit'''
    url = f'https://www.reddit.com/r/{subreddit}/hot.json?limit=10'

    posts = requests.get(
            url,
            headers={'User-Agent': 'MyWebApp'},
            allow_redirects=False
            )
    if posts.status_code >= 300:
        print('None')
    else:
        for child in posts.json().get('data').get('children'):
            print(child.get('data').get('title'))
