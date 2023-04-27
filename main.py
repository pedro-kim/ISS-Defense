import pygame, sys, os, json
import numpy as np

# Import classes
from classes.PlayerShip import PlayerShip
from classes.EnemyShip import EnemyShip
from classes.Meteor import Meteor

# Import utils
from utils.collide_bullets import collide_enemy_bullets, collide_player_bullets
from utils.collide_meteors import collide_meteors
from utils.render_planet import render_planet

# Import constants
from constants.velocities import velocities
from constants.dimensions import width, height
from constants.images import space_background_img, iss_img, spaceships_img, meteors_img, ui_img
from constants.fonts import score_font
from constants.buttons import button_return, button_pause, button_despause, button_play, button_instructions, button_history, button_title

# Import screens
from screens.instructions import render_instructions_screen
from screens.history import render_history_screen

# Initialize the mixer module
pygame.mixer.init()  

# Initialize global variables
WIN = pygame.display.set_mode((width.get("screen"), height.get("screen")))
pygame.display.set_caption("ISS Defense")


# Initialize global variables
SCORING_LIST = [0,0]
FPS = 60
START_SCREEN = 0
INSTRUCTIONS_SCREEN = 1
HISTORY_SCREEN = 2



def iss_start(space_station):
    if space_station.y < height.get("screen"):
        space_station.y += velocities.get("iss")

def read_high_score():
    data_file = os.path.join("assets", "data", "scoring.json")
    try:
        with open(data_file, "r") as f:
            data = json.load(f)
            SCORING_LIST[1] = data["high_score"]
    except FileNotFoundError:
        SCORING_LIST[1] = 0

    return data
    
def write_high_score(new_score, data):
    if new_score > SCORING_LIST[1]:
        data_file = os.path.join("assets", "data", "scoring.json")
        data["high_score"] = new_score
        with open(data_file, "w") as f:
            json.dump(data, f)


def draw_window(planet_frame, current_time, space_station, player, enemy, meteors):
    WIN.blit(space_background_img.get("space_background"), (0, 0))

    render_planet(WIN, planet_frame)

    WIN.blit(iss_img.get("first_iss"), (space_station.x, space_station.y))

    enemy.shoot(current_time, WIN)
    
    for dynamics in [player.bullets, enemy.bullets, meteors]:
        for dynamic in dynamics:
            dynamic.move()
            dynamic.draw(WIN)

    player.draw(WIN)
    
    enemy.draw(WIN)

    button_pause = pygame.transform.scale(
        pygame.image.load(os.path.join("assets", "images", "tile_0266.png")),
        (60, 60),
    )
    WIN.blit(button_pause, (10, 10))

    # Draw player health
    WIN.blit(ui_img.get("player_icon"), (width.get("screen") - 120, 20))
    WIN.blit(ui_img.get("digito_x"), (width.get("screen") - 70, 30))
    if player.health == 10:
        WIN.blit(ui_img.get("digito_1"), (width.get("screen") - 50, 20))
        WIN.blit(ui_img.get("digito_0"), (width.get("screen") - 30, 20))
    else:
        WIN.blit(ui_img.get(f"digito_{player.health}"), (width.get("screen") - 40, 20))

    # Draw score
    score_to_blit = f"{SCORING_LIST[0]}"
    score_sfc = score_font.render(score_to_blit, True, (255,255,255))
    WIN.blit(score_sfc, (width.get("screen") - 120, 50))

    pygame.display.update()



def main():
    SCORING_LIST[0] = 0
    METEOR_TIME = 0
    METEOR_TIME_DELAY = 500
    meteors = []
    planet_frame = [0]
    screenHistory = [START_SCREEN]

    pygame.mixer.music.load(os.path.join("assets", "music", "main_music.mp3"))  # Load the MP3 file
    pygame.mixer.music.play(-1)  # Play the music

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

    clock = pygame.time.Clock()

    run = False

    pygame.init()
    clock.tick(20)

    esc_paused = False

    data = read_high_score()

    while not run:

        WIN.blit(space_background_img.get("space_background"), (0, 0))
        
        if screenHistory[-1] is START_SCREEN:
            button_title.draw(WIN)
            button_play.draw(WIN)
            button_instructions.draw(WIN) 
            button_history.draw(WIN)
            text_surface = score_font.render(f'Highest Score:{data["high_score"]}', True, (255, 255, 255))
            WIN.blit(text_surface, (170, 700))
        if screenHistory[-1] is INSTRUCTIONS_SCREEN:
            render_instructions_screen(WIN)
        if screenHistory[-1] is HISTORY_SCREEN:
            render_history_screen(WIN)


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


        pygame.display.update()

    pygame.mixer.music.load(os.path.join("assets", "music", "level1_music.mp3"))
    pygame.mixer.music.play(-1)

    while run:
        clock.tick(FPS)
        current_time = pygame.time.get_ticks()
        keys_pressed = pygame.key.get_pressed()


        if current_time - METEOR_TIME > METEOR_TIME_DELAY:
            random_meteor_x = int((width.get("screen") - width.get("meteor")) * np.random.random())
            if (np.random.random() > 0.75):
                random_meteor_type = 'grey'
            else:
                random_meteor_type = 'brown'
            if random_meteor_x + width.get("meteor") < enemy.x or random_meteor_x > enemy.x + width.get("spaceship"):
                new_meteor = Meteor(random_meteor_x, -35, type=random_meteor_type)
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
                    esc_paused = True
                
            if button_pause.is_clicked(event) or esc_paused:
                pause = True
                while pause:
                    for pause_event in pygame.event.get():
                        if button_despause.is_clicked(pause_event):
                            pause = False
                            esc_paused = False
                        if pause_event.type == pygame.KEYDOWN:
                            if pause_event.key == pygame.K_ESCAPE:
                                pause = False
                                esc_paused = False
                        if pause_event == pygame.QUIT:
                            pause = False
                            esc_paused = False
                            run = False
                            pygame.quit()
                            sys.exit()
                    WIN.blit(pygame.transform.scale(pygame.image.load(os.path.join("assets", "images", "tile_0265.png")),(60, 60),), (10, 10))
                    pygame.display.update()


        iss_start(iss)
        
        player.move(keys_pressed)
        
        collide_player_bullets(player, enemy)
        
        collide_enemy_bullets(player, enemy)
        
        collide_meteors(meteors, player, SCORING_LIST)

        if player.health <= 0:
            run = False
            write_high_score(SCORING_LIST[0], data)
            main()

        draw_window(planet_frame, current_time, iss, player, enemy, meteors)
        pygame.display.update()


if __name__ == "__main__":
    main()
