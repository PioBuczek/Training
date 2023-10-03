import json
import socket as s

HOST = "192.168.0.115"
PORT = 33000
BUFFER = 1024

client_socket = s.socket(s.AF_INET, s.SOCK_STREAM)
client_socket.connect((HOST, PORT))

server_answer = ""


def authentication(client_socket):
    authenticated = False
    while not authenticated:
        print("Enter your username: ")
        client_socket.send(input().encode("utf8"))
        print("Enter your password: ")
        client_socket.send(input().encode("utf8"))
        response = client_socket.recv(BUFFER).decode("utf8")
        if response.startswith("Hi"):
            server_answer_authenticator = client_socket.recv(BUFFER).decode("utf8")
            print(server_answer_authenticator)
            authenticated = True
        else:
            print(response)


authentication(client_socket)

while True:
    client_request = input("Enter your command: ")
    client_socket.send(client_request.encode("utf8"))

    if client_request == "info":
        server_answer = client_socket.recv(BUFFER).decode("utf8")
        print(server_answer)

    elif client_request == "help_msg":
        server_answer = client_socket.recv(BUFFER).decode("utf8")
        print(server_answer)

    elif client_request == "uptime":
        server_answer = client_socket.recv(BUFFER).decode("utf8")
        print(server_answer)

    elif client_request == "stop":
        server_answer = client_socket.recv(BUFFER).decode("utf8")
        print(server_answer)

    elif client_request == "message":
        while True:
            print("Enter username: ")
            recipient = input()
            print("Enter your message: ")
            message_content = input()
            client_socket.send(recipient.encode("utf8"))
            client_socket.send(message_content.encode("utf8"))
            server_answer = client_socket.recv(BUFFER).decode("utf8")
            print(server_answer)
            break
