#!/usr/bin/python3
'''
A script to export data in the CSV format.
'''

import csv
import requests
import sys
if __name__ == "__main__":
    get_emp_id = sys.argv[1]
    user_url = f'https://jsonplaceholder.typicode.com/users/{get_emp_id}'
    get_emp_data = requests.get(user_url).json()

    todos_url = (
        f'https://jsonplaceholder.typicode.com/todos?userId={get_emp_id}'
    )
    get_emp_tasks = requests.get(todos_url).json()

    with open("{}.csv".format(get_emp_id), 'w', newline='') as csvfile:
        taskwriter = csv.writer(csvfile, quoting=csv.QUOTE_ALL)
        for task in get_emp_tasks:
            taskwriter.writerow([get_emp_id, get_emp_data.get(
                'username'), task.get('completed'), task.get('title')])
