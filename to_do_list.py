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
        return{"task":[]}


def save_task(data):
    with open(file_name, "w") as file:
        json.dump(data, file, indent=4)
    print("Task Saved")


def add_task(data):

    task = input("Enter the task : ")
    priority = input("Enter priority (High/Medium/Low): ")

    new_task = {"task": task, "priority": priority}
    data["task"].append(new_task)
    save_task(data)


def view_task(data):

    if not data["task"]:
        print("You don't have task yet")
        return

    for title in data["task"]:
        print(f"Task : {title['task']}  Priority : {title['priority']}")


# Working
def main():
    todo_data = load_task()

    while True:
        print("\nOptions: [1] View Tasks  [2] Add Task  [3] Quit")
        choice = input("What would you like to do? ")

        if choice == "1":
            view_task(todo_data)
        elif choice == "2":
            add_task(todo_data)
        elif choice == "3":
            print("Goodbye!")
            break
        else:
            print("Invalid choice, please type 1, 2, or 3.")


main()
