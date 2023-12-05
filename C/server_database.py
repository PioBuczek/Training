import json


def open_users():
    with open("database.json", "r") as file:
        data = json.load(file)
        return data.get("users", [])


users = open_users()
