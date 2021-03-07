import pygame


def constrain(val, min_val, max_val):
    if val < min_val:
        return min_val
    if val > max_val:
        return max_val
    return val


class Player:
    def __init__(self, surface, x, y, width, height, body_color, eyes_color, hp, view, score):
        self.surface = surface
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.body_color = body_color
        self.eyes_color = eyes_color
        self.hp = hp
        self.view = view  # "up", "down", "right", "left"
        self.score = score

    def draw(self):
        pygame.draw.rect(self.surface, self.body_color, (self.x, self.y, self.width, self.height))
        if self.view == "up":
            pygame.draw.rect(self.surface, self.eyes_color, (self.x, self.y, self.width, self.height // 5))
        elif self.view == "down":
            pygame.draw.rect(self.surface, self.eyes_color, (self.x, self.y + self.height * 0.8, self.width, self.height // 5))
        elif self.view == "right":
            pygame.draw.rect(self.surface, self.eyes_color, (self.x + self.height * 0.8, self.y, self.width // 5, self.height))
        elif self.view == "left":
            pygame.draw.rect(self.surface, self.eyes_color, (self.x, self.y, self.width // 5, self.height))
        else:
            pygame.draw.rect(self.surface, self.eyes_color, (self.x, self.y, self.width, self.height // 5))

    def get_x(self):
        return self.x

    def get_y(self):
        return self.y

    def get_width(self):
        return self.width

    def get_height(self):
        return self.height

    def get_color(self):
        return self.color

    def get_hp(self):
        return self.hp

    def get_score(self):
        return self.score

    def get_view(self):
        return self.view

    def new_x(self, val):
        self.x = val

    def new_y(self, val):
        self.y = val

    def new_color(self, val):
        self.color = val

    def new_hp(self, val):
        self.hp = constrain(val, 0, 5)

    def new_score(self, val):
        self.score = val

    def new_view(self, val):
        self.view = val

    def shoot(self):
        pass

