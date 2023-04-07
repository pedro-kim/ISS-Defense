from states.GameState import GameState
import json

class Menu(GameState):
    def __init__(self,menu_file):
        with open(menu_file, 'r') as f:
            self.menu_data = json.load(f)
        
        self.buttons = self.menu_data['buttons']
        self.