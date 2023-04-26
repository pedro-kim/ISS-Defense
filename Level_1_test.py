import pygame, sys, os
import numpy as np
from pathlib import Path

from states.Level import Level

from classes.PlayerShip import PlayerShip
from classes.EnemyShip import EnemyShip
from classes.Meteor import Meteor
from classes.Button import Button

from secondary_functions.collide_bullets import collide_enemy_bullets, collide_player_bullets
from secondary_functions.collide_meteors import collide_meteors

from constants.colors import colors
from constants.velocities import velocities
from constants.dimensions import width, height
from constants.images import iss_img, spaceships_img, meteors_img, background_img

# Initialize the mixer module
pygame.mixer.init()  
pygame.mixer.music.load(os.path.join("music", "main_music.mp3"))  # Load the MP3 file
pygame.mixer.music.play(-1)  # Play the music

# Initialize global variables
WIN = pygame.display.set_mode((width.get("screen"), height.get("screen")))
pygame.display.set_caption("ISS Defense")

BORDER = pygame.Rect(0, 0, width.get("screen"), height.get("screen"))

START_SCREEN = 0
INSTRUCTIONS_SCREEN = 1
HISTORY_SCREEN = 2


def main():
    clock = pygame.time.Clock()

    run = False

    pygame.init()
    clock.tick(20)
    screenHistory = [START_SCREEN]
    font = pygame.font.Font(os.path.join('fonts', 'RobotoMono-Light.ttf'), 30)
    title_font = pygame.font.Font(os.path.join('fonts', 'RobotoMono-Regular.ttf'), 54)
    button_title = Button(170, 100, 200, 90, colors.get("black"), "ISS Defense", title_font, (255, 255, 255))
    button_play = Button(170, 300, 200, 50, colors.get("red"), "Jogar", font, (255, 255, 255))
    button_instructions = Button(170, 400, 200, 50, colors.get("black"), "Instrucoes", font, (255, 255, 255))
    button_history = Button(170, 500, 200, 50, colors.get("black"), "Historia", font, (255, 255, 255))
    button_return = Button(10, 10, 200, 50, colors.get("mustard"), "Retornar", font, (255, 255, 255))
    button_pause = Button(10, 10, 50, 50, colors.get("mustard"), "Pausar", font, (255, 255, 255))
    button_despause = Button(10, 10, 50, 50, colors.get("mustard"), "Despausar", font, (255, 255, 255))

    esc_paused = False

    while not run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if button_play.is_clicked(event):
                run = True
            if button_instructions.is_clicked(event):
                screenHistory.append(INSTRUCTIONS_SCREEN)
            if button_history.is_clicked(event):
                screenHistory.append(HISTORY_SCREEN)
            if button_return.is_clicked(event):
                screenHistory.pop()


        if screenHistory[-1] is START_SCREEN:
            WIN.blit(background_img.get("space_background"), (0, 0))
            button_title.draw(WIN)
            button_play.draw(WIN)
            button_instructions.draw(WIN) 
            button_history.draw(WIN)
        if screenHistory[-1] is INSTRUCTIONS_SCREEN:
            WIN.blit(background_img.get("space_background"), (0, 0))
            pygame.draw.rect(WIN, colors.get("white"), BORDER)
            button_return.draw(WIN)
        if screenHistory[-1] is HISTORY_SCREEN:
            WIN.blit(background_img.get("space_background"), (0, 0))
            pygame.draw.rect(WIN, colors.get("white"), BORDER)
            button_return.draw(WIN)
        

        pygame.display.update()

    stages = {
        "stage1":{
            "level1": Path("level_data")/"S1L1.JSON"
        }
    }
    level_1 = Level(WIN, clock, stages.get("stage1").get("level1"))

    level_1.run()

if __name__ == "__main__":
    main()