from GameObjects.GameObject import GameObject
import os, pygame

class Projectile(GameObject):
    def __init__(self, x, y):
        self.width = 10
        self.height = 20
        self.vel = 10
        self.image = pygame.transform.scale(
            pygame.image.load(os.path.join("Images", "laserGreen13.png")),
            (self.width, self.height),
        )
        super().__init__(x, y, self.width, self.height, self.image)

    def move(self):
        self.y -= self.vel
        