import socket as s
import json
import commands
from clients import Client


client = Client("192.168.0.115", 33000, 1024)


client_socket = s.socket(s.AF_INET, s.SOCK_STREAM)
client_socket.connect((client.HOST, client.PORT))


def authenticator():
    authenticate_user = False
    # username
    print(client_socket.recv(client.BUFFER).decode("utf8"))
    client_answer_about_username = input()
    client_socket.send(client_answer_about_username.encode("utf8"))

    # password
    print(client_socket.recv(client.BUFFER).decode("utf8"))
    client_answer_about_password = input()
    client_socket.send(client_answer_about_password.encode("utf8"))

    # auhenctiactor
    type_authenticator = client_socket.recv(client.BUFFER).decode("utf8")
    if type_authenticator.startswith("Hello"):
        authenticate_user = True
        print(type_authenticator)
        return authenticate_user


authenticate_user_type = authenticator()

if authenticate_user_type:
    while True:
        client_commands = input("Command: ").encode("utf8")
        if client_commands == "login":
            client_socket.send(client_commands)
            server_answer = client_socket.recv(client.BUFFER).decode("utf8")
            print(server_answer)
            if client_commands == "stop":
                client_socket.close()
                break
            else:
                client_socket.send(client_commands)
                server_answer = client_socket.recv(client.BUFFER).decode("utf8")
                print(server_answer)
