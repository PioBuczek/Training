from datetime import datetime
from database_user import users


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
