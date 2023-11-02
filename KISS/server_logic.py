import json
import psycopg2
import socket
import datetime
from server_db import open_user


class Server:
    def __init__(self, host, port):
        self.HOST = host
        self.PORT = port
        self.BUFFER = 1024
        self.uptime = datetime.datetime.now()
        self.help_msg = "uptime - returns time of server activity\ninfo - returns version of the server and issue date\nhelp - returns list of commands\nstop - terminates connection\n"
        self.info = "version 1.0.0, issue date 13.12.2022\n"
        self.stop = "connection terminated\n"
        self.possible_options = ["uptime", "help_msg", "info", "stop"]
        self.authenticated_user = None
        self.users = open_user()
        self.address = None

    # def authentication(self):
    #     try:
    #         while self.authenticated_user is None:
    #             user_request = self.client_socket.recv(self.BUFFER).decode("utf8")
    #             password_request = self.client_socket.recv(self.BUFFER).decode("utf8")

    #             for user in self.users:
    #                 if (
    #                     user["username"] == user_request
    #                     and user["password"] == password_request
    #                 ):
    #                     self.authenticated_user = user
    #                     break

    #             if self.authenticated_user:
    #                 self.client_socket.send(f"Hi {user_request} !".encode("utf8"))
    #                 return self.authenticated_user["type"]
    #             else:
    #                 self.client_socket.send(
    #                     "Something is wrong, try again".encode("utf8")
    #                 )
    #     except Exception as e:
    #         print(f"An error occurred during authentication: {str(e)}")

    def send_and_save_message(sender, recipient, message_content):
        recipient_exist = False
        sender_exist = False
        for user in open_user():
            if user["username"] == sender and user["type"] == "user":
                sender_exist = True
            if user["username"] == recipient and user["type"] == "user":
                recipient_exist = True

        if recipient_exist and sender_exist:
            message = {
                "sender": sender,
                "recipient": recipient,
                "message": message_content,
            }

            with open("private_message.json", "r") as file:
                data = json.load(file)

            private_messages = data.get("private_message", [])

            if len(private_messages) >= 5:
                return "Inbox is full"

            private_messages.append(message)

            data["private_message"] = private_messages

            with open("private_message.json", "w") as file:
                json.dump(data, file)

            return "Message sent successfully"
        else:
            return "Sender or recipient doesn't exist"

    # # def run(self):
    # #     print("Hi")
    # #     try:
    # #         self.authenticated_user_type = self.authentication()

    #         if self.authenticated_user_type:
    #             if self.authenticated_user_type == "admin":
    #                 user_type_message = "You are admin - can use all functions"
    #             elif self.authenticated_user_type == "user":
    #                 user_type_message = (
    #                     "You are user - can use info, message, and uptime functions"
    #                 )
    #             self.client_socket.send(
    #                 f"You are connected as {self.authenticated_user_type}\n{user_type_message}".encode(
    #                     "utf8"
    #                 )
    #             )
    #             print(f"Client connected as {self.authenticated_user_type}")
    #             print(f"Hello {self.address[0]}: {self.address[1]}")
    #         server_answer = ""
    #     except Exception as e:
    #         print(f"An error occurred: {str(e)}")
