from datetime import datetime


class Server:
    def __init__(self, HOST, PORT, BUFFER):
        self.HOST = "192.168.0.115"
        self.PORT = 33000
        self.BUFFER = 1024
        self.version = "0.1.0"

    def uptime(self):
        current_time = datetime.now()
        server_uptime = current_time - datetime.now()
        return server_uptime

    def info(self):
        number_version = {
            "version": self.version,
            "version date": datetime.now().strftime("%m/%d/%Y, %H:%M"),
        }
        return number_version
