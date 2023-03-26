from GameObject import GameObject

class Ship(GameObject):
    def __init__(self, x, y, image):
        super().__init__(x, y, image)

    def shoot(self):
        