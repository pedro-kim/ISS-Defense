import pygame
from constants.dimensions import height, width
from constants.health import health
from constants.velocities import velocities
from constants.sounds import sounds
from classes.GameObject import GameObject
from classes.Projectile import Projectile

class PlayerShip(GameObject):
    def __init__(self, x, y, image):
        self.width = width.get("spaceship")
        self.height = height.get("spaceship")
        self.bullets = []
        self.health = health.get("player_ship")
        self.vel = velocities.get("player_ship")
        super().__init__(x, y, self.width, self.height, image)

    def move(self, keys_pressed):
        if keys_pressed[pygame.K_w] and self.y - self.vel > 0:  # Move up
            self.y -= self.vel
        if keys_pressed[pygame.K_a] and self.x - self.vel > 0:  # Move left
            self.x -= self.vel
        if (
            keys_pressed[pygame.K_s]
            and self.y + self.height + self.vel < height.get('screen')
        ):  # Move down
            self.y += self.vel
        if (
            keys_pressed[pygame.K_d]
            and self.x + self.width + self.vel < width.get('screen')
        ):  # Move right
            self.x += self.vel

    def shoot(self, surface):
        #if key_pressed[pygame.K_SPACE]:
        bullet = Projectile(self.x + self.width / 2 - 5, self.y + self.height / 2, 10)
        self.bullets.append(bullet)
        sounds['bulllet_sound'].play()
        for bull in self.bullets:
            bull.draw(surface)


    #def collide(self):
