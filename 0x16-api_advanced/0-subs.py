#!/usr/bin/python3
'''
Module: '0-subs'
'''

import requests


def number_of_subscribers(subreddit):
    '''Queries the Reddit API and returns the number of total subscribers'''
    url = f'https://www.reddit.com/r/{subreddit}/about.json'
    user_agent = 'MyWebApp'

    subs = requests.get(
            url,
            headers={'User-Agent': user_agent},
            allow_redirects=False
            )
    if subs.status_code >= 300:
        return 0
    return subs.json().get('data').get('subscribers')
