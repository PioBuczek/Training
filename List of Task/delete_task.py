import json


def load_list_of_task():
    with open("list_of_task.json", "r") as file:
        data = json.load(file)
        return data


def task_to_delete(number_of_task, list_of_task):
    if number_of_task in list_of_task:
        del list_of_task[number_of_task]
        return list_of_task
    else:
        return "Don't have this number"
