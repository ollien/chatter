import threading
from socket import timeout

class ConnectionListener(threading.Thread):
	def __init__(self,socket,passConnectionUpFunction):
		threading.Thread.__init__(self)
		self.setDaemon(True)
		self.sock=socket
		self.passConnectionUp=passConnectionUpFunction
		self.alive=True
	def run(self):
		while self.alive: #Note that we're being a good little while loop and not spinning idle. sock.accept() is blocking.
			print "Waiting for connection"
			request = self.sock.accept()
			connection = request[0]
			address = request[1]
			print "Recieved a connection from "+ address[0]
			self.passConnectionUp(connection)