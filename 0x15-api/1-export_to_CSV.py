#!/usr/bin/python3
'''
Module: '1-export_to_CSV'
Python script that returns information about TODO list progress of emoloyee
and stores in csv format
'''

import csv
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
        user_id = user_data.get("id")
        completed_tasks = [(user_id,
                            employee_name,
                            task["completed"],
                            task["title"]) for task in todo_data]

        return completed_tasks

    except requests.exceptions.RequestException as e:
        print("Error occurred while fetching data:", e)
        sys.exit(1)


def export_to_csv(data, filename):
    with open(filename, mode='w', newline='') as file:
        writer = csv.writer(file, quoting=csv.QUOTE_ALL)
        writer.writerow([
            "USER_ID",
            "USERNAME",
            "TASK_COMPLETED_STATUS",
            "TASK_TITLE"
            ])
        writer.writerows(data)


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python3 script.py EMPLOYEE_ID")
        sys.exit(1)

    try:
        employee_id = int(sys.argv[1])
    except ValueError:
        print("Employee ID must be an integer.")
        sys.exit(1)

    employee_todo_progress = get_employee_todo_progress(employee_id)
    if employee_todo_progress:
        filename = f"{employee_id}.csv"
        export_to_csv(employee_todo_progress, filename)
