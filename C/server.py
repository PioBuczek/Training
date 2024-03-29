import socket as s
import json
import commands
from functions import Server
from database_user import users


server = Server("192.168.0.115", 33000, 1024)


server_socket = s.socket(s.AF_INET, s.SOCK_STREAM)
server_socket.bind(("192.168.0.115", 33000))
server_socket.listen(2)
client_socket, address = server_socket.accept()


def authenticator():
    authenticate_user = None

    while authenticate_user is None:
        server_question_about_username = "Enter your username: "
        client_socket.send(server_question_about_username.encode("utf8"))
        client_answer_about_username = client_socket.recv(server.BUFFER).decode("utf8")

        server_question_about_password = "Enter your password: "
        client_socket.send(server_question_about_password.encode("utf8"))
        client_answer_about_password = client_socket.recv(server.BUFFER).decode("utf8")

        for user in server.users:
            if (
                client_answer_about_username == user.username
                and client_answer_about_password == user.password
            ):
                authenticate_user = user
                break

        if authenticate_user:
            client_socket.send(f"Hello {client_answer_about_username} ".encode("utf8"))
        else:
            print("Authentication failed.")
            client_socket.send("Authentication failed. Try again.".encode("utf8"))

    return authenticate_user["type"]


authenticate_user_type = authenticator()


while True:
    client_request = client_socket.recv(server.BUFFER).decode("utf8")
    if client_request == "login":
        authenticate_user_type = authenticator()

    if authenticate_user_type:
        possible_options_for_admin = ["uptime", "info", "help", "stop"]
        possible_options_for_user = ["uptime", "help"]

        if authenticate_user_type == "admin":
            if client_request in possible_options_for_admin:
                if client_request == "info":
                    server_answer = json.dumps(server.info(), indent=5)
                    client_socket.send(server_answer.encode("utf8"))
                elif client_request == "uptime":
                    server_answer = json.dumps(server.uptime(), indent=5)
                    client_socket.send(server_answer.encode("utf8"))
                elif client_request == "help":
                    server_answer = json.dumps(commands.commands_description, indent=5)
                    client_socket.send(server_answer.encode("utf8"))
                elif client_request == "stop":
                    server_answer = "The server has been stopped"
                    client_socket.send(server_answer.encode("utf8"))
                    server_socket.close()
                    break
            else:
                error_message = "Invalid option. Please choose from: " + ", ".join(
                    possible_options_for_admin
                )
                client_socket.send(error_message.encode("utf8"))

        elif authenticate_user_type == "user":
            if client_request in possible_options_for_user:
                if client_request == "info":
                    server_answer = "You are not admin, you can't use this function."
                    client_socket.send(server_answer.encode("utf8"))
                elif client_request == "uptime":
                    server_answer = json.dumps(server.uptime(), indent=5)
                    client_socket.send(server_answer.encode("utf8"))
                elif client_request == "help":
                    server_answer = json.dumps(commands.commands_description, indent=5)
                    client_socket.send(server_answer.encode("utf8"))
                elif client_request == "stop":
                    server_answer = "You are not admin, you can't use this function."
                    client_socket.send(server_answer.encode("utf8"))
            else:
                error_message = "Invalid option. Please choose from: " + ", ".join(
                    possible_options_for_user
                )
                client_socket.send(error_message.encode("utf8"))
