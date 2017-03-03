from Classes import Client
from Classes import Server
from Classes import Thread_manager as TM

import  sys

HOST = sys.argv[1]
PORT = sys.argv[0]

print(sys.argv[1])

def main(*args):
    TM.Thread_manager(Client.client,(HOST,PORT))
    TM.Thread_manager(Server.Server,(PORT))

main(sys.argv)

