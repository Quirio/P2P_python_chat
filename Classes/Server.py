import socket  

class Server:
  def __init__(self,port):
    self.socket = socket.socket()
    self.socket.bind(("0.0.0.0", port))
    self.socket.listen(1)
    self.sc = self.socket.accept()

  def listen(self):
    while True:
      recibido = self.sc.recv(1024)
      if recibido == '/quit':
        break
      print("Recibido: "+str(recibido))
      self.sc.send(recibido)
    self.close()

  def close(self):
    print ("Close conecction")
    self.sc.close()
    self.socket.close()

