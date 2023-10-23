from database import load_list_of_task, save_list_of_task


def add_new_tasks(new_task, list_of_task):
    list_of_task = load_list_of_task()
    last_task_number = max([int(key) for key in list_of_task.keys()], default=0)
    new_task_number = str(last_task_number + 1)
    list_of_task[new_task_number] = new_task
    save_list_of_task(list_of_task)
    return list_of_task
