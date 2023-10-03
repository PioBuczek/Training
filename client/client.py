import json
import socket


class Client:
    def __init__(self, host, port):
        self.HOST = host
        self.PORT = port
        self.BUFFER = 1024
        self.client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server_answer = ""

    def authentication(self):
        authenticated = False
        while not authenticated:
            print("Enter your username: ")
            self.client_socket.send(input().encode("utf8"))
            print("Enter your password: ")
            self.client_socket.send(input().encode("utf8"))
            response = self.client_socket.recv(self.BUFFER).decode("utf8")
            if response.startswith("Hi"):
                server_answer_authenticator = self.client_socket.recv(
                    self.BUFFER
                ).decode("utf8")
                print(server_answer_authenticator)
                authenticated = True
            else:
                print(response)

    def run(self):
        self.client_socket.connect((self.HOST, self.PORT))
        self.authentication()

        while True:
            client_request = input("Enter your command: ")
            self.client_socket.send(client_request.encode("utf8"))

            if (
                client_request == "info"
                or client_request == "uptime"
                or client_request == "stop"
            ):
                self.server_answer = self.client_socket.recv(self.BUFFER).decode("utf8")
                print(self.server_answer)

            elif client_request == "help_msg":
                self.server_answer = self.client_socket.recv(self.BUFFER).decode("utf8")
                print(self.server_answer)

            elif client_request == "message":
                while True:
                    print("Enter username: ")
                    recipient = input()
                    print("Enter your message: ")
                    message_content = input()
                    self.client_socket.send(recipient.encode("utf8"))
                    self.client_socket.send(message_content.encode("utf8"))
                    self.server_answer = self.client_socket.recv(self.BUFFER).decode(
                        "utf8"
                    )
                    print(self.server_answer)
                    break


if __name__ == "__main__":
    client = Client("192.168.0.115", 33001)
    client.run()
