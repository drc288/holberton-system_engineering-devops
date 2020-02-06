#!/usr/bin/python3
"""
This file send a request  to https://www.reddit.com and get
the subredit and return the first 10 position
"""
import requests


def top_ten(subreddit):
    """Get all subscribers for a subreddit
        Input: Str(subreddit)
        Out: Int(total of subscribers)
    """
    url = "https://www.reddit.com/r/"
    header = {
        'User-Agent': 'My user 1.0'
    }
    to_search = url + subreddit + "/hot.json?limit=10"
    req = requests.get(to_search, headers=header)
    if req.status_code == 404:
        return None

    t_ch = req.json().get("data")
    data_tch = t_ch.get("children")
    for ps_list in data_tch:
        print(ps_list.get("data")["title"])
