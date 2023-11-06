import socket as s
import json

HOST = "192.168.0.115"
PORT = 33000
BUFFER = 1024
client_socket = s.socket(s.AF_INET, s.SOCK_STREAM)
client_socket.connect((HOST, PORT))

while True:
    print("What you want")
    client_request = client_socket.send(json.dumps(input()).encode("utf8"))
    server_answer = json.loads(client_socket.recv(BUFFER).decode("utf8"))
    print(server_answer)
