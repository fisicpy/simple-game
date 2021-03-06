import pygame


class Wall:
    def __init__(self, surface, x, y, width, height, color):
        self.surface = surface
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.color = color

    def draw(self):
        pygame.draw.rect(self.surface, self.color, (self.x, self.y, self.width, self.height))

    def get_x(self):
        return self.x

    def get_y(self):
        return self.y

    def get_width(self):
        return self.width

    def get_height(self):
        return self.height

