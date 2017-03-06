from Classes import Client
from Classes import Server
from Classes import Thread_manager as TM

import  sys

HOST = sys.argv[1]
PORT = sys.argv[2]

def main(*args):
    #server = Server.Server(PORT)
    TM.Thread_manager(Server.Server,(PORT))
    #Client.client(HOST,PORT).receip()

main(sys.argv)

