from classes.GameObject import GameObject
from classes.Projectile import Projectile

class EnemyShip(GameObject):
    def __init__(self, x, y, width, height, image):
        self.width = width
        self.height = height
        self.health = 5
        self.bullets = []
        self.shoot_time = 0
        self.shoot_period = 1000
        super().__init__(x, y, self.width, self.height, image)

    def shoot(self, current_time, surface):
        if current_time - self.shoot_time > self.shoot_period:
            new_bullet = Projectile(self.x + self.width / 2 - 5, self.y + self.height / 2, -10)
            self.bullets.append(new_bullet)
            self.shoot_time = current_time
            new_bullet.draw(surface)
        