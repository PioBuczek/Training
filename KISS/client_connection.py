import json
import socket
from client_logic import Client

client = Client("192.168.0.115", 33000, 1024)
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect((client.HOST, client.PORT))


def authentication(client_socket):
    try:
        authenticated = False
        while not authenticated:
            print("Enter your username: ")
            username = input()
            print("Enter your password: ")
            password = input()
            client_socket.send(username.encode("utf8"))
            client_socket.send(password.encode("utf8"))
            response = client_socket.recv(client.BUFFER).decode("utf8")
            if response.startswith("Hi"):
                server_answer_authenticator = client_socket.recv(client.BUFFER).decode(
                    "utf8"
                )
                print(server_answer_authenticator)
                authenticated = True
            else:
                print(response)
    except Exception as e:
        print(f"An error occurred during authentication: {str(e)}")


def run(client_socket):
    try:
        authentication(client_socket)

        while True:
            client_request = input("Enter your command: ")
            client_socket.send(client_request.encode("utf8"))

            if (
                client_request == "info"
                or client_request == "uptime"
                or client_request == "stop"
                or client_request == "help_msg"
            ):
                client.server_answer = client_socket.recv(client.BUFFER).decode("utf8")
                print(client.server_answer)

            elif client_request == "message":
                print("Enter username: ")
                recipient = input()
                print("Enter your message: ")
                message_content = input()
                client_socket.send(recipient.encode("utf8"))
                client_socket.send(message_content.encode("utf8"))
                client.server_answer = client_socket.recv(client.BUFFER).decode("utf8")
                print(client.server_answer)
    except Exception as e:
        print(f"An error occurred: {str(e)}")


if __name__ == "__main__":
    run(client_socket)
