#!/usr/bin/python
#----------------------------------------------------------------------#
#							Sockets									   #
#----------------------------------------------------------------------#

import socket
import sys
from thread import *
import Queue
import socketCom


class VerbindingList:
	def __init__(self):
		self.lijst = []
		self.counter = 0
		
	def add(self, conn, addr):
		self.counter += 1
		verb = Verbinding(conn,addr,self.counter)
		self.lijst.append(verb)
		print "connection added"
		self.printConn(self.counter)
		
	#def remove(self):
	def printConn(self,num):
		verb = self.lijst[num-1]
		print "Number:  " + str(verb.num)
		
		
	def closeAll(self):
		for verb in self.lijst:
			verb.conn.close()

class Verbinding:
	def __init__(self, conn, addr, num):
		self.lijst	= self
		self.conn	= conn
		self.addr	= addr
		self.num	= num
		self.loop	= True
		


#----------------------------------------------------------------------#
#							Client									   #
#----------------------------------------------------------------------#

class ClientProg:
	""" Client programme voor socket communicatie """
	def __init__(self, host='127.0.0.1', port=55632):
		self.host = host
		self.port = port
		self.start()
	
	def start(self):
		# Socket creation
		try:
			self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		except socket.error:
			print 'Failed to create socket'
			sys.exit()
		print 'Socket Created'
		
		#Connect to remote server
		try:
			self.sock.connect((self.host , self.port))
			print 'Socket Connected to ' + self.host + ' on port ' + str(self.port)
		except Exception, e:
			alert('something\'s wrong with %s. Exception type is %s' % (address, `e`))
	
	def send(self, msg):
		try:
			# Send whole string
			self.sock.sendall(msg)
			print 'Message send successfully'
		except socket.error:
			#Send failed
			print 'Send failed'
			sys.exit()
	
	def receive(self):
		recvmsg = self.sock.recv(16)
		print recvmsg
		return recvmsg
		
	def mainLoop(self):
		#while self.loop == True:
		print 'test'
		self.receive()
		self.send('test')
		self.receive()
		self.send('close')
		self.close()
	
	def close(self):
		self.sock.close()



if __name__ == "__main__":
	if len(sys.argv) > 1:
		if sys.argv[1] == 'server':
			mainProg = ServerProg()
			
		else:
			mainProg = ClientProg()
	else:
		mainProg = ServerProg()
		
		
