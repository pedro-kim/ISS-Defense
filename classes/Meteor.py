from classes.GameObject import GameObject
from constants.dimensions import width, height
from constants.velocities import velocities
from constants.health import health
from constants.images import meteors_img

class Meteor(GameObject):
    def __init__(self, x, y, type):

        if type not in ["brown", "grey"]:
            raise ValueError("Type must be 'brown' or 'grey'")
        self.x = x
        self.y = y
        self.type = type
        self.width = width.get("meteor")
        self.height = height.get("meteor")
        self.health = health.get(type + "_meteor")
        self.image = meteors_img.get(type + "1")
        self.vel = velocities.get("meteor")
        super().__init__(self.x, self.y, self.width, self.height, self.image)

    