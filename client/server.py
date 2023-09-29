import json
import socket as s
import datetime

HOST = "192.168.0.115"
PORT = 33000
BUFFER = 1024
uptime = datetime.datetime.now()
help_msg = "uptime - returns time of server activity\ninfo - returns version of the server and issue date\nhelp - returns list of commands\nstop - terminates connection\n"
info = "version 1.0.0, issue date 13.12.2022\n"
stop = "connection terminated\n"
possible_options = ["uptime", "help_msg", "info", "stop"]
authenticated_user = None

server_socket = s.socket(s.AF_INET, s.SOCK_STREAM)
server_socket.bind((HOST, PORT))
server_socket.listen(2)
client_socket, address = server_socket.accept()


def open_user():
    with open("database.json", "r") as file:
        data = json.load(file)
        return data.get("users", [])


users = open_user()


def authentication(client_socket):
    global authenticated_user
    while authenticated_user is None:
        user_request = client_socket.recv(BUFFER).decode("utf8")
        password_request = client_socket.recv(BUFFER).decode("utf8")

        for user in users:
            if (
                user["username"] == user_request
                and user["password"] == password_request
            ):
                authenticated_user = user
                break

        if authenticated_user:
            client_socket.send(f"Hi {user_request} !".encode("utf8"))
            return authenticated_user["type"]
        else:
            client_socket.send("Something is wrong, try again".encode("utf8"))


authenticated_user_type = authentication(client_socket)

if authenticated_user_type:
    if authenticated_user_type == "admin":
        user_type_message = "You are admin - can use all functions"
    elif authenticated_user_type == "user":
        user_type_message = "You are user - can use info and uptime functions"
    client_socket.send(
        f"You are connected as {authenticated_user_type}\n{user_type_message}".encode(
            "utf8"
        )
    )
    print(f"Client connected as {authenticated_user_type}")


def send_and_save_message(client_socket, sender, recipient, message_content):
    recipient_exist = False
    sender_exist = False
    for user in users:
        if user["username"] == sender and user["type"] == "user":
            sender_exist = True
        if user["username"] == recipient and user["type"] == "user":
            recipient_exist = True

    if recipient_exist and sender_exist:
        message = {"sender": sender, "recipient": recipient, "message": message_content}

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


server_answer = ""

while True:
    if authenticated_user_type == "admin":
        client_request = client_socket.recv(BUFFER).decode("utf8")
        if client_request == "info":
            server_answer = info
        elif client_request == "help_msg":
            server_answer = help_msg
        elif client_request == "uptime":
            server_answer = str(datetime.datetime.now() - uptime)
        elif client_request == "stop":
            client_socket.send(stop.encode("utf8"))
            client_socket.close()
            break

        client_socket.send(server_answer.encode("utf8"))

    elif authenticated_user_type == "user":
        client_request = client_socket.recv(BUFFER).decode("utf8")
        if client_request == "info":
            server_answer = info
        elif client_request == "message":
            while True:
                recipient = client_socket.recv(BUFFER).decode("utf8")
                message_content = client_socket.recv(BUFFER).decode("utf8")
                result = send_and_save_message(
                    client_socket,
                    authenticated_user["username"],
                    recipient,
                    message_content,
                )
                client_socket.send(result.encode("utf8"))
                break
        elif client_request == "help_msg":
            server_answer = "You are not admin, you cannot use this function"
        elif client_request == "uptime":
            server_answer = str(datetime.datetime.now() - uptime)
        elif client_request == "stop":
            server_answer = "You are not admin, you cannot use this function"

        client_socket.send(server_answer.encode("utf8"))

server_socket.close()
