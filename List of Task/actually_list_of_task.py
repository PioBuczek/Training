def list_of_task_(list_of_task):
    task_list = []
    for key, values in list_of_task.items():
        task_list.append(f"{key}:{values}")
    return task_list
