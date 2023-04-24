#!/usr/bin/python3
"""script using this REST API, for a given employee ID,
returns information about his/her TODO list progress."""
import sys
import requests

def get_employee_todo_progress(employee_id):
    # Fetching employee information
    employee_response = requests.get(f'https://jsonplaceholder.typicode.com/users/{employee_id}')
    employee = employee_response.json()

    # Fetching employee's TODO list
    todos_response = requests.get(f'https://jsonplaceholder.typicode.com/todos?userId={employee_id}')
    todos = todos_response.json()

    # Calculating TODO list progress
    completed_tasks = [todo for todo in todos if todo['completed']]
    total_tasks = len(todos)

    # Displaying TODO list progress
    print(f"Employee {employee['name']} is done with tasks({len(completed_tasks)}/{total_tasks}):")
    for task in completed_tasks:
        print(f"\t {task['title']}")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python employee_todo_progress.py <employee_id>")
    else:
        try:
            employee_id = int(sys.argv[1])
            get_employee_todo_progress(employee_id)
        except ValueError:
            print("Invalid employee ID. Please provide an integer as the employee ID.")
