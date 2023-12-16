import socket as s
import json
import commands
from functions import Server


server = Server("192.168.0.115", 33000, 1024)


server_socket = s.socket(s.AF_INET, s.SOCK_STREAM)
server_socket.bind(("192.168.0.115", 33000))
server_socket.listen(2)
client_socket, address = server_socket.accept()

while True:
    print(f"You are connected with {address[0]} : {address[1]}")

    possible_options = ["uptime", "info", "help", "close"]
    client_request = client_socket.recv(server.BUFFER).decode("utf8")

    if client_request in possible_options:
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
            possible_options
        )
        client_socket.send(error_message.encode("utf8"))
