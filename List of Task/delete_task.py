import json


def save_list_of_task(list_of_task):
    with open("list_of_task.json", "w") as file:
        json.dump(list_of_task, file)


def task_to_delete(number_of_task, list_of_task):
    if number_of_task in list_of_task:
        del list_of_task[number_of_task]
        save_list_of_task(list_of_task)
    else:
        return "Don't have this number"
    return None
