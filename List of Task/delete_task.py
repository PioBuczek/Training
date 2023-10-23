from database import save_list_of_task


def task_to_delete(number_of_task, list_of_task):
    if number_of_task in list_of_task:
        del list_of_task[number_of_task]
        save_list_of_task(list_of_task)
        return "Task deleted successfully"
    else:
        return "Don't have this number"
