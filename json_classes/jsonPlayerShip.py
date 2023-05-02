import pygame as pg
from constants.dimensions import height, width
from classes.GameObject import GameObject
from classes.Projectile import Projectile

class PlayerShip(GameObject):
    def __init__(self, x, y, image, player_ship_data):
        self.x = x
        self.y = y
        self.image = image

        # Load the main PlayerShip attributes from the JSON Level file
        self.width = player_ship_data.get('width')
        self.height = player_ship_data.get('height')
        self.health = player_ship_data.get('health')
        self.vel = player_ship_data.get('velocity')

        # Build the list to store the PlayerShip Projectiles
        self.bullets = []

        super().__init__(x, y, self.width, self.height, self.image)

    def move(self, keys_pressed):
        if keys_pressed[pg.K_w] and self.y - self.vel > 0:  # Move up
            self.y -= self.vel
        if keys_pressed[pg.K_a] and self.x - self.vel > 0:  # Move left
            self.x -= self.vel
        if (
            keys_pressed[pg.K_s]
            and self.y + self.height + self.vel < height.get('screen')
        ):  # Move down
            self.y += self.vel
        if (
            keys_pressed[pg.K_d]
            and self.x + self.width + self.vel < width.get('screen')
        ):  # Move right
            self.x += self.vel

    def shoot(self, surface):
        #if key_pressed[pg.K_SPACE]:
        bullet = Projectile(self.x + self.width / 2 - 5, self.y + self.height / 2, 10)
        self.bullets.append(bullet)
        for bull in self.bullets:
            bull.draw(surface)


    def collide_bullets(self, meteors, enemies):
        for bullet in self.bullets:
            for enemy in enemies:
                if enemy.colliderect(bullet):
                    self.bullets.remove(bullet)
                elif bullet.y < 0:
                    self.bullets.remove(bullet)