from datetime import datetime
from database_user import users
from users_config import User
import random
import string


class Server:
    def __init__(self, HOST, PORT, BUFFER):
        self.HOST = "192.168.0.115"
        self.PORT = 33000
        self.BUFFER = 1024
        self.creation_time = datetime.now()
        self.version = "Version 0.1.0"
        self.authenticate_user = None

    def uptime(self):
        current_time = datetime.now()
        server_uptime = current_time - self.creation_time
        server_time = {"server_time": str(server_uptime)}
        return server_time

    def info(self):
        version = {
            "Version": self.version,
            "Version_date": datetime.now().strftime("%m/%d/%Y, %H:%M"),
        }
        return version

    def list_of_users(self):
        self.users = {}

    def add_user(self, username):
        if self.get_users():
            print("Choose another nickname.")
        else:
            password = self.generate_password()
            user_data = {"username": username, "password": password}
            self.users[username] = user_data
            print(f"Użytkownik {username} został dodany. Hasło: {password}")

    def get_users(self, username):
        return self.users.get(username, None)

    def generate_password(self):
        characters = string.ascii_letters + string.digits + string.punctuation
        password = "".join(random.choice(characters) for x in range(12))
        return password
