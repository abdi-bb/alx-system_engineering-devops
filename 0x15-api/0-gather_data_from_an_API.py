#!/usr/bin/python3
'''
Module: '0-gather_data_from_an_API'
Python script that returns information about TODO list progress of emoloyee
'''

import requests
import sys


def get_employee_todo_progress(employee_id):
    base_url = "https://jsonplaceholder.typicode.com"
    user_url = f"{base_url}/users/{employee_id}"
    todos_url = f"{base_url}/todos?userId={employee_id}"

    try:
        user_data = requests.get(user_url).json()
        todo_data = requests.get(todos_url).json()

        employee_name = user_data.get("name")
        total_tasks = len(todo_data)
        done_tasks = sum(1 for task in todo_data if task["completed"])
        completed_titles = [task["title"] for task in todo_data
                            if task["completed"]]

        print("Employee {} is done with tasks({}/{}):".format(
            employee_name,
            done_tasks,
            total_tasks))
        for title in completed_titles:
            print(f"\t{title}")

    except requests.exceptions.RequestException as e:
        print("Error occurred while fetching data:", e)
        sys.exit(1)


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python3 script.py EMPLOYEE_ID")
        sys.exit(1)

    try:
        employee_id = int(sys.argv[1])
    except ValueError:
        print("Employee ID must be an integer.")
        sys.exit(1)

    get_employee_todo_progress(employee_id)
