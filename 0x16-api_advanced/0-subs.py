#!/usr/bin/python3
"""
This file send a request  to https://www.reddit.com and get
the subredit
"""
import requests


def number_of_subscribers(subreddit):
    """Get all subscribers for a subreddit
        Input: Str(subreddit)
        Out: Int(total of subscribers)
    """
    url = "https://www.reddit.com/r/"
    header = {
        'User-Agent': 'My user 1.0'
    }
    to_search = url + subreddit + "/about.json"

    req = requests.get(to_search, headers=header)
    if req.status_code == 404:
        return 0
    
    dataJSON = req.json().get("data")
    return dataJSON.get("subscribers")
