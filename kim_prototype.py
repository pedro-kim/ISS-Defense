import pygame, sys, os
import numpy as np
from GameObjects.PlayerShip import PlayerShip
from constants.colors import colors
from constants.velocities import velocities
from constants.dimensions import width_dimensions, height_dimensions
from constants.images import background_img, iss_img, spaceships_img, bullets_img, meteors_img
from GameObjects.Button import Button

WIN = pygame.display.set_mode((width_dimensions.get("screen"), height_dimensions.get("screen")))
pygame.display.set_caption("ISS Defense")

FPS = 60

BORDER = pygame.Rect(0, 0, width_dimensions.get("screen"), height_dimensions.get("screen"))

PLAYER_SHIP_HEALTH = 10


def iss_start(space_station):
    if space_station.y < height_dimensions.get("screen"):
        space_station.y += velocities.get("iss")


def handle_movement_player(keys_pressed, player_ship):
    if (
        (keys_pressed[pygame.K_w] or keys_pressed[pygame.K_UP])
        and player_ship.y - velocities.get("player_ship") > 0
    ):  # UP
        player_ship.y -= velocities.get("player_ship")

    if (
        (keys_pressed[pygame.K_a] or keys_pressed[pygame.K_LEFT]) 
        and player_ship.x - velocities.get("player_ship") > 0
    ):  # LEFT
        player_ship.x -= velocities.get("player_ship")

    if (
        keys_pressed[pygame.K_d]
        and player_ship.x + velocities.get("player_ship") + player_ship.width < BORDER.width
    ):  # RIGHT
        player_ship.x += velocities.get("player_ship")

    if keys_pressed[pygame.K_w] and player_ship.y - velocities.get("player_ship") > 0:  # UP
        player_ship.y -= velocities.get("player_ship")

    if (
        keys_pressed[pygame.K_s]
        and player_ship.y + velocities.get("player_ship") + player_ship.height < BORDER.height - 15
    ):  # DOWN
        player_ship.y += velocities.get("player_ship")

# def handle_enemy_movement(enemy_ship, bullets):
#     enemy_ship.y += ENEMY_SHIP_VEL
#     for bullet in bullets:
#         if enemy_ship.colliderect(bullet):
            

def handle_player_bullets(bullets, player_ship, enemy_ship):
    for bullet in bullets:
        bullet.y -= velocities.get("bullet")
        if enemy_ship.colliderect(bullet):
            bullets.remove(bullet)
        elif bullet.y < 0:
            bullets.remove(bullet)

def new_player_health(player_ship, player_health, enemy_bullets, meteors):


    for bullet in enemy_bullets:
        if player_ship.colliderect(bullet):
            player_health -= 1
    for meteor in meteors:
        if player_ship.colliderect(meteor):
            player_health -= 3
    return player_health

def handle_enemy_bullets(bullets, player_ship, enemy_ship):
    for bullet in bullets:
        bullet.y += velocities.get("bullet")
        if player_ship.colliderect(bullet):
            bullets.remove(bullet)
        elif bullet.y > height_dimensions.get("screen"):
            bullets.remove(bullet)

def handle_meteors(meteors, player_ship, player_bullets):
    for meteor in meteors:
        meteor.y += velocities.get("meteor")
        if player_ship.colliderect(meteor):
            meteors.remove(meteor)
        # elif meteor.y > height_dimensions.get("screen"):
        #     meteors.remove(meteor)
        for bullet in player_bullets:
            if bullet.colliderect(meteor):
                meteors.remove(meteor)
                player_bullets.remove(bullet)


def draw_window(space_station, player_ship, test_player, enemy_ship, player_bullets, enemy_bullets, meteors, button_pause):
    WIN.blit(background_img.get("first_background"), (0, 0))
    #pygame.draw.rect(WIN, colors.get("white"), BORDER)
    WIN.blit(background_img.get("first_background"), (0, 0))

    WIN.blit(iss_img.get("first_iss"), (space_station.x, space_station.y))
    WIN.blit(spaceships_img.get("player_blue3"), (player_ship.x, player_ship.y))
    WIN.blit(spaceships_img.get("enemy_black2"), (enemy_ship.x, enemy_ship.y))

    for bullet in player_bullets:
        WIN.blit(bullets_img.get("player_blue"), (bullet.x, bullet.y))

    for bullet in enemy_bullets:
        WIN.blit(bullets_img.get("enemy_red"), (bullet.x, bullet.y))
    
    for meteor in meteors:
        WIN.blit(meteors_img.get("brown1"), (meteor.x, meteor.y))

    test_player.draw(WIN)
    button_pause.draw(WIN)

    pygame.display.update()


def main():

    iss = pygame.Rect(
        (width_dimensions.get("screen") - width_dimensions.get("iss")) / 2, height_dimensions.get("screen") - height_dimensions.get("iss"), width_dimensions.get("iss"), height_dimensions.get("iss")
    )

    test_player = PlayerShip((width_dimensions.get("screen") - width_dimensions.get("spaceship")) / 2,height_dimensions.get("screen") - height_dimensions.get("spaceship") - height_dimensions.get("iss"),spaceships_img.get("player_red2"))

    player = pygame.Rect(
        (width_dimensions.get("screen") - width_dimensions.get("spaceship")) / 2,
        height_dimensions.get("screen") - height_dimensions.get("spaceship") - height_dimensions.get("iss"),
        width_dimensions.get("spaceship"),
        height_dimensions.get("spaceship"),
    )

    player_bullets = []
    player_health = 10

    meteors = []

    enemy = pygame.Rect(
        (width_dimensions.get("screen") - width_dimensions.get("spaceship")) / 2, 0, width_dimensions.get("spaceship"), height_dimensions.get("spaceship")
    )
    enemy_bullets = []


    clock = pygame.time.Clock()

    ENEMY_SHOOT_TIME = 0
    ENEMY_SHOOT_DELAY = 1000

    METEOR_TIME = 0
    METEOR_TIME_DELAY = 500

    # Telas iniciais pre-jogo
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
                screenHistory.append(1)
            if button_history.is_clicked(event):
                screenHistory.append(2)
            if button_return.is_clicked(event):
                screenHistory.pop()


        if screenHistory[-1] == 0:
            WIN.blit(background_img.get("first_background"), (0, 0))
            button_play.draw(WIN)
            button_instructions.draw(WIN) 
            button_history.draw(WIN) 
        if screenHistory[-1] == 1:
            WIN.blit(background_img.get("first_background"), (0, 0))
            pygame.draw.rect(WIN, colors.get("white"), BORDER)
            button_return.draw(WIN)
        if screenHistory[-1] == 2:
            WIN.blit(background_img.get("first_background"), (0, 0))
            pygame.draw.rect(WIN, colors.get("white"), BORDER)
            button_return.draw(WIN)
        

        pygame.display.update()

    button_pause = Button(10, 10, 200, 50, colors.get("mustard"), "Pausar", font, (255, 255, 255))
    button_despause = Button(10, 10, 200, 50, colors.get("mustard"), "Despausar", font, (255, 255, 255))

    while run and player_health > 0:
        clock.tick(FPS)
        current_time = pygame.time.get_ticks()

        if current_time - ENEMY_SHOOT_TIME > ENEMY_SHOOT_DELAY:
            bullet = pygame.Rect(
                enemy.x + enemy.width / 2 - 5,
                enemy.y + enemy.height / 2,
                height_dimensions.get("bullet"),
                width_dimensions.get("bullet"),
            )
            enemy_bullets.append(bullet)
            ENEMY_SHOOT_TIME = current_time

        if current_time - METEOR_TIME > METEOR_TIME_DELAY:
            random_meteor_x = int((width_dimensions.get("screen") - width_dimensions.get("meteor")) * np.random.random())
            if random_meteor_x + width_dimensions.get("meteor") < enemy.x or random_meteor_x > enemy.x + width_dimensions.get("spaceship"):
                new_meteor = pygame.Rect(random_meteor_x, -35, height_dimensions.get("meteor"), width_dimensions.get("meteor"))
                meteors.append(new_meteor)
                METEOR_TIME = current_time

        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                run = False
                pygame.quit()
                sys.exit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    bullet = pygame.Rect(
                        player.x + player.width / 2 - 5,
                        player.y + player.height / 2,
                        height_dimensions.get("bullet"),
                        width_dimensions.get("bullet"),
                    )
                    player_bullets.append(bullet)
                    test_player.shoot(WIN)

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


        for bullet in test_player.bullets:
            bullet.move()
                    
        keys_pressed = pygame.key.get_pressed()

        iss_start(iss)

        player_health = new_player_health(player, player_health, enemy_bullets, meteors)
        
        handle_movement_player(keys_pressed, player)
        test_player.move(keys_pressed, BORDER)
        handle_player_bullets(player_bullets, player, enemy)
        #test_player.shoot(keys_pressed)
        handle_enemy_bullets(enemy_bullets, player, enemy)
        handle_meteors(meteors, player, player_bullets)

        if player_health <= 0:
            run = False
            pygame.quit()
            sys.exit()

        draw_window(iss, player, test_player,enemy, player_bullets, enemy_bullets, meteors, button_pause)
        for bullet in test_player.bullets:
            bullet.draw(WIN)
        pygame.display.update()


if __name__ == "__main__":
    main()
