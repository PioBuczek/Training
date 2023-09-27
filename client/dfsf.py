import json

with open("server\client\database.json", "r") as file:
    data = json.load(file)
    print(data)
    print(type(data))
    print("_________")
    private_message = data.get("users", [])
    print(private_message)
    print(type(private_message))
