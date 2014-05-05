import threading

class MessageListener(threading.Thread):
	def __init__(self,sock):
		threading.Thread.__init__(self)
		self.setDaemon(True)
		self.alive=True
		self.sock=sock
	def run(self):
		while self.alive: #Not a bad loop! it won't idle spin, as sock.recv() is blocking
			message=self.sock.recv(5120)
			print message
			