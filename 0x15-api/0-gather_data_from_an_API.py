#!/usr/bin/env python3

import requests
from sys import argv


if __name__ == '__main__':
    if len(argv) != 2:
        print("Usage: ./0-gather_data_from_an_API.py <employee_id>")
        exit(1)

    employee_id = argv[1]
    user = requests.get(
            'https://jsonplaceholder.typicode.com/users/{}'.format(
                employee_id)).json()
    todos = requests.get(
            'https://jsonplaceholder.typicode.com/todos?userId={}'.format(
                employee_id)).json()

    done_tasks = [task for task in todos if task.get('completed') is True]
    print("Employee {} is done with tasks({}/{}):".format(
        user.get('name'),
        len(done_tasks),
        len(todos)
        ))
    for task in done_tasks:
        print("\t {}".format(task.get('title')))
