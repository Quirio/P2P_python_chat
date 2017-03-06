import os

class Orchestador:
    def __init__(self,server_pid,client_pid,host):
        self.server_pid = server_pid
        self.client_pid = client_pid
        self.host = host

    def check_pid(self):
        try:
           os.kill(self.pid, 0)
        except OSError:
            return False
        else:
            return True

    def check_host(self):
        try:
