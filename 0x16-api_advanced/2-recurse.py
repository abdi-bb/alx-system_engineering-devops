#!/usr/bin/python3
"""
2-recurse
"""
import requests


def recurse(subreddit, hot_list=[], after=None):
    """
    Queries the Reddit API and returns a list of titles of hot articles
    for a given subreddit. If no results are found, returns None.
    """
    # Base case: no more pages to fetch
    if after is None and len(hot_list) > 0:
        return hot_list

    # Recursive case: fetch the next page and append the titles to the list
    url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
    headers = {"User-Agent": "python3:alx-system_engineering-devops"}
    params = {"limit": 100, "after": after}
    response = requests.get(url, headers=headers, params=params,
                            allow_redirects=False)
    if response.status_code != 200:
        return None
    data = response.json().get("data")
    if data is None:
        return None
    after = data.get("after")
    children = data.get("children")
    if children is None or len(children) == 0:
        return None
    for child in children:
        title = child.get("data").get("title")
        if title is not None:
            hot_list.append(title)
    return recurse(subreddit, hot_list, after)
