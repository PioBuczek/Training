database = []


def add_task():
    add = input("Add your task: ")
    if add not in database:
        return database.append(add)


task = add_task()
print(database)
