import socket as s
import json
import database

HOST = "192.168.0.115"
PORT = 33000
BUFFER = 1024
info = "xD"

server_socket = s.socket(s.AF_INET, s.SOCK_STREAM)
server_socket.bind((HOST, PORT))
server_socket.listen(2)
client_socket, address = server_socket.accept()


def open_users():
    with open("database.json", "r") as file:
        data = json.load(file)
        return data.get("users", [])


users = open_users()


def authentication():
    server_question_username = "Enter your username: "
    client_socket.send(server_question_username.encode("utf8"))
    client_socket.recv(BUFFER).decode("utf8")
    server_question_password = "Enter your password: "
    client_socket.send(server_question_password.encode("utf8"))
    client_socket.recv(BUFFER).decode("utf8")
    authenticate_user = None
    for user in users:
        if (
            user["username"] == server_question_username
            and user["password"] == server_question_password
        ):
            return authenticate_user == user
        else:
            return "This user doesn't exist"

    if authenticate_user:
        hello_user = f"Hi {server_question_username}"
        client_socket.send(hello_user.encode("utf8"))
        return authenticate_user["type"]


while True:
    print("You are connect")
    client_request = json.loads(client_socket.recv(BUFFER).decode("utf8"))
    if client_request == "info":
        server_answer = info
    client_socket.send(json.dumps(server_answer).encode("utf8"))
