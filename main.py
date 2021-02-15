import pygame
import keyboard, config
import level, player
import apple, random

def constrain(val, min_val, max_val):
	if val < min_val: return min_val
	if val > max_val: return max_val
	return val


pygame.init()
display = pygame.display.set_mode((config.display_width, config.display_height))
pygame.display.set_caption("My game")
clock = pygame.time.Clock()
pygame.font.init()
myfont = pygame.font.SysFont('Arial', 30)

level_map = ["###############",
			 "#~~~~~~~~~~~~~#",
			 "#~~~~~~~~~~~~~#",
			 "#####~~~###~~~#",
			 "#~~~~~~##~~~~~#",
			 "#~~~~~~~~~~~~~#",
			 "##~~~~~~~~~~~~#",
			 "##~~~~~~~###~~#",
			 "##~~~#~~~~~~~~#",
			 "#~~~###~~~~~~~#",
			 "#~~~~~#~~~~####",
			 "#~~~~~#~~~~#~~#",
			 "#~~~~~~~~~~~~~#",
			 "####~~~~~~~~~~#",
			 "###############",]

level = level.Level(display, level_map, 15, 15, config.block_size, (198, 42, 136), "#", (0, 0, 0), "~")

player = player.Player(display, (3, 196, 161), config.block_size, 7, 6, "right", "left", "up", "down", 0)

apple_x = 0
apple_y = 0		
while True:
	apple_x = random.randint(0, 14)
	apple_y = random.randint(0, 14)
	if player.get_y() == apple_y:
		continue
	elif player.get_x() == apple_x:
		continue
	elif level.get_symbol(apple_x, apple_y) == "#":
		continue
	else:
		break
apple = apple.Apple(display, apple_x, apple_y, (89, 9, 149), config.block_size)


if __name__ == "__main__":
	run_game = True
	while run_game:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				run_game = False

		if keyboard.is_pressed(player.get_btn_right()):
			new_player_x = constrain(player.get_x() + 1, 0, 14) 
			if level.get_symbol(new_player_x, player.get_y()) == "~":
				player.new_x(new_player_x)
		if keyboard.is_pressed(player.get_btn_left()):
			new_player_x = constrain(player.get_x() - 1, 0, 14) 
			if level.get_symbol(new_player_x, player.get_y()) == "~":
				player.new_x(new_player_x)
		if keyboard.is_pressed(player.get_btn_up()):
			new_player_y = constrain(player.get_y() - 1, 0, 14)
			if level.get_symbol(player.get_x(), new_player_y) == "~":
				player.new_y(new_player_y)
		if keyboard.is_pressed(player.get_btn_down()):
			new_player_y = constrain(player.get_y() + 1, 0, 14)
			if level.get_symbol(player.get_x(), new_player_y) == "~":
				player.new_y(new_player_y)

		if player.get_x() == apple.get_x() and player.get_y() == apple.get_y():
			while True:
				apple.new_x(random.randint(0, 14)) 
				apple.new_y(random.randint(0, 14)) 
				if player.get_y() == apple.get_y():
					continue
				elif player.get_x() == apple.get_x():
					continue
				elif level.get_symbol(apple.get_x(), apple.get_y()) == "#":
					continue
				else:
					break
			player.new_score(player.get_score() + 1)

		display.fill((0, 0, 0))

		level.draw()
		player.draw()
		apple.draw()

		textsurface = myfont.render(f"score: {player.get_score()}", False, (3, 196, 161))
		display.blit(textsurface, (5, 297))

		pygame.display.flip()
		clock.tick(config.FPS)


