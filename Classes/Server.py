import socket  

class Server:
  def __init__(self, port):
    print(port[0])
    self.socket = socket.socket()
    self.port = int(port[0])
    self.socket.bind(("0.0.0.0", self.port))
    self.socket.listen(1)
    self.sc,self.host = self.socket.accept()

    self.listen()

  def listen(self):
    while True:
      recibido = str(self.sc.recv(1024))
      if recibido == '/quit':
        break
      elif len(recibido) != 0:
        print("Recibido: "+ recibido)
      #self.sc.send(recibido)
    self.close()

  def close(self):
    print ("Close conecction")
    self.sc.close()
    self.socket.close()

