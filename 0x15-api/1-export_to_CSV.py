#!/usr/bin/python3
"""
extend your Python script from 0-gather_data_from_an_API.py
to export data in the CSV format.

Requirements:
    Records all tasks that are owned by this employee
    Format must be: "USER_ID","USERNAME","TASK_COMPLETED_STATUS",
    "TASK_TITLE"
    File name must be: USER_ID.csv

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
    filename = "{}.csv".format(user.get('id'))
    header = ["userId", "username", "completed", "title"]
    with urllib.request.urlopen(req1) as response:
        tasks = json.loads(response.read())
    completed_tasks = 0
    second_line = ""
    data = {}
    for record in tasks:
        record['username'] = user.get('username')
        del record['id']
    with open(filename, 'w') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=header)
        writer.writerows(tasks)
