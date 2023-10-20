list_of_task = {}


def add_new_task(new_task):
    if new_task not in list_of_task.values():
        number_task = max(list_of_task.keys(), default=0) + 1
        list_of_task[number_task] = new_task
    return list_of_task


while True:
    new_task = input("Enter your task, or press 'q' if you want exit: ")
    if new_task == "q":
        break

    result = add_new_task(new_task)
    print(result)


def delete_task():
    pass
