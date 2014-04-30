class OutgoingConnection():
	def __init__(self,connection,userId):
		self.connection=connection
		self.userId=userId
	def send(self,message):
		self.connection.send(message)
	