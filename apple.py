import pygame
import random

class Apple():
	def __init__(self, screen, x, y, color, size):
		self.screen = screen
		self.x = x
		self.y = y
		self.color = color
		self.size = size

	def draw(self):
		pygame.draw.rect(self.screen, self.color, (self.x * self.size, self.y * self.size, self.size, self.size))

	def get_x(self):
		return self.x

	def get_y(self):
		return self.y

	def new_x(self, val):
		self.x = val

	def new_y(self, val):
		self.y = val
		