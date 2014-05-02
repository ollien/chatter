import threading
from socket import timeout

class IncomingConnection(threading.Thread):
	def __init__(self,connection,userId,bufferSize,recvMessageFunction,killConnectionFunction):
		threading.Thread.__init__(self)
		self.setDaemon(True)
		self.connection=connection
		self.bufferSize=bufferSize
		self.userId=userId
		self.sendMessageUp=recvMessageFunction
		self.killMyConnection=killConnectionFunction
		self.alive=True #When false, the loop can die.
	def run(self):
		while self.alive: #Not a bad loop! It won't idle spin, as connection.recv()  will block
			data=self.connection.recv(self.bufferSize)
			if not data:
				print "User "+str(self.userId)+"\'s data was False."
				self.killMyConnection()
				break;
			self.sendMessageUp(data,self.userId)