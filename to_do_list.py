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
    id = 0
    day_created = f"{time.strftime("%Y%m06")}{id}"

    if day_created not in data.keys():
        data[day_created] = {
        "task" : task,
        "done" : False
    }
        
        with open('python/to_do_list_db.txt', 'w') as file:
            file.write(str(data))
    else:
        ids = []
        for i in data.keys():
            if i[0:8] == day_created[0:8]:
                ids.append(int(i[8:]))        

            continue

        day_created = f"{time.strftime("%Y%m%d")}{max(ids)+1}"
        data[day_created] = {
        "task" : task,
        "done" : False
        }

        with open('python/to_do_list_db.txt', 'w') as file:
            file.write(str(data))
    
    return data

task = input("Enter task: ")
print(create_task(database, task))