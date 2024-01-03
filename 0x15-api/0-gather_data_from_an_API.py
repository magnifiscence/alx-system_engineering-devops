#!/usr/bin/python3
"""Gather data from an API"""
import requests
from sys import argv


if __name__ == "__main__":
    """Gather data from an API"""
    url = "https://jsonplaceholder.typicode.com/"
    user_id = argv[1]
    user = requests.get(url + "users/{}".format(user_id)).json()
    todos = requests.get(url + "todos?userId={}".format(user_id)).json()
    completed_tasks = []
    for task in todos:
        if task.get("completed"):
            completed_tasks.append(task.get("title"))
    print("Employee {} is done with tasks({}/{}):".format(
        user.get("name"), len(completed_tasks), len(todos)))
    for task in completed_tasks:
        print("\t {}".format(task))
