from Classes import Client
from Classes import Server

HOST = 0
PORT = 1

def main(*args):
    Client.client(args[HOST],args[PORT])
    server = Server.Server(args[PORT])


