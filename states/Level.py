import pygame as pg
import numpy as np
import json, sys

from json_classes.jsonIss import Iss
from json_classes.jsonPlayerShip import PlayerShip
from json_classes.jsonEnemyShip import EnemyShip
from json_classes.jsonMeteor import Meteor
from json_classes.jsonButton import Button

from constants.images import iss_img, spaceships_img, background_img, buttons_img, meteors_img
from constants.dimensions import width, height
from constants.colors import colors


class Level():
    def __init__(self, screen, clock, level_file):

        # Sets the screen in which will occur the animations
        self.screen = screen
        
        # Loads the JSON file data
        with open(level_file, 'r') as f:
            self.level_data = json.load(f)

        # Store the iss data
        self.iss_data = self.level_data['iss'][0]

        # Store the player_ship data
        self.player_ship_data = self.level_data['player_ship'][0]

        # Store the enemy_ships data
        self.enemy_ships_data = self.level_data['enemy_ships'][0]
        ['enemy_ships']
        self.enemy_ships_time = 0

        # Create the list to store the EnemyShip objects
        self.enemy_ships = []

        # Store the brown and gray meteors data
        self.brown_meteors_data = self.level_data['meteors'][0]
        if len(self.level_data['meteors']) == 2:
            self.gray_meteors_data = self.level_data['meteors'][1]
        self.meteors_time = 0

        # Create the list to store the Meteor objects
        self.meteors = []

        # Create the ISS object:
        self.iss = Iss(iss_img.get('first_iss'), self.iss_data)

        # Create the PlayerShip object:
        self.player = PlayerShip(
            (width.get('iss') - self.player_ship_data.get('width')) / 2,
            height.get("screen") - self.player_ship_data.get('height') - self.iss.height,
            spaceships_img.get("player_red2"),
            self.player_ship_data
        )

        # Set background variables
        self.planet_data = self.level_data['planet'][0]
        self.planet_time = 0
        self.planet_frame = [0]

        self.fps = 60
        self.clock = pg.time.Clock()

        #Level buttons
        self.pause_button_x = 10
        self.pause_button_y = 10
        self.pause_button = Button(
            self.pause_button_x,self.pause_button_y,
            width.get('pause_tile'), height.get('pause_tile'),
            is_rect=False, image=buttons_img.get('pause_tile')
        )
        self.continue_button = Button(
            self.pause_button_x, self.pause_button_y,
            width.get('continue_tile'), height.get('continue_tile'),
            is_rect=False, image=buttons_img.get('continue_tile')
        )

        # Level booleans
        self.running = True
        self.pause = False
        self.esc_paused = False
        self.click_paused = False        


        

    def draw_level(self, current_time):

        # Blit the star and dark background image
        self.screen.blit(background_img.get("space_background"), (0,0))

        # Blit the planet background
        if current_time - self.planet_time > self.fps:
            self.screen.blit(
                background_img.get("planet_background")[self.planet_frame[0]], 
                ((width.get('screen') - self.planet_data.get('planet_width')) / 2,
                 (height.get('screen') - self.planet_data.get('planet_height')) / 2)
            )
            self.planet_time = current_time
            self.planet_frame[0] += 1
            if self.planet_frame[0] >= 2025: self.planet_frame[0] = 0
        else:
            self.screen.blit(
                background_img.get('planet_background')[self.planet_frame[0]],
                ((width.get('screen') - self.planet_data.get('planet_width')) / 2,
                (height.get('screen') - self.planet_data.get('planet_height')) / 2)
            )

        # Blit the Iss object
        self.screen.blit(self.iss.image, (self.iss.x, self.iss.y))

        # Blit the player bullets
        for bullet in self.player.bullets:
            bullet.move()
            bullet.draw(self.screen)

        # Shoot and blit enemy bullets
        for enemy in self.enemy_ships:
            enemy.shoot(current_time, self.screen)
            for bullet in enemy.bullets:
                bullet.move()
                bullet.draw(self.screen)

        # Blit the meteors
        for meteor in self.meteors:
            meteor.draw(self.screen)

        self.player.draw(self.screen)
        
        for enemy in self.enemy_ships:
            enemy.draw(self.screen)

        self.pause_button.draw(self.screen)
        

        pg.display.update()

    def pause_loop(self):
        self.pause = True
        while self.pause:
            self.continue_button.draw(self.screen)
            pg.display.update()
            for pause_event in pg.event.get():
                if pause_event.type == pg.QUIT:
                    self.pause = False
                    self.running = False
                    pg.quit()
                    sys.exit()
                if self.continue_button.is_clicked(pause_event):
                    self.pause = False
                    self.esc_paused = False
                if pause_event.type == pg.KEYDOWN:
                    if pause_event.key == pg.K_ESCAPE:
                        self.pause = False
                        self.esc_paused = False
                self.continue_button.draw(self.screen)


    def check_events(self):
        for event in pg.event.get():

            if event.type == pg.QUIT:
                self.running = False
                pg.quit()
                sys.exit()

            if event.type == pg.KEYDOWN:
                if event.key == pg.K_SPACE:
                    self.player.shoot(self.screen)

                if event.key == pg.K_ESCAPE:
                    self.esc_paused = True
            
            if (self.pause_button.is_clicked(event) or self.esc_paused):
                self.continue_button.draw(self.screen)
                self.pause_loop()
                

    def summon_enemy_ships(self, current_time):
        if current_time - self.enemy_ships_time > self.enemy_ships_data.get("summon_period"):
            for summon_x in self.enemy_ships_data.get("summon_x"):
                new_enemy_ship = EnemyShip(round(summon_x * width.get('screen')), -35, spaceships_img.get('enemy_black2'), self.enemy_ships_data)
                self.enemy_ships.append(new_enemy_ship)
        self.enemy_ships_time = current_time


    def summom_brown_meteors(self, current_time):
        #for enemy in self.enemy_ships:
        if current_time - self.meteors_time > self.brown_meteors_data.get('summon_period'):
            random_meteor_x = int((width.get("screen") - width.get("meteor"))*np.random.random())
            if random_meteor_x + width.get("meteor") < enemy.x or random_meteor_x > enemy.x + enemy.width:
                new_meteor = Meteor(random_meteor_x, -35, self.brown_meteors_data)
                self.meteors.append(new_meteor)
                self.meteors_time = current_time

    def summom_gray_meteors(self, current_time):
        for enemy in self.enemy_ships:
            if current_time - self.meteors_time > self.meteors[0].get('summom_period'):
                random_meteor_x = int((width.get("screen") - width.get("meteor"))*np.random.random())
                if random_meteor_x + width.get("meteor") < enemy.x or random_meteor_x > enemy.x + enemy.width:
                    new_meteor = Meteor(random_meteor_x, -35, self.gray_meteors_data)
                    self.meteors.append(new_meteor)
                    self.meteors_time = current_time

    # def collide_player_bullets(self):
    #     for bullet in self.player.bullets:
    #         for enemy in self.enemy_ships:
    #             if self.enemy.colliderect(bullet):
    #                 self.player.bullets.remove(bullet)
    #             elif bullet.y < 0:
    #                 self.player.bullets.remove(bullet)

    def collide_enemy_bullets(self):
        for enemy in self.enemy_ships:
            for bullet in enemy.bullets:
                if self.player.colliderect(bullet):
                    self.player.health -= 1
                    enemy.bullets.remove(bullet)
                elif bullet.y > height.get("screen"):
                    enemy.bullets.remove(bullet)
    
    def collide_meteors(self):
        for meteor in self.meteors:
            meteor.y += meteor.vel
            if self.player.colliderect(meteor):
                self.player.health -= 3
                self.meteors.remove(meteor)
            elif meteor.y > height.get("screen"):
                self.meteors.remove(meteor)
            for bullet in self.player.bullets:
                if bullet.colliderect(meteor):
                    if meteor.type == 'brown':
                        self.meteors.remove(meteor)
                    else:
                        meteor.type = 'brown'
                        meteor.image = meteors_img.get("brown1")
                    self.player.bullets.remove(bullet)
    

    def check_player_health(self):
        if self.player.health <= 0:
            self.running = False
     
    def run(self):
        while self.running:
            # Set the FPS:
            self.clock.tick(self.fps)

            # Measure the passage of time
            current_time = pg.time.get_ticks()

            # Get the pressed keys
            keys_pressed = pg.key.get_pressed()

            

            # Functions that depend of the passage of time
            self.summon_enemy_ships(current_time)
            #self.summom_brown_meteors(current_time)

            self.check_events()

            # Functions of each object
            self.iss.start()

            self.player.move(keys_pressed)
            self.player.collide_bullets(self.meteors, self.enemy_ships)

            for enemy in self.enemy_ships:
                enemy.move()
            
            #for enemy in self.enemy_ships:
               # enemy.collide_bul
            # Global Level functions
            self.collide_enemy_bullets()
            # self.collide_player_bullets()
            self.collide_meteors()

            self.check_player_health()

            self.draw_level(current_time)
