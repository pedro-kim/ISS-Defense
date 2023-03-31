import pygame, sys, os
import numpy as np

WIDTH, HEIGHT = 540, 960
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("ISS Defense")

WHITE = (255, 255, 255)

FPS = 60

BORDER = pygame.Rect(WIDTH, 0, 10, HEIGHT)
BACKGROUND_IMAGE = pygame.transform.scale(
    pygame.image.load(os.path.join("Images", "background.png")), (WIDTH, HEIGHT)
)

PLAYER_SHIP_HEALTH = 10

ISS_VEL = 1
METEOR_VEL = 2
ENEMY_SHIP_VEL = 3
PLAYER_SHIP_VEL = 5
BULLET_VEL = 10

SPACESHIP_WIDTH, SPACESHIP_HEIGHT = 55, 40
BULLET_WIDTH, BULLET_HEIGHT = 10, 20
ISS_WIDTH, ISS_HEIGHT = 490, 353
METEOR_WIDTH, METEOR_HEIGHT = 80, 70

SPACE_STATION = pygame.transform.scale(
    pygame.image.load(os.path.join("Images", "Station Center.png")),
    (ISS_WIDTH, ISS_HEIGHT),
)

PLAYER_BLUE_SPACESHIP = pygame.transform.scale(
    pygame.image.load(os.path.join("Images", "playerShip3_blue.png")),
    (SPACESHIP_WIDTH, SPACESHIP_HEIGHT),
)

PLAYER_BLUE_BULLET = pygame.transform.scale(
    pygame.image.load(os.path.join("Images", "laserBlue16.png")),
    (BULLET_WIDTH, BULLET_HEIGHT),
)

ENEMY_BLACK_SPACESHIP = pygame.transform.scale(
    pygame.image.load(os.path.join("Images", "enemyBlack2.png")),
    (SPACESHIP_WIDTH, SPACESHIP_HEIGHT),
)

ENEMY_RED_BULLET_IMAGE = pygame.image.load(os.path.join("Images", "laserRed16.png"))
ENEMY_RED_BULLET = pygame.transform.rotate(
    pygame.transform.scale(ENEMY_RED_BULLET_IMAGE, (BULLET_WIDTH, BULLET_HEIGHT)),
    180,
)

BROWN_METEOR = pygame.transform.scale(
    pygame.image.load(os.path.join("Images", "meteorBrown_big1.png")),
    (METEOR_WIDTH, METEOR_HEIGHT),
)


def iss_start(space_station):
    if space_station.y < HEIGHT:
        space_station.y += ISS_VEL


def handle_movement_player(keys_pressed, player_ship):
    if keys_pressed[pygame.K_a] and player_ship.x - PLAYER_SHIP_VEL > 0:  # LEFT
        player_ship.x -= PLAYER_SHIP_VEL

    if (
        keys_pressed[pygame.K_d]
        and player_ship.x + PLAYER_SHIP_VEL + player_ship.width < BORDER.x
    ):  # RIGHT
        player_ship.x += PLAYER_SHIP_VEL

    if keys_pressed[pygame.K_w] and player_ship.y - PLAYER_SHIP_VEL > 0:  # UP
        player_ship.y -= PLAYER_SHIP_VEL

    if (
        keys_pressed[pygame.K_s]
        and player_ship.y + PLAYER_SHIP_VEL + player_ship.height < HEIGHT - 15
    ):  # DOWN
        player_ship.y += PLAYER_SHIP_VEL

# def handle_enemy_movement(enemy_ship, bullets):
#     enemy_ship.y += ENEMY_SHIP_VEL
#     for bullet in bullets:
#         if enemy_ship.colliderect(bullet):
            


def handle_player_bullets(bullets, player_ship, enemy_ship):
    for bullet in bullets:
        bullet.y -= BULLET_VEL
        if enemy_ship.colliderect(bullet):
            bullets.remove(bullet)
        elif bullet.y < 0:
            bullets.remove(bullet)

def new_player_health(player_ship, player_health, enemy_bullets, meteors):

    print(enemy_bullets,meteors)

    for bullet in enemy_bullets:
        if player_ship.colliderect(bullet):
            player_health -= 1
            print('colidiu com  bala')
    for meteor in meteors:
        if player_ship.colliderect(meteor):
            player_health -= 3
            print('colidiu com meteoro')
    return player_health

def handle_enemy_bullets(bullets, player_ship, enemy_ship):
    for bullet in bullets:
        bullet.y += BULLET_VEL
        if player_ship.colliderect(bullet):
            bullets.remove(bullet)
        elif bullet.y > HEIGHT:
            bullets.remove(bullet)

def handle_meteors(meteors, player_ship, player_bullets):
    for meteor in meteors:
        meteor.y += METEOR_VEL
        if player_ship.colliderect(meteor):
            meteors.remove(meteor)
        # elif meteor.y > HEIGHT:
        #     meteors.remove(meteor)
        for bullet in player_bullets:
            if bullet.colliderect(meteor):
                meteors.remove(meteor)
                player_bullets.remove(bullet)


def draw_window(space_station, player_ship, enemy_ship, player_bullets, enemy_bullets, meteors):
    WIN.blit(BACKGROUND_IMAGE, (0, 0))
    pygame.draw.rect(WIN, WHITE, BORDER)

    WIN.blit(SPACE_STATION, (space_station.x, space_station.y))
    WIN.blit(PLAYER_BLUE_SPACESHIP, (player_ship.x, player_ship.y))
    WIN.blit(ENEMY_BLACK_SPACESHIP, (enemy_ship.x, enemy_ship.y))

    for bullet in player_bullets:
        WIN.blit(PLAYER_BLUE_BULLET, (bullet.x, bullet.y))

    for bullet in enemy_bullets:
        WIN.blit(ENEMY_RED_BULLET, (bullet.x, bullet.y))
    
    for meteor in meteors:
        WIN.blit(BROWN_METEOR, (meteor.x, meteor.y))

    pygame.display.update()


def main():

    iss = pygame.Rect(
        (WIDTH - ISS_WIDTH) / 2, HEIGHT - ISS_HEIGHT, ISS_WIDTH, ISS_HEIGHT
    )

    player = pygame.Rect(
        (WIDTH - SPACESHIP_WIDTH) / 2,
        HEIGHT - SPACESHIP_HEIGHT - ISS_HEIGHT,
        SPACESHIP_WIDTH,
        SPACESHIP_HEIGHT,
    )
    player_bullets = []
    player_health = 10

    meteors = []


    enemy = pygame.Rect(
        (WIDTH - SPACESHIP_WIDTH) / 2, 0, SPACESHIP_WIDTH, SPACESHIP_HEIGHT
    )
    enemy_bullets = []


    clock = pygame.time.Clock()

    ENEMY_SHOOT_TIME = 0
    ENEMY_SHOOT_DELAY = 1000

    METEOR_TIME = 0
    METEOR_TIME_DELAY = 500

    run = True
    while run and player_health > 0:
        clock.tick(FPS)
        current_time = pygame.time.get_ticks()


        if current_time - ENEMY_SHOOT_TIME > ENEMY_SHOOT_DELAY:
            bullet = pygame.Rect(
                enemy.x + enemy.width / 2 - 5,
                enemy.y + enemy.height / 2,
                BULLET_HEIGHT,
                BULLET_WIDTH,
            )
            enemy_bullets.append(bullet)
            ENEMY_SHOOT_TIME = current_time

        if current_time - METEOR_TIME > METEOR_TIME_DELAY:
            random_meteor_x = int((WIDTH - METEOR_WIDTH) * np.random.random())
            if random_meteor_x + METEOR_WIDTH < enemy.x or random_meteor_x > enemy.x + SPACESHIP_WIDTH:
                new_meteor = pygame.Rect(random_meteor_x, 0, METEOR_HEIGHT, METEOR_WIDTH)
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
                        BULLET_HEIGHT,
                        BULLET_WIDTH,
                    )
                    player_bullets.append(bullet)
                
                if event.key == pygame.K_ESCAPE:
                    run = False
                    pygame.quit()
                    sys.exit()

            # if event.type == pygame.KEYDOWN:
            #     if event.key == pygame.K_ESCAPE:
                    
        keys_pressed = pygame.key.get_pressed()

        iss_start(iss)

        player_health = new_player_health(player, player_health, enemy_bullets, meteors)
        
        handle_movement_player(keys_pressed, player)
        handle_player_bullets(player_bullets, player, enemy)
        handle_enemy_bullets(enemy_bullets, player, enemy)
        handle_meteors(meteors, player, player_bullets)

        if player_health <= 0:
            run = False
            pygame.quit()
            sys.exit()

        draw_window(iss, player, enemy, player_bullets, enemy_bullets, meteors)


if __name__ == "__main__":
    main()
