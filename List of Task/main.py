from quit import quit_program
from add_new_task import add_new_tasks

list_of_task = {}

while True:
    new_task = input(
        "List of possible options:\n 1.Add new task \n 2.Delete task \n 3.List of actually tasks \n 4.Quit \n Press your number: "
    )

    if new_task == "1":
        new_task_description = input("Enter your task:")
        list_of_task = add_new_tasks(new_task_description, list_of_task)
        print("Task added successfully")
    elif new_task == "4":
        print(quit_program())
        break
    result = add_new_tasks(new_task, list_of_task)
    print(result)
