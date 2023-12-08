import json
import socket as s
import commands
from functions import Server

server = Server("192.168.0.115", 33000, 1024)

server_socket = s.socket(s.AF_INET, s.SOCK_STREAM)
server_socket.bind((server.HOST, server.PORT))
server_socket.listen(2)
client_socket, address = server_socket.accept()


while True:
    print(f"Connection with client {address[0]} : {address[1]}")

    command_list = ["uptime", "info", "help", "stop"]

    client_answer = client_socket.recv(server.BUFFER).decode("utf8")

    if client_answer in command_list:
        if client_answer == "help":
            server_answer = json.dumps(commands.commands_description)
            client_socket.send(server_answer.encode("utf8"))
        elif client_answer == "info":
            server_answer = json.dumps(server.info())
            client_socket.send(server_answer.encode("utf8"))
