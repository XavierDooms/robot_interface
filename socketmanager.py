#!/usr/bin/python
#----------------------------------------------------------------------#
#							Sockets									   #
#----------------------------------------------------------------------#

import socket
import sys
from thread import *
import Queue
import socketCom

#----------------------------------------------------------------------#
#							Server									   #
#----------------------------------------------------------------------#

class ServerProg:
	""" Server programme voor socket communicatie """
	def __init__(self, port=42000):
		self.host = socket.gethostname()	# Symbolic name meaning all available interfaces
		self.host = ''
		self.port = port					# Arbitrary non-privileged port
		self.loop = True
		self.comh = socketCom.CommandoVerwerken()  	#commandHandler
		self.connList = VerbindingList()
		self.start()
		self.mainLoop()

	def start(self):
		# Socket creation
		try:
			self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		except socket.error:
			print 'Failed to create socket'
			sys.exit()
		
		#Bind socket to local host and port
		try:
			self.sock.bind((self.host, self.port))
		except socket.error , msg:
			print 'Bind failed. Error Code : ' + str(msg[0]) + ' Message ' + msg[1]
			sys.exit()
		print 'Socket bind complete'
		
		#Start listening on socket
		self.sock.listen(10)
		print 'Socket now listening'
		
		#Give server status
		print ''
		print 'Server is now accessable'
		print 'Server name: ' + self.host
		print 'Server port: ' + str(self.port)
		print '.'
		
	def send(self, msg):
		try:
			# Send whole string
			self.socket.sendall(msg)
			print 'Message send successfully'
		except socket.error:
			#Send failed
			print 'Send failed'
			sys.exit()
	
	def recveive(self):
		recvmsg = self.sock.recv(4096)
		print recvmsg
		return recvmsg
		
	def mainLoop(self):
		try:
			while self.loop == True:
				conn, addr = self.getConnection()
				print 'Connected with ' + addr[0] + ':' + str(addr[1])
				# Start new thread for connection server client
				start_new_thread(self.startServerThread ,(conn,))
				self.connList.add(conn,addr)
		finally:
			self.close()
			print 'socket closed'
			
	def mainLoop2(self):
		try:
			conn, addr = self.getConnection()
			print 'Connected with ' + addr[0] + ':' + str(addr[1])
		finally:
			self.close()
			print 'socket closed'
	
	def startServerThread (self, conn, thrNum = 1):
		try:
			#comHand = 
			""" Start new thread for socket session handeling """
			#Sending message to connected client
			conn.send('Welcome to the server. Type something and hit enter\n') #send only takes string
			#infinite loop so that function do not terminate and thread do not end.
			while self.loop == True:
				#Receiving from client
				data = conn.recv(1024)
				reply = 'OK... ' + data
				if not data: 
					break
				self.getCommand(data)
				conn.sendall(reply)
		finally:
			#came out of loop
			conn.close()
			print 'connection closed'
	
	def getConnection(self):
		conn, addr = self.sock.accept()
		self.conn = conn
		self.addr = addr
		return conn, addr
	
	def close(self):
		self.loop = False
		self.connList.closeAll()
		self.sock.close()

	def getCommand(self, msg):
		#remove 'enter'
		if(msg[-2:] == '\r\n'):
			msg = msg[:-2]
		elif(msg[-1:] == '\n'):
			msg = msg[:-1]
		else:
			msg = msg
		
		#split msg in command and data
		msgsplit = msg.split(' ', 1)
		if (len(msgsplit) == 2):
			msgcom = msgsplit[0]
			msgvalue = msgsplit[1]
		else:
			msgcom = msg
			msgvalue = 'leeg'
		
		#CommandoVerwerken.comSelect(msgcom, msgvalue)
		print 'Command: ' + repr(msgcom)
		print 'Value:   ' + str(msgvalue)
		
		#select commando from options
		if msgcom == 'comMovFW':
			self.comh.comMovFW()
		elif msgcom == 'comMovBW':
			self.comh.comMovBW()
		elif msgcom == 'comTurnLeft':
			self.comh.comTurnLeft()
		elif msgcom == 'comTurnRight':
			self.comh.comTurnRight()
		elif msgcom == 'comFree':
			self.comh.comFree()
		elif msgcom == 'print':
			print 'Message received: '
			print msgvalue
			#self.comh.comPrint(msgvalue)
		elif msgcom == 'close':	
			self.close()
		elif msgcom == 'closeall':
			self.close()
			sys.exit()
		else:
			print 'error: invalid message'
		

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
	def __init__(self, host='192.168.1.20', port=42000):
		self.host = host
		self.port = port
		self.start()
		#self.mainLoop()
	
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
			print 'Socket Connected to ' + self.host + ' on ip ' + str(self.port)
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
		recvmsg = self.sock.recv(4096)
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
		
		
