#!/usr/bin/python3
"""Exports the previously returned to-do list information to JSON format."""
import json
import requests

if __name__ == "__main__":
    url = "https://jsonplaceholder.typicode.com/"
    users = requests.get(url + "users").json()

    with open("todo_all_employees.json", "w") as jsonfile:
        json.dump({
            u.get("id"): [{
                "task": task.get("title"),
                "completed": task.get("completed"),
                "username": u.get("username")
            } for task in requests.get(url + "todos",
                                       params={"userId": u.get("id")}).json()]
            for u in users}, jsonfile)
