#!/usr/bin/python3
"""
This file consume a api for https://jsonplaceholder.typicode.com/
"""
import requests
from sys import argv


if __name__ == "__main__":
    id_user = argv[1]
    complete = 0
    user = requests.get("https://jsonplaceholder.typicode.com/users/{}"
                        .format(id_user))
    td = requests.get("https://jsonplaceholder.typicode.com/todos?userId={}"
                      .format(id_user))

    json_td = td.json()
    json_user = user.json()
    user_name = json_user.get("name")

    for comp in json_td:
        if comp.get("completed"):
            complete += 1

    print("Employee {} is done with tasks({}/{}):"
          .format(user_name, complete, len(json_td)))

    for title in json_td:
        if title.get("completed"):
            print("\t {}".format(title.get("title")))