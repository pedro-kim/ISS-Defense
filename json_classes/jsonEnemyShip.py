from classes.GameObject import GameObject
from classes.Projectile import Projectile

from constants.dimensions import height

class EnemyShip(GameObject):
    def __init__(self, x, y, image, enemy_ship_data):
        self.x = x
        self.y = y
        self.image = image

        self.width = enemy_ship_data.get('width')
        self.height = enemy_ship_data.get('height')
        self.health = enemy_ship_data.get('health')
        self.vel = enemy_ship_data.get('velocity')

        self.bullets = []

        self.shoot_time = 0
        self.shoot_period = enemy_ship_data.get('shoot_period')
        super().__init__(self.x, self.y, self.width, self.height, self.image)

    #TODO: see if the shoot method should not draw (change Level.py also in level_draw())
    def shoot(self, current_time, surface):
        if current_time - self.shoot_time > self.shoot_period:
            new_bullet = Projectile(self.x + self.width / 2 - 5, self.y + self.height / 2, -10)
            self.bullets.append(new_bullet)
            self.shoot_time = current_time
            new_bullet.draw(surface)

    def move(self):
         self.y += self.vel
        
    def collide_bullets(self, player):
        for bullet in self.bullets:
            if player.colliderect(bullet):
                self.bullets.remove(bullet)
            elif bullet.y > height.get("screen"):
                    self.bullets.remove(bullet)