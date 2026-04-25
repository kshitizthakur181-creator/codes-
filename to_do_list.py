import os
import json

file_name = "todo_list.json"

# Simple Features


def load_task():

    if os.path.exists(file_name):
        with open(file_name, "r") as file:
            return json.load(file)

    else:
        print("No such file exsist")


def save_task(data):
    with open(file_name, "w") as file:
        json.dump(data, file, indent=4)
    print("Task Saved")


def add_task(data):

    task = input("Enter the task : ")
    priority = input("Enter priority (High/Medium/Low): ")

    new_task = {"task": task, "priority": priority}
    data["task"].append(new_task)
    save_task


def view_task(data):
    
    if not data['task']:
        print("You don't have task yet")
        
    for title in data["task"]:
        print(f"Task : {title["task"]}  Priority : {title["priority"]}")

# Working
