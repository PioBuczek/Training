import socket as s
import json
import datetime
from server_database import users
from message import send_and_save_message

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


def authentication():
    server_request_about_username = "Enter your username: "
    client_socket.send(server_request_about_username.encode("utf8"))
    client_answer_about_username = client_socket.recv(BUFFER).decode("utf8")

    server_request_about_password = "Enter your password: "
    client_socket.send(server_request_about_password.encode("utf8"))
    client_answer_about_password = client_socket.recv(BUFFER).decode("utf8")

    authenticate_user = None
    for user in users:
        if (
            user["username"] == client_answer_about_username
            and user["password"] == client_answer_about_password
        ):
            authenticate_user = user
            break

    if authenticate_user:
        welcome_client = f"Hi {client_answer_about_username}"
        client_socket.send(welcome_client.encode("utf8"))
        return authenticate_user["type"]
    else:
        client_socket.close()
        server_socket.close()
        raise SystemExit


authenticate_user_type = authentication()


server_inform_client_about_type = f"You are connect as {authenticate_user_type} \n"
client_socket.send(server_inform_client_about_type.encode("utf8"))


while True:
    server_request_about_command = "Enter your command: "
    client_socket.send(server_request_about_command.encode("utf8"))

    client_answer_about_command = client_socket.recv(BUFFER).decode("utf8")
    server_answer = ""
    if client_answer_about_command == "info":
        server_answer = info

    elif client_answer_about_command == "message":
        recipient = client_socket.recv(BUFFER).decode("utf8")
        message = client_socket.recv(BUFFER).decode("utf8")

        result = send_and_save_message(authenticate_user_type, recipient, message)
        server_answer = result
        client_socket.send(server_answer.encode("utf8"))
        client_socket.send("Enter your command:".encode("utf8"))
        continue
    client_socket.send(server_answer.encode("utf8"))
