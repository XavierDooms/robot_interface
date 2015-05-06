#----------------------------------------------------------------------#
#					Sockets: Commando verwerken						   #
#----------------------------------------------------------------------#

class CommandoVerwerken:
	def __init__(self):
		opt = ' '
	
	def comMovFW(self):
		print 'Forward'
	
	def comMovBW(self):
		print 'Backward'
	
	def comTurnLeft(self):
		print 'Turn left'
	
	def comTurnRight(self):
		print 'Turn right'
		
	def comFree(self):
		print 'Neutral'
		
	def comPrint(self, msgvalue = ' '):
		print 'printing: ' + msgvalue
	
	
