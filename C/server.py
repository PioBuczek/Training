import json
import socket as s
import commands

HOST = "192.168.0.115"
PORT = 33000
BUFFER = 1024


server_socket = s.socket(s.AF_INET, s.SOCK_STREAM)
server_socket.bind((HOST, PORT))
server_socket.listen(2)
client_socket, address = server_socket.accept()

while True:
    command_list = ["uptime", "info", "help", "stop"]
    server_request = "What you want: "
    client_socket.send(server_request.encode("utf8"))
    client_answer = client_socket.recv(BUFFER).decode("utf8")
    if client_answer in command_list:
        if client_answer == "info":
            server_answer = commands.commands_description
            client_socket.send(server_answer.encode("utf8"))
