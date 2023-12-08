import json
import socket as s


HOST = "192.168.0.115"
PORT = 33000
BUFFER = 1024

client_socket = s.socket(s.AF_INET, s.SOCK_STREAM)
client_socket.connect((HOST, PORT))

while True:
    client_answer = input("Command: ")
    client_socket.send(client_answer.encode("utf8"))
    server_answer = client_socket.recv(BUFFER).decode("utf8")
    print(server_answer)
