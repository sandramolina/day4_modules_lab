from modules.task_list import *
from modules.output import *
from data.task_list import *
from modules.input import *

while (True):
    print_menu()
    user_input = option()
    if (user_input.lower() == 'q'):
        break
    if user_input == '1':
        print_list(tasks)
    elif user_input == '2':
        print_list(get_uncompleted_tasks(tasks))
    elif user_input == '3':
        print_list(get_completed_tasks(tasks))
    elif user_input == '4':
        user_input_description = description()
        task = get_task_with_description(tasks, user_input_description)
        if task is not None:
            mark_task_complete(task)
            print("Task marked complete")
        else:
            print("Task not found")
    elif user_input == '5':
        user_input_time = time()
        print_list(get_tasks_taking_at_least(tasks, user_input_time))
    elif user_input == '6':
        description()
        print(get_task_with_description(tasks, description))
    elif user_input == '7':
        user_input_new = new_description()
        user_input_new_time = time_taken()
        task = create_task(user_input_new, user_input_new_time)
        tasks.append(task)
    else:
        print("Invalid Input - choose another 3")
