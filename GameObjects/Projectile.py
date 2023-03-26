from GameObject import GameObject

class Projectile(GameObject):
    def __init__(self, x, y, image):
        super().__init__(x, y, image)

    def collide(self, )