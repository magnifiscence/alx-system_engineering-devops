#!/usr/bin/python3
"""Gather data from an API and export to JSON"""
import json
import requests
from sys import argv


if __name__ == "__main__":
    """Gather data from an API and export to JSON"""
    url = "https://jsonplaceholder.typicode.com/"
    user_id = argv[1]
    user = requests.get(url + "users/{}".format(user_id)).json()
    todos = requests.get(url + "todos?userId={}".format(user_id)).json()
    tasks = []
    for task in todos:
        tasks.append({"task": task.get("title"),
                      "completed": task.get("completed"),
                      "username": user.get("username")})
    with open("{}.json".format(user_id), "w") as jsonfile:
        json.dump({user_id: tasks}, jsonfile)
