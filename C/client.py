import socket as s
import json
import commands
from clients import Client


client = Client("192.168.0.115", 33000, 1024)


client_socket = s.socket(s.AF_INET, s.SOCK_STREAM)
client_socket.connect((client.HOST, client.PORT))

while True:
    client_commands = input("Command: ").encode("utf8")
    if client_commands == "stop":
        client_socket.close()
        break
    else:
        client_socket.send(client_commands)
        server_answer = client_socket.recv(client.BUFFER).decode("utf8")
        print(server_answer)
