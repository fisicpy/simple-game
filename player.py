import pygame
import keyboard

class Player(object):
	def __init__(self, screen, color, size, x, y, btn_right, btn_left, btn_up, btn_down, score):
		self.screen = screen
		self.color = color
		self.size = size
		self.x = x
		self.y = y
		self.btn_right = btn_right
		self.btn_left = btn_left
		self.btn_up = btn_up
		self.btn_down = btn_down
		self.score = score

	def get_x(self):
		return self.x

	def get_y(self):
		return self.y

	def get_btn_right(self):
		return self.btn_right

	def get_btn_left(self):
		return self.btn_left

	def get_btn_up(self):
		return self.btn_up

	def get_btn_down(self):
		return self.btn_down

	def get_score(self):
		return self.score

	def new_x(self, val):
		self.x = val

	def new_y(self, val):
		self.y = val

	def new_score(self, val):
		self.score = val

	def draw(self):
		pygame.draw.rect(self.screen, self.color, (self.x * self.size, self.y * self.size, self.size, self.size))
