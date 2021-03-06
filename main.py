import pygame
import config
import keyboard
import player
import wall


def constrain(val, min_val, max_val):
    if val < min_val:
        return min_val
    if val > max_val:
        return max_val
    return val


pygame.init()
display = pygame.display.set_mode((config.display_width, config.display_height))
pygame.display.set_caption("My game")
clock = pygame.time.Clock()
pygame.font.init()

player = player.Player(display, 100, 150, 50, 50, (36, 94, 255), (150, 202, 224), 5, "left")

walls = [wall.Wall(display, 0, 50, 600, 30, (198, 42, 136)),
         wall.Wall(display, 0, 50, 30, 500, (198, 42, 136)),
         wall.Wall(display, 0, 520, 600, 30, (198, 42, 136)),
         wall.Wall(display, 570, 50, 30, 500, (198, 42, 136))]

if __name__ == "__main__":
    run_game = True
    while run_game:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run_game = False

        display.fill((0, 0, 0))

        for wall in walls:
            wall.draw()

        player.draw()

        pygame.display.flip()
        clock.tick(config.FPS)


