#!/usr/bin/python3
"""
This file consume a api for https://jsonplaceholder.typicode.com/ and create
a new CSV file
"""
import csv
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

    with open("{}.csv".format(id_user), "w") as file:
        new_file = csv.writer(file, quoting=csv.QUOTE_ALL)
        for num_data in range(len(json_td)):
            new_file.writerow([json_user["id"], json_user["username"],
                               json_td[num_data]["completed"],
                               json_td[num_data]["title"]])
