import pygame as pg
import numpy as np
import sys

from constants.dimensions import width, height
from constants.time import time

from secondary_functions.collide_bullets import collide_enemy_bullets, collide_player_bullets
from secondary_functions.collide_meteors import collide_meteors

from classes.Meteor import Meteor
from classes.Button import Button

clock = pg.time.Clock()

METEOR_TIME = time.get("meteor")



def game_loop(iss, meteors, player, enemy, screen):
    while run:
        clock.tick(time.get("fps"))
        current_time = pg.time.get_ticks()
        keys_pressed = pg.key.get_pressed()

        if current_time - METEOR_TIME > time.get("meteor_delay"):
            random_meteor_x = int((width.get("screen") - width.get("meteor")) * np.random.random())
            if (np.random.random() > 0.75):
                random_meteor_type = 'grey'
            else:
                random_meteor_type = 'brown'
            if random_meteor_x + width.get("meteor") < enemy.x or random_meteor_x > enemy.x + width.get("spaceship"):
                new_meteor = Meteor(random_meteor_x, -35, type=random_meteor_type)
                meteors.append(new_meteor)
                METEOR_TIME = current_time

        for event in pg.event.get():

            if event.type == pg.QUIT:
                run = False
                pg.quit()
                sys.exit()

            if event.type == pg.KEYDOWN:
                if event.key == pg.K_SPACE:
                    player.shoot(screen)

                if event.key == pg.K_ESCAPE:
                    esc_paused = True
                
            if button_pause.is_clicked(event) or esc_paused:
                pause = True
                while pause:
                    for pause_event in pg.event.get():
                        if button_despause.is_clicked(pause_event):
                            pause = False
                            esc_paused = False
                        if pause_event.type == pg.KEYDOWN:
                            if pause_event.key == pg.K_ESCAPE:
                                pause = False
                                esc_paused = False
                        if pause_event == pg.QUIT:
                            pause = False
                            esc_paused = False
                            run = False
                            pg.quit()
                            sys.exit()
                    button_despause.draw(screen)
                    pg.display.update()


        iss_start(iss)
        player.move(keys_pressed)
        collide_player_bullets(player, enemy)
        collide_enemy_bullets(player, enemy)
        collide_meteors(meteors, player)

        if player.health <= 0:
            run = False
            main()

        draw_window(PLANET_TIME,planet_frame,current_time,iss, player, enemy, meteors, button_pause)
        pg.display.update()