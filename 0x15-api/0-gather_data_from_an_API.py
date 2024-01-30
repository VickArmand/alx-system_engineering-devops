#!/usr/bin/python3
"""
Python script that, using this REST API, for a given employee ID,
returns information about his/her TODO list progress.
Requirements:
    The script must accept an integer as a parameter, which is the employee ID
    The script must display on the standard output the employee
    TODO list progress in this exact format:
    First line: Employee EMPLOYEE_NAME is done with tasks
    (NUMBER_OF_DONE_TASKS/TOTAL_NUMBER_OF_TASKS):
    EMPLOYEE_NAME: name of the employee
    NUMBER_OF_DONE_TASKS: number of completed tasks
    TOTAL_NUMBER_OF_TASKS: total number of tasks,
    which is the sum of completed and non-completed tasks
    Second and N next lines display the title of completed tasks:
    TASK_TITLE (with 1 tabulation and 1 space before the TASK_TITLE)
"""
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
    with urllib.request.urlopen(req1) as response:
        tasks = json.loads(response.read())
    completed_tasks = 0
    second_line = ""
    for d in tasks:
        if d.get('completed'):
            second_line += "\t {}\n".format(d.get('title'))
            completed_tasks += 1
    print("Employee {} is done with tasks({}/{}):".format(
        user.get('name'), completed_tasks, len(tasks)))
    print(second_line, end="")
