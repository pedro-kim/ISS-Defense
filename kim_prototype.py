import pygame, sys
import numpy as np
from GameObjects.PlayerShip import PlayerShip
from GameObjects.EnemyShip import EnemyShip
from handlers.bullets import handle_player_bullets, handle_enemy_bullets
from handlers.meteors import handle_meteors
from constants.colors import colors
from constants.velocities import velocities
from constants.dimensions import width, height
from constants.images import background_img, iss_img, spaceships_img, meteors_img
from GameObjects.Button import Button

WIN = pygame.display.set_mode((width.get("screen"), height.get("screen")))
pygame.display.set_caption("ISS Defense")

FPS = 60

BORDER = pygame.Rect(0, 0, width.get("screen"), height.get("screen"))

START_SCREEN = 0
INSTRUCTIONS_SCREEN = 1
HISTORY_SCREEN = 2


def iss_start(space_station):
    if space_station.y < height.get("screen"):
        space_station.y += velocities.get("iss")

# def handle_enemy_movement(enemy_ship, bullets):
#     enemy_ship.y += ENEMY_SHIP_VEL
#     for bullet in bullets:
#         if enemy_ship.colliderect(bullet):
            
# def new_player_health(player_ship, player_health, enemy_bullets, meteors):
#     for bullet in enemy_bullets:
#         if player_ship.colliderect(bullet):
#             player_health -= 1
#     for meteor in meteors:
#         if player_ship.colliderect(meteor):
#             player_health -= 3
#     return player_health

def draw_window(space_station, player, enemy, meteors, button_pause, current_time):
    # WIN.blit(background_img.get("first_background"), (0, 0))
    #pygame.draw.rect(WIN, colors.get("white"), BORDER)
    WIN.blit(background_img.get("first_background"), (0, 0))

    WIN.blit(iss_img.get("first_iss"), (space_station.x, space_station.y))
    for bullet in player.bullets:
            bullet.move()
            bullet.draw(WIN)

    enemy.shoot(current_time, WIN)
    for bullet in enemy.bullets:
        bullet.move()
        bullet.draw(WIN)
    for meteor in meteors:
        WIN.blit(meteors_img.get("brown1"), (meteor.x, meteor.y))

    player.draw(WIN)
    enemy.draw(WIN)
    button_pause.draw(WIN)

    pygame.display.update()


def main():

    iss = pygame.Rect(
        (width.get("screen") - width.get("iss")) / 2,
        height.get("screen") - height.get("iss"),
        width.get("iss"),
        height.get("iss")
    )

    player = PlayerShip(
        (width.get("screen") - width.get("spaceship")) / 2,
        height.get("screen") - height.get("spaceship") - height.get("iss"),
        spaceships_img.get("player_red2")
    )

    enemy = EnemyShip((width.get("screen") - width.get("spaceship")) / 2, 0, 55, 40, spaceships_img.get('enemy_black2'))

    # player_health = 10

    meteors = []


    clock = pygame.time.Clock()

    # ENEMY_SHOOT_TIME = 0
    # ENEMY_SHOOT_DELAY = 1000

    METEOR_TIME = 0
    METEOR_TIME_DELAY = 500

    ### Inicial Screens
    run = False

    screenHistory = [0]
    pygame.init()
    clock.tick(20)
    font = pygame.font.Font('RobotoMono-Light.ttf', 30)
    button_play = Button(170, 100, 200, 50, colors.get("red"), "Jogar", font, (255, 255, 255))
    button_instructions = Button(170, 200, 200, 50, colors.get("black"), "Instrucoes", font, (255, 255, 255))
    button_history = Button(170, 300, 200, 50, colors.get("black"), "Historia", font, (255, 255, 255))
    button_return = Button(10, 10, 200, 50, colors.get("mustard"), "Retornar", font, (255, 255, 255))

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
            WIN.blit(background_img.get("first_background"), (0, 0))
            button_play.draw(WIN)
            button_instructions.draw(WIN) 
            button_history.draw(WIN) 
        if screenHistory[-1] is INSTRUCTIONS_SCREEN:
            WIN.blit(background_img.get("first_background"), (0, 0))
            pygame.draw.rect(WIN, colors.get("white"), BORDER)
            button_return.draw(WIN)
        if screenHistory[-1] is HISTORY_SCREEN:
            WIN.blit(background_img.get("first_background"), (0, 0))
            pygame.draw.rect(WIN, colors.get("white"), BORDER)
            button_return.draw(WIN)
        

        pygame.display.update()

    button_pause = Button(10, 10, 200, 50, colors.get("mustard"), "Pausar", font, (255, 255, 255))
    button_despause = Button(10, 10, 200, 50, colors.get("mustard"), "Despausar", font, (255, 255, 255))

    ### Game Screen
    while run:
        clock.tick(FPS)
        current_time = pygame.time.get_ticks()
        keys_pressed = pygame.key.get_pressed()

        if current_time - METEOR_TIME > METEOR_TIME_DELAY:
            random_meteor_x = int((width.get("screen") - width.get("meteor")) * np.random.random())
            if random_meteor_x + width.get("meteor") < enemy.x or random_meteor_x > enemy.x + width.get("spaceship"):
                new_meteor = pygame.Rect(random_meteor_x, -35, height.get("meteor"), width.get("meteor"))
                meteors.append(new_meteor)
                METEOR_TIME = current_time

        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                run = False
                pygame.quit()
                sys.exit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    player.shoot(WIN)

                if event.key == pygame.K_ESCAPE:
                    run = False
                    pygame.quit()
                    sys.exit()
                
            if button_pause.is_clicked(event):
                pause = True
                while pause:
                    for pause_event in pygame.event.get():
                        if button_despause.is_clicked(pause_event):
                            pause = False
                    button_despause.draw(WIN)
                    pygame.display.update()


        iss_start(iss)
        player.move(keys_pressed)
        handle_player_bullets(player, enemy)
        handle_enemy_bullets(player, enemy)
        handle_meteors(meteors, player)

        if player.health <= 0:
            run = False
            main()

        draw_window(iss, player, enemy, meteors, button_pause, current_time)
        pygame.display.update()


if __name__ == "__main__":
    main()
