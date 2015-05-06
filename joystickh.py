#! /usr/bin/env python
""" Joystick classes """

import os, sys
import pygame
from pygame.locals import *

class JoyStickHandl:
	def __init__(self):
		self.count = pygame.joystick.get_count()
		if(self.count > 0):
			self.joystick = pygame.joystick.Joystick(0)
			self.joystick.init()
			self.name = self.joystick.get_name()
			self.joyx = self.joystick.get_axis( 0 )
			self.joyy = self.joystick.get_axis( 1 )
			self.joyr = self.joystick.get_axis( 2 )
			"""self.joyr = 0.20"""
			
			
	def setCount(self,counter):
		self.count = counter
		
	def getCount(self):
		return self.count
	
	def setJoystick(self,js):
		self.joystick = js
	
	def getJoystick(self):
		return self.joystick
	
	def getAxis(self):
		self.updateAxis()
		return (self.joyx,self.joyy,self.joyr)
	
	def updateAxis(self):
		if(self.count > 0):
			self.joyx = self.joystick.get_axis( 0 )
			self.joyy = self.joystick.get_axis( 1 )
			self.joyr = self.joystick.get_axis( 2 )
			"""self.joyr = 0.20"""
