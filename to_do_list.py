import os 
import json

file_name = "todo_list.json"

# Simple Features 


def load_task():
    
    if os.path.exists(file_name):
        with open(file_name, "r") as file :
            return json.load(file)
    
    else :
        print("No such file exsist")

def add_task() :
    pass




def completed_task():
    pass

def edit_task():
    pass


# Working 




