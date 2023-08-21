#!/usr/bin/python3
'''
Python script that exports data in the JSON format
'''
import json
import requests
import sys

if __name__ == "__main__":
    get_emp_id = sys.argv[1]
    user_url = (f'https://jsonplaceholder.typicode.com/users/{get_emp_id}')
    get_emp_data = requests.get(user_url).json()
    todos_url = (
        f'https://jsonplaceholder.typicode.com/todos?userId={get_emp_id}'
    )
    get_emp_tasks = requests.get(todos_url).json()

    tasks_list = []
    for task in get_emp_tasks:
        task_dict = {}
        task_dict["task"] = task.get("title")
        task_dict["completed"] = task.get("completed")
        task_dict["username"] = get_emp_data.get("username")
        tasks_list.append(task_dict)

    tasks_json = {}
    tasks_json[get_emp_id] = tasks_list

    with open("{}.json".format(get_emp_id), 'w') as jsonfile:
        json.dump(tasks_json, jsonfile)
