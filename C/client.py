import socket as s

HOST = "192.168.0.115"
PORT = 33000
BUFFER = 1024

client_socket = s.socket(s.AF_INET, s.SOCK_STREAM)
client_socket.connect((HOST, PORT))


def authentication():
    server_request_about_username = client_socket.recv(BUFFER).decode("utf8")
    print(server_request_about_username)
    client_answer_about_username = input()
    client_socket.send(client_answer_about_username.encode("utf8"))

    server_request_about_password = client_socket.recv(BUFFER).decode("utf8")
    print(server_request_about_password)
    client_answer_about_password = input()
    client_socket.send(client_answer_about_password.encode("utf8"))

    server_answer_about_welcome_client = client_socket.recv(BUFFER).decode("utf8")
    if server_answer_about_welcome_client.startswith("Hi "):
        return server_answer_about_welcome_client
    else:
        return None


authenticate_user_type = authentication()
server_inform_client_about_type = client_socket.recv(BUFFER).decode("utf8")
print(server_inform_client_about_type)

if authenticate_user_type:
    while True:
        # Enter your command
        server_request_about_command = client_socket.recv(BUFFER).decode("utf8")
        print(server_request_about_command)
        # Enter your command
        client_answer_about_command = input()

        if client_answer_about_command == "info":
            client_socket.send(client_answer_about_command.encode("utf8"))
            server_answer_about_info = client_socket.recv(BUFFER).decode("utf8")
            print(server_answer_about_info)

        elif client_answer_about_command == "message":
            while True:
                print("Enter your recipient:")
                client_answer_about_recipient = input()
                client_socket.send(client_answer_about_recipient.encode("utf8"))
                print("Enter your message:")
                client_answer_about_message = input()
                client_socket.send(client_answer_about_message.encode("utf8"))
                server_answer = client_socket.recv(BUFFER).decode("utf8")
                print(server_answer)
                client_socket.recv(BUFFER).decode("utf8")
                break
