import json
from server_database import users
from private_messages_database import (
    private_messages,
    private_message_save_new_messages,
)


def send_and_save_message(sender, recipient, message):
    sender_exists = False
    recipient_exists = False
    for user in users:
        if user["username"] == sender and user["type"] == "user":
            sender_exists = True
        if user["username"] == recipient and user["type"] == "user":
            recipient_exists = True
    if sender_exists and recipient_exists:
        new_message = {
            "sender": sender,
            "recipient": recipient,
            "message_content": message,
        }

        private_messages.append(new_message)

        if len(private_messages) >= 2:
            return "Inbox is full"

        print("Before save:", private_messages)
        private_message_save_new_messages()
        print("After save:", private_messages)

        return "Message sent successfully"
    else:
        return "Sender or recipient doesn't exist"
