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
#     authenticated_user = None
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
#     client_socket.send(f"You are connected as {authenticated_user_type}".encode("utf8"))
#     print(f"You are connected as {authenticated_user_type}")
#     client_socket.send("Enter your command".encode("utf8"))
# server_answer = ""

# # ...
# while True:
#     print("Waiting for a connection...")
#     client_socket, address = server_socket.accept()
#     print(f"Call received from {address[0]}:{address[1]}")

#     authenticated_user_type = authentication(client_socket)

#     if authenticated_user_type:
#         client_socket.send(
#             f"You are connected as {authenticated_user_type}".encode("utf8")
#         )
#         print(f"You are connected as {authenticated_user_type}")
#         client_socket.send("Enter your command".encode("utf8"))

#     while True:
#         client_request = client_socket.recv(BUFFER).decode("utf8")
#         if client_request == "info":
#             server_answer = info
#         elif client_request == "help_msg":
#             server_answer = help_msg
#         elif client_request == "uptime":
#             server_answer = str(datetime.datetime.now() - uptime)
#         elif client_request == "stop":
#             client_socket.send(stop.encode("utf8"))
#             client_socket.close()
#             break

#         client_socket.send(server_answer.encode("utf8"))
#      client_socket.close()
#     print(f"Connection with {address[0]}:{address[1]} closed")
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
    authenticated_user = None
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
    client_socket.send(f"You are connected as {authenticated_user_type}".encode("utf8"))
    print(f"You are connected as {authenticated_user_type}")

while True:
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
