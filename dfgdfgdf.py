import json
import psycopg2
import socket
import datetime
from server_logic import Server

server = Server("192.168.0.115", 33000)

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind((server.HOST, server.PORT))
server_socket.listen(2)
client_socket, server.address = server_socket.accept()

authenticated_user_type = True

while True:
    if authenticated_user_type == "admin":
        client_request = client_socket.recv(server.BUFFER).decode("utf8")
        if client_request == "info":
            server_answer = server.info
        elif client_request == "help_msg":
            server_answer = server.help_msg
        elif client_request == "message":
            server_answer = "You are not user"
        elif client_request == "uptime":
            server_answer = str(datetime.datetime.now() - server.uptime)
        elif client_request == "stop":
            client_socket.send(server.stop.encode("utf8"))
            client_socket.close()
            break

        server_socket.send(server_answer.encode("utf8"))

    elif authenticated_user_type == "user":
        client_request = client_socket.recv(server.BUFFER).decode("utf8")
        if client_request == "info":
            server_answer = server.info
        elif client_request == "message":
            recipient = client_socket.recv(server.BUFFER).decode("utf8")
            message_content = client_socket.recv(server.BUFFER).decode("utf8")
            result = server.send_and_save_message(
                server.authenticated_user["username"],
                recipient,
                message_content,
            )
            client_socket.send(result.encode("utf8"))
            continue
        elif client_request == "help_msg":
            server_answer = "You are not admin, you cannot use this function"
        elif client_request == "uptime":
            server_answer = str(datetime.datetime.now() - server.uptime)
        elif client_request == "stop":
            server_answer = "You are not admin, you cannot use this function"

        client_socket.send(server_answer.encode("utf8"))

server_socket.close()
