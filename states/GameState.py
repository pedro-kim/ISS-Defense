import pygame as pg
import json

class GameState():
    def __init__(self, screen, state_file):

        self.screen = screen

        with open(state_file, 'r') as f:
            self.state_data = json.load(f)