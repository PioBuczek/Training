from quit import quit_program
from add_new_task import add_new_tasks
from actually_list_of_task import list_of_task_
from delete_task import task_to_delete
from database import save_list_of_task, load_list_of_task

list_of_task = load_list_of_task()


while True:
    new_task = input(
        "List of possible options:\n 1.Add new task \n 2.Delete task \n 3.List of actually tasks \n 4.Quit \n Press your number: "
    )

    if new_task == "1":
        new_task_description = input("Enter your task:")
        list_of_task = add_new_tasks(new_task_description, list_of_task)
        save_list_of_task(list_of_task)
        print("Task added successfully")
    elif new_task == "2":
        number_of_task = input("Enter number task to delete: ")
        list_of_task = load_list_of_task()
        result = task_to_delete(number_of_task, list_of_task)
        save_list_of_task(list_of_task)
        print(result)

    elif new_task == "3":
        task_list = list_of_task_(list_of_task)
        print(task_list)
    elif new_task == "4":
        print(quit_program())
        break
