def add_new_tasks(new_task, list_of_task):
    if new_task not in list_of_task.values():
        number_task = max(list_of_task.keys(), default=0) + 1
        list_of_task[number_task] = new_task
    return list_of_task
