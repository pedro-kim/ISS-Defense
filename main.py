import os
from classes import *

DISPLAY_WIDTH, DISPLAY_HEIGHT = 540, 900 
WIN = pg.display.set_mode((DISPLAY_WIDTH, DISPLAY_HEIGHT))
pg.display.set_caption("ISS Defense")

FPS = 60
VEL = 5
BULLET_VEL = 8

YELLOW = (255, 255, 0)

BACKGROUND_IMAGE = pg.image.load("ISS-Defense/Images/background.png")

def draw_window(player, player_bullets):
    WIN.blit(BACKGROUND_IMAGE, (0, 0))
    WIN.blit(WHITE_SPACESHIP,(player.x, player.y))

    for bullet in player_bullets:
        pg.draw.rect(WIN, YELLOW, bullet)

    pg.display.update()

def handle_player_bullets(player_bullets, player):
    for bullet in player_bullets:
        bullet.y -= BULLET_VEL

def main():

    clock = pg.time.Clock()
    previous_time = pg.time.get_ticks()

    player = Spaceship(245, 800, SPACESHIP_WIDTH, SPACESHIP_HEIGHT)

    run = True
    while run:

        clock.tick(FPS)

        for event in pg.event.get():
            if event.type == pg.QUIT:
                run = False

        current_time = pg.time.get_ticks()
        if current_time - previous_time > 500:
            previous_time = current_time
            bullet = pg.Rect(player.x + player.width/2 - 2, player.y - 1, 4 ,8) 
            player_bullets.append(bullet)

        keys_pressed = pg.key.get_pressed()
        player_movement(keys_pressed, player)

        handle_player_bullets(player_bullets, player)
        
        draw_window(player, player_bullets)

    pg.quit()


if __name__ == "__main__":
    main()
