import socket
import threading
from uuid import uuid4
import connection as connectionClass
import connectionListener
class BaseServer(threading.Thread):
	def __init__(self,port=50028,bufferSize=5120):
		threading.Thread.__init__(self)
		self.connectedUsers={}
		self.port=port
		self.bufferSize=bufferSize
		self.listener=None
		self.sock=None
	def run(self):
		self.sock=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
		self.sock.bind(('0.0.0.0',self.port))
		self.sock.listen(1)
		self.listener=connectionListener.ConnectionListener(self.sock,self.recvConnection)
		self.listener.start()

	def addUser(self,userId,connection):
		if userId not in self.connectedUsers.keys():
			if connection is not None:
				self.connectedUsers[userId]=connectionClass.Connection(connection,userId,self.bufferSize,self.removeConnection,self.recvMessage)
			else:
				raise ValueError("The connection is null.")
		else:
			raise ValueError("User " + str(userId) + "Already exists.")
	def recvConnection(self,connection):
		try:
			self.addUser(uuid4().hex,connection)
		#This should never actually be needed, but worst case scneario ittl keep trying to create users until an unkown id is found.
		except ValueError,error:
			print error
	def recvMessage(self,message,userId):
		sendMessage=str(userId)+":"+message
		for user in self.connectedUsers:
			if user is not userId:
				self.connectedUsers[user].outgoing.send(sendMessage)

	def killThreads(self):
		if self.sock is not None:
			self.sock.close()
		for key in self.connectedUsers:
			print "killing "+key
			self.connectedUsers[key].incoming.alive=False
			self.connectedUsers[key].closeConnections()
		if self.listener is not None:
			self.listener.alive=False
		raise SystemExit
		return
	def removeConnection(self,userId):
		try:
			del self.connectedUsers[userId]
		except KeyError:
			raise ValueError("User not Found")		
