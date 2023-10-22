from quit import quit_program

list_of_task = {}


def add_new_task(new_task):
    if new_task not in list_of_task.values():
        number_task = max(list_of_task.keys(), default=0) + 1
        list_of_task[number_task] = new_task
    return list_of_task


while True:
    new_task = input(
        "List of possible options:\n 1.Add new task \n 2.Delete task \n 3.List of actually tasks \n 4.Quit \n Press your number: "
    )
    if new_task == "4":
        print(quit_program())
        break

    result = add_new_task(new_task)
    print(result)
