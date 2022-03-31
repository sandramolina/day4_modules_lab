

# Functions to complete:

## Get a list of uncompleted tasks
def get_uncompleted_tasks(list):
    uncompleted_tasks_list = []
    for index, task in enumerate(list):
        if list[index]["completed"] == False:
            uncompleted_tasks_list.append(task)     
    return uncompleted_tasks_list


## Get a list of completed tasks
def get_completed_tasks(list):
    completed_tasks_list = []
    for index, task in enumerate(list):
        if list[index]["completed"] == True:
            completed_tasks_list.append(task)     
    return completed_tasks_list

# ## Get tasks where time_taken is at least a given time
def get_tasks_taking_at_least(list, time):
    time_taken_task = []
    for index, task in enumerate(list):
        if list[index]["time_taken"] >= time:
            time_taken_task.append(task)
    return time_taken_task

# ## Find a task with a given description
def get_task_with_description(list, description):
    for index, task in enumerate(list):
        if list[index]["description"] == description:
            return task

# # Extention (Function): 

# ## Get a list of tasks by status
def get_tasks_by_status(list, status):
    list_completed = []
    list_uncompleted = []
    if status == "completed":
        list_completed = get_completed_tasks(list)
        return list_completed
    elif status == "uncompleted":
        list_uncompleted = get_uncompleted_tasks(list)
        return list_uncompleted

def mark_task_complete(task):
    task["completed"] = True

def create_task(description, time_taken):
    task = {}
    task["description"] = description
    task["completed"] = False
    task["time_taken"] = time_taken

    return task

def add_to_list(list, task):
    list.append(task)
