from classes.GameObject import GameObject

from constants.images import meteors_img

class Meteor(GameObject):
    def __init__(self, x, y, meteors_data):

        self.x = x
        self.y = y
        self.type = meteors_data.get("type")
        self.width = meteors_data.get("width")
        self.height = meteors_data.get("height")
        self.health = meteors_data.get("health")
        self.image = meteors_img.get(type + "1")
        self.vel = meteors_data.get("velocity")
        super().__init__(self.x, self.y, self.width, self.height, self.image)

    def move(self):
        self.y += self.vel
