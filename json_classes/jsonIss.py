import pygame as pg

from constants.dimensions import height, width
from constants.health import health
from constants.velocities import velocities

from classes.GameObject import GameObject

class Iss(GameObject):
    def __init__(self,image, iss_data):

        self.width = iss_data.get('width')
        self.height = iss_data.get('height')
        self.health = iss_data.get('health')
        self.vel = iss_data.get('velocity')

        self.x = (width.get("screen") - self.width) / 2
        self.y = height.get("screen") - self.height

        self.image = image

        super().__init__(self.x, self.y, self.width, self.height, self.image)

    def start(self):
        if self.y < height.get('screen'):
            self.y += self.vel