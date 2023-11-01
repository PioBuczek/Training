import json


def open_user():
    with open("database.json", "r") as file:
        data = json.load(file)
        return data.get("users", [])
