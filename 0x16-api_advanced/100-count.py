#!/usr/bin/python3
"""
100-count
"""
import requests
from collections import Counter


def count_words(subreddit, word_list, after=None, count=None):
    """
    Queries the Reddit API, parses the title of all hot articles,
    and prints a sorted count of given keywords
    """
    # Initialize the count dictionary
    if count is None:
        count = Counter()

    # Base case: no more pages to fetch
    if after is None and len(count) > 0:
        # Sort the count by value (descending) and key (ascending)
        sorted_count = sorted(count.items(), key=lambda x: (-x[1], x[0]))
        # Print the count for each keyword if it is not zero
        for word, n in sorted_count:
            if n > 0:
                print("{}: {}".format(word.lower(), n))
        return

    # Recursive case: fetch the next page and update the count
    url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
    headers = {"User-Agent": "python3:alx-system_engineering-devops"}
    params = {"limit": 100, "after": after}
    response = requests.get(url, headers=headers, params=params,
                            allow_redirects=False)
    if response.status_code != 200:
        return
    data = response.json().get("data")
    if data is None:
        return
    after = data.get("after")
    children = data.get("children")
    if children is None or len(children) == 0:
        return
    for child in children:
        title = child.get("data").get("title")
        if title is not None:
            # Split the title by spaces and punctuation marks
            words = [w.strip(".,!?_:;\"'()[]{}") for w in title.split()]
            # Update the count for each word in the word_list
            for wrd in word_list:
                # Convert the word to lowercase before updating the count
                wrd = wrd.lower()
                count[wrd] += words.count(wrd) + words.count(wrd.capitalize())
    return count_words(subreddit, word_list, after, count)
