#!/usr/bin/python3
"""
extend your Python script from 0-gather_data_from_an_API.py
to export data in the JSON format.

Requirements:
    Records all tasks from all employees
    Format must be: { "USER_ID": [ {"username": "USERNAME",
    "task": "TASK_TITLE", "completed": TASK_COMPLETED_STATUS},
    {"username": "USERNAME", "task": "TASK_TITLE",
    "completed": TASK_COMPLETED_STATUS}, ... ],
    "USER_ID": [ {"username": "USERNAME", "task": "TASK_TITLE",
    "completed": TASK_COMPLETED_STATUS},
    {"username": "USERNAME", "task": "TASK_TITLE",
    "completed": TASK_COMPLETED_STATUS}, ... ]}
    File name must be: todo_all_employees.json
"""
import csv
import json
import sys
import urllib.request


if __name__ == "__main__":
    req0 = urllib.request.Request(
            "https://jsonplaceholder.typicode.com/users")
    with urllib.request.urlopen(req0) as response:
        users = json.loads(response.read())
    req1 = urllib.request.Request(
            "https://jsonplaceholder.typicode.com/todos")
    filename = "todo_all_employees.json"
    with urllib.request.urlopen(req1) as response:
        all_tasks = json.loads(response.read())
    data = {}
    for user in users:
        for task in all_tasks:
            if user.get('id') == task.get('userId'):
                user_id = user.get('id')
                if user_id in data.keys():
                    data[user_id].append(
                            {'task': task.get('title'),
                                'username': user.get('username'),
                                'completed': task.get('completed')}
                            )
                else:
                    data[user_id] = [{'task': task.get('title'),
                                      'username': user.get('username'),
                                      'completed': task.get('completed')}]
    with open(filename, 'w') as jsonfile:
        json.dump(data, jsonfile)
