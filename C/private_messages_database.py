import json


def private_message():
    try:
        with open("private_message.json", "r") as file:
            data = json.load(file)
            return data.get("private_message", [])
    except json.decoder.JSONDecodeError:
        return []


private_messages = private_message()


def private_message_save_new_messages():
    with open("private_message.json", "w") as file:
        json.dump(
            {"private_message": private_messages}, file, indent=2
        )  # Dodaj indent=2 dla czytelności


private_message_save_new_messages()
