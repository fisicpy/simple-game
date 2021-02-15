import pygame

def constrain(val, min_val, max_val):
	if val < min_val: return min_val
	if val > max_val: return max_val
	return val

class Level():
	def __init__(self, screen, level_map, level_width_symbols, level_height_symbols, block_width, block_color, block_symbol, floor_color, floor_symbol):
		self.screen = screen
		self.level_map = level_map
		self.level_width_symbols = level_width_symbols
		self.level_height_symbols = level_height_symbols
		self.block_width = block_width
		self.block_color = block_color
		self.block_symbol = block_symbol
		self.floor_color = floor_color
		self.floor_symbol = floor_symbol

	def draw(self):
		for string_i, string_e in enumerate(self.level_map):
			for element_i, element_e in enumerate(string_e):
				if element_e == self.block_symbol:
					color = (self.block_color)
				elif element_e == self.floor_symbol:
					color = (self.floor_color)
				pygame.draw.rect(self.screen, color, (element_i * self.block_width, string_i * self.block_width, self.block_width, self.block_width))

	def get_symbol(self, x, y):
		return self.level_map[y][x]