#! /usr/bin/env python
""" Joystick classes """

import os, sys
import pygame
from pygame.locals import *

class JoyStickHandl:
	def __init__(self):
		self.count = pygame.joystick.get_count()
		if(self.count > 0):
			sys.stdout = os.devnull
			sys.stderr = os.devnull
			
			self.joystick = pygame.joystick.Joystick(0)
			self.joystick.init()
			self.name = self.joystick.get_name()
			self.joyx = self.joystick.get_axis( 0 )
			self.joyy = self.joystick.get_axis( 1 )
			self.joyr = self.joystick.get_axis( 2 )
			"""self.joyr = 0.20"""
			
			sys.stdout = sys.__stdout__
			sys.stderr = sys.__stderr__
		else:
			self.name = 'No joystick'
			self.joyx = 0.0
			self.joyy = 0.0
			self.joyr = 0.0
			
			
	def setCount(self,counter):
		self.count = counter
		
	def getCount(self):
		return self.count
		
	def renewCount(self):
		self.count = pygame.joystick.get_count()
	
	def setJoystick(self,js):
		self.joystick = js
	
	def getJoystick(self):
		return self.joystick
	
	def getAxis(self):
		self.updateAxis()
		return (self.joyx,self.joyy,self.joyr)
	
	def updateAxis(self):
		if(self.count > 0):
			#sys.stdout = os.devnull
			#sys.stderr = os.devnull
			
			self.joyx = self.joystick.get_axis( 0 )
			self.joyy = self.joystick.get_axis( 1 )
			self.joyr = self.joystick.get_axis( 2 )
			"""self.joyr = 0.20"""
			
			#sys.stdout = sys.__stdout__
			#sys.stderr = sys.__stderr__
			
