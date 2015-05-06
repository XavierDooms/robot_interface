#! /usr/bin/env python
""" Interface classes """

import os, sys
import pygame
from pygame.locals import *

red = (255,0,0)
green = (0,255,0)
blue = (0,0,255)
darkBlue = (0,0,128)
white = (255,255,255)
black = (0,0,0)
pink = (255,200,200)

class Interfacer:
	""" Class to make drawings on screen """
	def __init__(self,screen):
		self.data = []
		self.screen = screen
		(self.xscr,self.yscr) = self.screen.get_size()
		
		self.xr1 = 200
		self.xr2 = 300
		self.yr1 = 200
		self.yr2 = 220
		self.color1 = blue
		self.color2 = white
		self.color3 = red
		self.color4 = white
		self.color5 = green
		
		self.joyx = 0.5
		self.joyy = 0.5
		self.joyr = 0.5
		self.colorj = white
		
		self.speed = 10
		
		self.mx = 10
		self.my = 10
		
		self.rtel = 0.5
		self.rdir = True
		
		
	def drawHouse(self,x, y, width, height, screen, color):
		points = [(x, y-((2/3.0) * height)), (x,y), (x+width,y), (x+width,y-(2/3.0) * height), (x,y-((2/3.0) * height)), (x + width/2.0,y-height), (x+width,y-(2/3.0)*height)]
		lineThickness = 5
		pygame.draw.lines(screen, color, False, points, lineThickness)

	def makeHouseFrame(self,x,y,width,height):
		points = [] # start with an empty list
		points.append((x,y- ((2/3.0) * height))) # top of 1st story, upper left
		points.append((x,y))  # lower left corner
		points.append((x+width,y)) # lower right corner
		points.append((x+width,y-(2/3.0) * height)) # top of 1st story upper right
		points.append((x,y- ((2/3.0) * height))) # top of first story, upper left
		points.append((x + width/2.0,y-height)) # top of roof
		points.append((x+width,y-(2/3.0)*height)) # top of 1st story, upper right
		return points
		
	def rectangle(self,x1,y1,x2,y2,screen,color):
		points = [(x1,y1),(x1,y2),(x2,y2),(x2,y1),(x1,y1)]
		lineThickness = 2
		pygame.draw.lines(screen, color, False, points, lineThickness)
		
	def intRec(self):
		self.rectangle(self.xr1,self.yr1,self.xr2,self.yr2,self.screen,self.color1)
		
	def intHouse(self):
		self.drawHouse(self.xr1,self.yr1,50,50,self.screen,self.color1)
		
	def movRec(self,xmov,ymov):
		self.xr1 += xmov
		self.xr2 += xmov
		self.yr1 += ymov
		self.yr2 += ymov
		
	def movRecJoy(self):
		self.movRec(self.speed*(self.joyx),self.speed*(self.joyy))
		
	def drawInterface(self):
		""" x pos joystick """
		self.rectangle(self.xscr*0.1,self.yscr*0.02,self.xscr*0.9,self.yscr*0.02+20,self.screen,self.color2)
		pygame.draw.rect( self.screen, self.color3, ((self.xscr*0.105,self.yscr*0.02+4),(self.xscr*0.795*(self.joyx+1)/2,14)) )
		
		""" y pos joystick """
		self.rectangle(self.xscr*0.98-20,self.yscr*0.1,self.xscr*0.98,self.yscr*0.9,self.screen,self.color2)
		pygame.draw.rect( self.screen, self.color3, ((self.xscr*0.9795,self.yscr*0.105),(-14,self.yscr*0.795*(self.joyy+1)/2)) )
		
		""" rotation joystick """
		joyrangle = 3.1415*(0.5-0.3*self.joyr)
		xmid = int(self.xscr*0.85)
		ymid = int(self.yscr*0.85)
		radius = int(self.yscr*0.06)
		radius2 = int(radius*self.rtel)
		pygame.draw.circle( self.screen, self.color4, (xmid,ymid), radius+2, 1)
		pygame.draw.arc(self.screen,self.color5,((xmid-radius2,ymid-radius2),(radius2*2,radius2*2)),joyrangle-0.3,joyrangle+0.3,radius2)
		self.animRotation()
		
		"""self.intRec()"""
		self.intHouse()
		
		
	def updateJoyAxis(self,joy):
		(jx,jy,jr) = joy
		self.joyx = jx
		self.joyy = jy
		self.joyr = jr
		
	def animRotation(self):
		if(self.rtel>1):
			self.rtel = 1
			self.rdir = False
		elif(self.rtel<0.5):
			self.rtel = 0.5
			self.rdir = True
		elif(self.rdir == True):
			self.rtel += 0.04
		else:
			self.rtel -= 0.04
			

	def keyEventHandl(self,key):
		if (key == K_RIGHT):
			self.movRec(self.speed,0)
		elif (key == K_LEFT):
			self.movRec(-self.speed,0)
		elif (key == K_UP):
			self.movRec(0,-self.speed)
		elif (key == K_DOWN):
			self.movRec(0,self.speed)
		elif (key == K_ESCAPE):
			sys.exit()
	
	def mouseEventHandl(self,button,(xpos,ypos)):
		self.mx = xpos
		self.my = ypos
		self.xr1 = xpos
		self.xr2 = xpos + 100
		self.yr1 = ypos
		self.yr2 = ypos + 20

	def resizeHadl(self,size,w,h,screen):
		self.xscr = w
		self.yscr = h
		self.screen = screen

class TextPrint:
	def __init__(self,inter):
		self.inter = inter
		self.reset()
		self.font = pygame.font.Font(None, 20)
		

	def printer(self, screen, textString):
		textBitmap = self.font.render(textString, True, white)
		screen.blit(textBitmap, [self.x, self.y])
		self.y -= self.line_height
		
	def reset(self):
		self.x = 10
		self.y = self.inter.yscr - 20
		self.line_height = 15
		
	def indent(self):
		self.x += 10
		
	def unindent(self):
		self.x -= 10
