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

def collision(obj1, obj2):
    if obj1.get_x() + obj1.get_width() >= obj2.get_x() and obj1.get_x() <= obj2.get_x() + obj2.get_width():
        x_coll = True
    else:
        x_coll = False
    if obj1.get_y() + obj1.get_height() >= obj2.get_y() and obj1.get_y() <= obj2.get_y() + obj2.get_height():
        y_coll = True
    else:
        y_coll = False
    return x_coll, y_coll


pygame.init()
display = pygame.display.set_mode((config.display_width, config.display_height))
pygame.display.set_caption("My game")
clock = pygame.time.Clock()
pygame.font.init()
pygame.font.init()
myfont = pygame.font.SysFont("Arial Black", 30)

player = player.Player(display, 250, 250, 50, 50, (3, 196, 161), (255, 255, 255), 5, "up", 0)

walls = [wall.Wall(display, 0, 50, 600, 30, (198, 42, 136)),
         wall.Wall(display, 0, 50, 30, 500, (198, 42, 136)),
         wall.Wall(display, 0, 520, 600, 30, (198, 42, 136)),
         wall.Wall(display, 570, 50, 30, 500, (198, 42, 136)),
         wall.Wall(display, 0, 200, 200, 30, (198, 42, 136)),
         wall.Wall(display, 120, 200, 30, 150, (198, 42, 136)),
         wall.Wall(display, 170, 170, 30, 60, (198, 42, 136)),
         wall.Wall(display, 340, 400, 150, 30, (198, 42, 136)),
         wall.Wall(display, 400, 320, 30, 100, (198, 42, 136)),
         wall.Wall(display, 220, 430, 30, 100, (198, 42, 136)),
         wall.Wall(display, 520, 170, 50, 30, (198, 42, 136)),
         wall.Wall(display, 400, 50, 30, 150, (198, 42, 136))]

if __name__ == "__main__":
    run_game = True
    while run_game:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run_game = False

        if keyboard.is_pressed("right"):
            if player.get_view() == "up":
                player.new_view("right")
            elif player.get_view() == "down":
                player.new_view("left")
            elif player.get_view() == "right":
                player.new_view("down")
            elif player.get_view() == "left":
                player.new_view("up")
        elif keyboard.is_pressed("left"):
            if player.get_view() == "up":
                player.new_view("left")
            elif player.get_view() == "down":
                player.new_view("right")
            elif player.get_view() == "left":
                player.new_view("down")
            elif player.get_view() == "right":
                player.new_view("up")

        display.fill((0, 0, 0))

        text = myfont.render(f"score: {player.get_score()}", False, (3, 196, 161))
        display.blit(text, (0, 0))

        for wall in walls:
            wall.draw()

        player.draw()

        pygame.display.flip()
        clock.tick(config.FPS)


