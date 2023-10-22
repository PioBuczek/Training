import json


def save_list_of_task(list_of_task):
    with open("list_of_task.json", "w") as file:
        json.dump(list_of_task, file)


def load_list_of_task():
    try:
        with open("list_of_task.json", "r") as file:
            data = json.load(file)
            return data
    except FileNotFoundError:
        return {}
