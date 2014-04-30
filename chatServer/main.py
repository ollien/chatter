import baseServer
import signal
import sys
import threading
def killProgram(signal,frame):
	print "Ctrl-C"
	server.killThreads()
	print "Conections closed. Joining threads."
	server.join()
	raise ValueError
	for thread in threading.enumerate():
		try:
			print thread.__class__.__name__
			if thread is not threading.currentThread() and thread.__class__.__name__ is not "HistorySavingThread":
				print thread
				thread.join()
		except TypeError:
			print "Type Error on closing"
	print "Threads joined. Closing"
	sys.exit()
server=baseServer.BaseServer()
server.start()
print "Started"
signal.signal(signal.SIGINT,killProgram)
signal.pause()
print "f"