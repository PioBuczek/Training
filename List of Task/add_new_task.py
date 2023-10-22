def add_new_tasks(new_task, list_of_task):
    list_of_task_len = len(list_of_task)
    list_of_task[list_of_task_len + 1] = new_task
    return list_of_task
