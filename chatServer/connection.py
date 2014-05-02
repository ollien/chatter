import outgoingConnection
import incomingConnection

class Connection():
	def __init__(self,connection,userId,passMessageUpFunction,bufferSize):
		self.userId=userId
		self.connection=connection
		self.bufferSize=bufferSize
		print self.recvMessage
		print type(self.recvMessage)
		self.incoming=incomingConnection.IncomingConnection(self.connection,self.userId,self.bufferSize,self.recvMessage,self.closeConnections)
		self.outgoing=outgoingConnection.OutgoingConnection(self.connection,self.userId)
		self.incoming.start()
		self.passMessageUp=passMessageUpFunction
	def sendMessage(self,message,userId=None): #userId will be used for private messages
		self.outgoing.send(message)
	
	def recvMessage(self,message,userId):
		self.passMessageUp(message,userId)
	def closeConnections(self):
		self.connection.close()
		self.incoming.connection.close()
		self.outgoing.connection.close()