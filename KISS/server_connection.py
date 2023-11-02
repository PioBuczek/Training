import json
import psycopg2
import socket
import datetime
from server_logic import Server
from server_db import open_user

server = Server("192.168.0.115", 33000)

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind((server.HOST, server.PORT))
server_socket.listen(2)
client_socket, server.address = server_socket.accept()
users = open_user()


def authentication():
    try:
        global authenticated_user
        while authenticated_user is None:
            print("login")
            user_request = client_socket.recv(server.BUFFER).decode("utf8")
            print("password")
            password_request = client_socket.recv(server.BUFFER).decode("utf8")

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
    except Exception as e:
        print(f"An error occurred during authentication: {str(e)}")


def run():
    print("Hi")
    try:
        authenticated_user_type = authentication()

        if authenticated_user_type:
            if authenticated_user_type == "admin":
                user_type_message = "You are admin - can use all functions"
            elif authenticated_user_type == "user":
                user_type_message = (
                    "You are user - can use info, message, and uptime functions"
                )
            client_socket.send(
                f"You are connected as {authenticated_user_type}\n{user_type_message}".encode(
                    "utf8"
                )
            )
            print(f"Client connected as {authenticated_user_type}")
            print(f"Hello {address[0]}: {address[1]}")
        server_answer = ""
    except Exception as e:
        print(f"An error occurred: {str(e)}")


authenticated_user_type = True

print("Hi!")
while True:
    if authenticated_user_type == "admin":
        client_request = client_socket.recv(server.BUFFER).decode("utf8")
        if client_request == "info":
            server_answer = server.info
        elif client_request == "help_msg":
            server_answer = server.help_msg
        elif client_request == "message":
            server_answer = "You are not user"
        elif client_request == "uptime":
            server_answer = str(datetime.datetime.now() - server.uptime)
        elif client_request == "stop":
            client_socket.send(server.stop.encode("utf8"))
            client_socket.close()
            break

        client_socket.send(server_answer.encode("utf8"))

    elif authenticated_user_type == "user":
        client_request = client_socket.recv(server.BUFFER).decode("utf8")
        if client_request == "info":
            server_answer = server.info
        elif client_request == "message":
            recipient = client_socket.recv(server.BUFFER).decode("utf8")
            message_content = client_socket.recv(server.BUFFER).decode("utf8")
            result = server.send_and_save_message(
                server.authenticated_user["username"],
                recipient,
                message_content,
            )
            client_socket.send(result.encode("utf8"))
            continue
        elif client_request == "help_msg":
            server_answer = "You are not admin, you cannot use this function"
        elif client_request == "uptime":
            server_answer = str(datetime.datetime.now() - server.uptime)
        elif client_request == "stop":
            server_answer = "You are not admin, you cannot use this function"

        client_socket.send(server_answer.encode("utf8"))

server_socket.close()
