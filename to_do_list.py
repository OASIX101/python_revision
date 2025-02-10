# Sure! How about building a **To-Do List app** in Python? It’s a great way to practice working with data structures, file handling, and basic user interfaces.

# ### Task: Create a To-Do List Application

# **Features:**
# 1. **Add a Task**: Allow the user to add tasks.
# 2. **View Tasks**: Show all tasks that have been added.
# 3. **Mark Tasks as Done**: Allow the user to mark tasks as completed.
# 4. **Delete a Task**: Let the user delete a task if it’s no longer needed.
# 5. **Save and Load Tasks**: Save the tasks to a file so they persist between sessions.

# **Bonus:**
# - Implement a simple text-based user interface.
# - Sort the tasks based on whether they are completed or not.

# ### Suggested Python Concepts to Practice:
# - Lists (to hold the tasks)
# - File handling (to save and load tasks)
# - Basic functions (for each of the operations)
# - Conditionals (to check if a task is done)
# - Loops (to display tasks and interact with the user)

import time


with open('python/to_do_list_db.txt', 'r') as file:
    database = eval(file.read())


def create_task(data: dict, task: str):
    """this is function that adds a new task to the database with unique ids 
    """
    id = 0
    day_created = f"{time.strftime("%Y%m%d")}{id}"
    ids = []
    for i in data.keys(): # checks for the tasks of that day and gets the id of the recently added task and adds one to it to create a unique id
        if i[0:8] == day_created[0:8]:
            ids.append(int(i[8:]))        

        continue

    if ids == []: # checks if there is a task created for the day
        data[day_created] = {
        "task" : task,
        "done" : False
    }
        
        with open('python/to_do_list_db.txt', 'w') as file:
            file.write(str(data))
    else:
        day_created = f"{time.strftime("%Y%m%d")}{max(ids)+1}"
        data[day_created] = {
        "task" : task,
        "done" : False
        }

        with open('python/to_do_list_db.txt', 'w') as file:
            file.write(str(data))
    
    return data

def view_task(data: dict, tasks_date: str):
    """This is a function that checks the task related to the date provided if it exists and return a new dict of the task
    """
    id_list = []
    new_dic = {}
    if len(tasks_date) == 8:
        pass
    else:
        print("Invalid date length")
 
    for i in data.keys():
        if i[0:8] == tasks_date:
            id_list.append(i)
            continue
        else:
            print("Taks not found relating to the date provided")
            break

    for ids in id_list:
        new_dic[ids] = data.get(ids)

    return new_dic

def mark_as_done(data: dict, task_id: str):
    info = data.get(task_id)      
    if task_id in data.keys():

        if info["done"] == True:
            print("This task has been marked as done already")
        else:
            info["done"] = True
            with open('python/to_do_list_db.txt', 'w') as file:
                file.write(str(data))
         
    else:
        info = "Task not found"
        
    return f"{task_id} : {info}"

def delete(data:dict, task_id: str):
    info = data.get(task_id)      
    if task_id in data.keys():
        data.__delitem__(task_id)
        with open('python/to_do_list_db.txt', 'w') as file:
            file.write(str(data))
        print("Task successfully deleted")
        return data
         
    else:
        return "Task not found"

print("welcome to my to_do_list app The Oasix")
while True:
    operation = input("\nInput the corresponding numbers shown below to perform the following operation...\n1. Create new task\n2. view all tasks created for a date\n3. Mark task as done\n4. Delete task\n5. stop\n------> ")
    if operation == "1":
        task = input("Enter task: ")
        print(create_task(database, task))
        continue

    if operation == "2":
        task_date = input("Enter task date to be viewed: ")
        print(view_task(database, task_date))
        continue

    if operation == "3":
        task_id = input("Enter task id to be marked as done: ")
        print(mark_as_done(database, task_id))
        continue
        
    if operation == "4":
        task_id = input("Enter task id to be deleted: ")
        print(delete(database, task_id))
        continue
    
    if operation == "5":
        print("Goodbyyyye!")
        break

    if operation != "1" or "2" or "3" or "4" or "5":
        print("Invalid input. Responds must be either 1,2,3,4,5")
        continue