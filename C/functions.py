import datetime


class Server:
    def __init__(self, HOST, PORT, BUFFER):
        self.HOST = "192.168.0.115"
        self.PORT = 33000
        self.BUFFER = 1024
        self.version = "0.1.0"
        self.uptime = datetime.datetime.now()

    def current_time(self):
        server_time = str(datetime.datetime.now() - self.uptime)
        return server_time

    def info(self):
        number_version = {
            "version": self.version,
            "version date": datetime.datetime.now().strftime("%m/%d/%Y, %H:%M"),
        }
        return number_version
