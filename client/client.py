import json
import socket as s

HOST = "192.168.0.115"
PORT = 33000
BUFFER = 1024

client_socket = s.socket(s.AF_INET, s.SOCK_STREAM)
client_socket.connect((HOST, PORT))


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
    client_socket.send(input("Enter your command: ").encode("utf8"))
    server_answer = client_socket.recv(BUFFER).decode("utf8")
    print(server_answer)
