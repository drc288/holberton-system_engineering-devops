#!/usr/bin/python3
"""Recursive count"""
import requests


def recurse(subreddit, hot_list=[], after=""):
    """
    Create a recursive search in the API of Reddit
    :param subreddit: the subredit divition
    :param hot_list: list to append the data
    :param after: after position
    :return: a list of data
    """
    url = "https://www.reddit.com/r/"
    header = {
        'User-Agent': 'My user 1.0'
    }
    to_search = url + subreddit + "/hot.json"
    parameters = {
        "limit": 100,
        "after": after
    }
    req = requests.get(to_search, headers=header, params=parameters)

    if after is None:
        return hot_list

    if req.status_code == 404:
        return None

    res = req.json()
    for new_dst in res.get("data").get("children"):
        hot_list.append(new_dst.get("data").get("title"))

    after = res.get("data").get("after")
    return recurse(subreddit, hot_list, after)
