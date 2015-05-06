#! /usr/bin/env python

import os, sys
import math
import pygame
import pygame.camera
from pygame.locals import *
from Interface import *
from joystickh import *
import socketmanager

if not pygame.font: print 'Warning, fonts disabled'
if not pygame.mixer: print 'Warning, sound disabled'

""" Definiton of colors """
red = (255,0,0)
green = (0,255,0)
blue = (0,0,255)
darkBlue = (0,0,128)
white = (255,255,255)
black = (0,0,0)
pink = (255,200,200)

class PyManMain:
	#"""The Main PyMan Class - This class handles the main 
	#initialization and creating of the Game."""
	
	def __init__(self, width=1000,height=720):
		#"""Initialize"""
		#"""Initialize PyGame"""
		pygame.init()
		#"""Set the window Size"""
		self.width = width
		self.height = height
		#"""Create the Screen"""
		self.screen = pygame.display.set_mode((self.width, self.height),RESIZABLE)
		#Connection
		self.connected = False
		
														  
	def MainLoop(self):
		#"""This is the Main Loop of the Game"""
		
		"""os.environ['PYGAME_CAMERA'] = 'opencv'"""
		#"""no idea screen"""
		screen = self.screen
		#"""Pen om te tekenen"""
		inter = Interfacer(screen)
		#""" timer """
		clock = pygame.time.Clock()
		#""" joystick settings """
		joystick = JoyStickHandl()
		#""" Print text """
		textPrint = TextPrint(inter)
		#held down"""
		pygame.key.set_repeat(500, 30)
		
		#"""Create the background"""
		self.background = pygame.Surface(self.screen.get_size())
		self.background = self.background.convert()
		self.background.fill((0,0,0))
		bg_image = pygame.image.load("bg_image.jpg").convert()
		
		#--- Socket start ---
		#self.clientSock = socketmanager.ClientProg()
		updateclientcounter = 0
		
		print('Starting main loop')
		
		while 1:
			#""" Event handeling """
			for event in pygame.event.get():
				if event.type == pygame.QUIT: 
					sys.exit()
				elif event.type == KEYDOWN:
					if ((event.key == K_RIGHT)
					or (event.key == K_LEFT)
					or (event.key == K_UP)
					or (event.key == K_DOWN)
					or (event.key == K_ESCAPE)):
						inter.keyEventHandl(event.key)
				elif event.type == MOUSEBUTTONDOWN:
					inter.mouseEventHandl(event.button,event.pos)
				elif event.type == VIDEORESIZE:
					self.screen = pygame.display.set_mode(event.size,DOUBLEBUF|RESIZABLE)
					screen = self.screen
					inter.resizeHadl(event.size,event.w,event.h,screen)
			pygame.event.pump()
			
			
			#--- Socket handeling ---
			if(updateclientcounter >= 5):
				#self.clientSock.send('print test')
				(yax,xax,rax) = joystick.getAxis()
				#(yax,xax,rax) = (0.0,0.0,0.0)
				if(math.fabs(xax) > 0.2) or (math.fabs(yax) > 0.2):
					if(math.fabs(xax) > math.fabs(yax)):
						if(xax > 0):
							speed = str(int(100*math.fabs(xax)))
							#print "Backwards"
							#print "Speed: " + speed
							#self.clientSock.send('comMovBW ' + speed)
						else:
							speed = str(int(100*math.fabs(xax)))
							#self.clientSock.send('comMovFW ' + speed)
					else:
						if(yax > 0):
							speed = str(int(100*math.fabs(yax)))
							#self.clientSock.send('comTurnRight ' + speed)
						else:
							speed = str(int(100*math.fabs(yax)))
							#self.clientSock.send('comTurnLeft ' + speed)
				#else:
						#self.clientSock.send('comFree 0')
						
				"""
				if(xax > 0.5):
					self.clientSock.send('comMovBW 100')
				elif(xax < -0.5):
					self.clientSock.send('comMovFW 100')
				elif(yax < -0.5):
					self.clientSock.send('comTurnLeft 100')
				elif(yax > 0.5):
					self.clientSock.send('comTurnRight100')
				else:
					self.clientSock.send('comFree 0')"""
				updateclientcounter = 0
			else:
				updateclientcounter += 1
			
			#""" Calculations """
			inter.updateJoyAxis(joystick.getAxis())
			inter.movRecJoy()
			"""camimage = cam.get_image()"""
			
			#""" Animation """
			screen.fill(black)
			screen.blit(pygame.transform.scale(bg_image,screen.get_size()), (0,0))
			"""screen.blit(camimage,((0,0),(640,480)))"""
			inter.drawInterface()
			
			textPrint.reset()
			textPrint.printer(screen, joystick.name )
			textPrint.printer(screen, "last mouse click: x=" + str(inter.mx) + " y=" + str(inter.my) )
			"""textPrint.printer(screen, pygame.camera.list_cameras() )"""
			
			"""inter.drawHouse(5,120,100,100,screen,green)
			inter.rectangle(200,200,300,240,screen,red)
			inter.intRec()
			inter.movRec(1,0)
			pygame.draw.rect( screen, white, ((200,240),(20,20)) )"""
			
			#""" Image handeling """
			pygame.display.flip()
			msElapsed = clock.tick(40)



if __name__ == "__main__":
	MainWindow = PyManMain()
	MainWindow.MainLoop()
	   
