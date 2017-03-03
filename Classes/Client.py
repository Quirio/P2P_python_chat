import socket

class client:
    def __init__(self,host,port):
        self.socket = socket.socket()
        self.socket.connect((host, port))

    def receip(self):
        while True:
            mensaje = raw_input("Yo > ")
            self.socket.send(mensaje)
            if mensaje == '/quit':
                break
            self.close()

    def close(self):
        print ("Exiting P2P python chat")
        self.socket.close()
