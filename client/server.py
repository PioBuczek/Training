import json
import socket
import datetime


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
        self.users = self.open_user()
        self.server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server_socket.bind((self.HOST, self.PORT))
        self.server_socket.listen(2)
        self.client_socket, self.address = self.server_socket.accept()

    def open_user(self):
        with open("database.json", "r") as file:
            data = json.load(file)
            return data.get("users", [])

    def authentication(self):
        while self.authenticated_user is None:
            user_request = self.client_socket.recv(self.BUFFER).decode("utf8")
            password_request = self.client_socket.recv(self.BUFFER).decode("utf8")

            for user in self.users:
                if (
                    user["username"] == user_request
                    and user["password"] == password_request
                ):
                    self.authenticated_user = user
                    break

            if self.authenticated_user:
                self.client_socket.send(f"Hi {user_request} !".encode("utf8"))
                return self.authenticated_user["type"]
            else:
                self.client_socket.send("Something is wrong, try again".encode("utf8"))

    def send_and_save_message(self, sender, recipient, message_content):
        recipient_exist = False
        sender_exist = False
        for user in self.users:
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

            if len(private_messages) >= 2:
                return "Inbox is full"

            private_messages.append(message)

            data["private_message"] = private_messages

            with open("private_message.json", "w") as file:
                json.dump(data, file)

            return "Message sent successfully"
        else:
            return "Sender or recipient doesn't exist"

    def run(self):
        authenticated_user_type = self.authentication()

        if authenticated_user_type:
            if authenticated_user_type == "admin":
                user_type_message = "You are admin - can use all functions"
            elif authenticated_user_type == "user":
                user_type_message = "You are user - can use info and uptime functions"
            self.client_socket.send(
                f"You are connected as {authenticated_user_type}\n{user_type_message}".encode(
                    "utf8"
                )
            )
            print(f"Client connected as {authenticated_user_type}")

        server_answer = ""

        while True:
            if authenticated_user_type == "admin":
                client_request = self.client_socket.recv(self.BUFFER).decode("utf8")
                if client_request == "info":
                    server_answer = self.info
                elif client_request == "help_msg":
                    server_answer = self.help_msg
                elif client_request == "message":
                    server_answer = "You are not user"
                elif client_request == "uptime":
                    server_answer = str(datetime.datetime.now() - self.uptime)
                elif client_request == "stop":
                    self.client_socket.send(self.stop.encode("utf8"))
                    self.client_socket.close()
                    break

                self.client_socket.send(server_answer.encode("utf8"))

            elif authenticated_user_type == "user":
                client_request = self.client_socket.recv(self.BUFFER).decode("utf8")
                if client_request == "info":
                    server_answer = self.info
                elif client_request == "message":
                    recipient = self.client_socket.recv(self.BUFFER).decode("utf8")
                    message_content = self.client_socket.recv(self.BUFFER).decode(
                        "utf8"
                    )
                    result = self.send_and_save_message(
                        self.authenticated_user["username"],
                        recipient,
                        message_content,
                    )
                    self.client_socket.send(result.encode("utf8"))
                    continue
                elif client_request == "help_msg":
                    server_answer = "You are not admin, you cannot use this function"
                elif client_request == "uptime":
                    server_answer = str(datetime.datetime.now() - self.uptime)
                elif client_request == "stop":
                    server_answer = "You are not admin, you cannot use this function"

                self.client_socket.send(server_answer.encode("utf8"))

        self.server_socket.close()


if __name__ == "__main__":
    server = Server("192.168.0.115", 33000)
    server.run()


# import json
# import socket as s
# import datetime

# HOST = "192.168.0.115"
# PORT = 33000
# BUFFER = 1024
# uptime = datetime.datetime.now()
# help_msg = "uptime - returns time of server activity\ninfo - returns version of the server and issue date\nhelp - returns list of commands\nstop - terminates connection\n"
# info = "version 1.0.0, issue date 13.12.2022\n"
# stop = "connection terminated\n"
# possible_options = ["uptime", "help_msg", "info", "stop"]
# authenticated_user = None

# server_socket = s.socket(s.AF_INET, s.SOCK_STREAM)
# server_socket.bind((HOST, PORT))
# server_socket.listen(2)
# client_socket, address = server_socket.accept()


# def open_user():
#     with open("database.json", "r") as file:
#         data = json.load(file)
#         return data.get("users", [])


# users = open_user()


# def authentication(client_socket):
#     global authenticated_user
#     while authenticated_user is None:
#         user_request = client_socket.recv(BUFFER).decode("utf8")
#         password_request = client_socket.recv(BUFFER).decode("utf8")

#         for user in users:
#             if (
#                 user["username"] == user_request
#                 and user["password"] == password_request
#             ):
#                 authenticated_user = user
#                 break

#         if authenticated_user:
#             client_socket.send(f"Hi {user_request} !".encode("utf8"))
#             return authenticated_user["type"]
#         else:
#             client_socket.send("Something is wrong, try again".encode("utf8"))


# authenticated_user_type = authentication(client_socket)

# if authenticated_user_type:
#     if authenticated_user_type == "admin":
#         user_type_message = "You are admin - can use all functions"
#     elif authenticated_user_type == "user":
#         user_type_message = "You are user - can use info and uptime functions"
#     client_socket.send(
#         f"You are connected as {authenticated_user_type}\n{user_type_message}".encode(
#             "utf8"
#         )
#     )
#     print(f"Client connected as {authenticated_user_type}")


# def send_and_save_message(client_socket, sender, recipient, message_content):
#     recipient_exist = False
#     sender_exist = False
#     for user in users:
#         if user["username"] == sender and user["type"] == "user":
#             sender_exist = True
#         if user["username"] == recipient and user["type"] == "user":
#             recipient_exist = True

#     if recipient_exist and sender_exist:
#         message = {"sender": sender, "recipient": recipient, "message": message_content}

#         with open("private_message.json", "r") as file:
#             data = json.load(file)

#         private_messages = data.get("private_message", [])

#         if len(private_messages) >= 2:
#             return "Inbox is full"

#         private_messages.append(message)

#         data["private_message"] = private_messages

#         with open("private_message.json", "w") as file:
#             json.dump(data, file)

#         return "Message sent successfully"
#     else:
#         return "Sender or recipient doesn't exist"


# server_answer = ""

# while True:
#     if authenticated_user_type == "admin":
#         client_request = client_socket.recv(BUFFER).decode("utf8")
#         if client_request == "info":
#             server_answer = info
#         elif client_request == "help_msg":
#             server_answer = help_msg
#         elif client_request == "message":
#             server_answer = "You are not user"
#         elif client_request == "uptime":
#             server_answer = str(datetime.datetime.now() - uptime)
#         elif client_request == "stop":
#             client_socket.send(stop.encode("utf8"))
#             client_socket.close()
#             break

#         client_socket.send(server_answer.encode("utf8"))

#     elif authenticated_user_type == "user":
#         client_request = client_socket.recv(BUFFER).decode("utf8")
#         if client_request == "info":
#             server_answer = info
#         elif client_request == "message":
#             recipient = client_socket.recv(BUFFER).decode("utf8")
#             message_content = client_socket.recv(BUFFER).decode("utf8")
#             result = send_and_save_message(
#                 client_socket,
#                 authenticated_user["username"],
#                 recipient,
#                 message_content,
#             )
#             client_socket.send(result.encode("utf8"))
#             continue
#         elif client_request == "help_msg":
#             server_answer = "You are not admin, you cannot use this function"
#         elif client_request == "uptime":
#             server_answer = str(datetime.datetime.now() - uptime)
#         elif client_request == "stop":
#             server_answer = "You are not admin, you cannot use this function"

#         client_socket.send(server_answer.encode("utf8"))

# server_socket.close()
