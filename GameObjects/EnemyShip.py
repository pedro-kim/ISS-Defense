import GameObject, Projectile

class EnemyShip(GameObject):
    def __init__(self, x, y, width, height, image):
        super().__init__(x, y, image)
        self.width = 55
        self.height = 40
        self.health = 5
        self.bullets = []
        self.shoot_time = 0
        self.shoot_delay = 1000

    def shoot(self, current_time):
        if current_time - self.shoot_time > self.shoot_delay:
            new_bullet = Projectile(self.x + self.width / 2 - 5, self.y + self.height / 2)
            self.bullets.append(new_bullet)
            self.shoot_time = current_time
        