import pygame as pg
import numpy as np
import sys, os

class Game():
    def __init__(self):
        pg.init()
        self.screen = pg.display.set_mode((540,960))
        self.clock = pg.time.Clock()
                
    