#!/usr/bin/python3
"""
extend your Python script from 0-gather_data_from_an_API.py
to export data in the JSON format.

Requirements:
    Records all tasks that are owned by this employee
    Format must be: { "USER_ID": [{"task": "TASK_TITLE",
    "completed": TASK_COMPLETED_STATUS, "username": "USERNAME"},
    {"task": "TASK_TITLE", "completed": TASK_COMPLETED_STATUS,
    "username": "USERNAME"}, ... ]}
    File name must be: USER_ID.json
"""
import csv
import json
import sys
import urllib.request


if __name__ == "__main__":
    e_id = sys.argv[1]
    req0 = urllib.request.Request(
            "https://jsonplaceholder.typicode.com/users/{}".format(e_id))
    with urllib.request.urlopen(req0) as response:
        user = json.loads(response.read())
    req1 = urllib.request.Request(
            "https://jsonplaceholder.typicode.com/users/{}/todos".format(e_id))
    user_id = user.get('id')
    filename = "{}.json".format(user_id)
    with urllib.request.urlopen(req1) as response:
        tasks = json.loads(response.read())
    data = {}
    prev_keys = ['title', 'userId', 'id']
    for record in tasks:
        record['task'] = record.get('title')
        record['username'] = user.get('username')
        for key in prev_keys:
            del record[key]
    data[user_id] = tasks
    with open(filename, 'w') as jsonfile:
        json.dump(data, jsonfile)
