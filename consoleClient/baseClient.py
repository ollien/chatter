import socket
import traceback
import messageListener
class BaseClient():
	def __init__(self):
		self.sock=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
		self.server=None
		self.port=50028
	def start(self,server,port=50028):
		print "Connecting to ",server,":",port,"..."
		try:
			self.sock.connect((server,port))
		except Exception, error:
			print "Failed to connect to the server. Stacktrace is as follows."
			print error
			return;
		print "Connected!"
		print "Press ctrl-c to exit."
		listener=messageListener.MessageListener(self.sock)
		listener.start()
		try:
			while True:
				message=raw_input()
				self.sock.send(message)
		except (KeyboardInterrupt, SystemExit):
			print "Caught ctrl-c"
			self.sock.close()
			