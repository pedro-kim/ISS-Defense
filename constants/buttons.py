from classes.Button import Button
from constants.colors import colors
from constants.fonts import button_font, title_font

button_title = Button(170, 100, 200, 90, colors.get("black"), "ISS Defense", title_font, (255, 255, 255))

button_play = Button(170, 300, 200, 50, colors.get("red"), "Jogar", button_font, (255, 255, 255))

button_instructions = Button(170, 400, 200, 50, colors.get("black"), "Instrucoes", button_font, (255, 255, 255))

button_history = Button(170, 500, 200, 50, colors.get("black"), "Historia", button_font, (255, 255, 255))

button_pause = Button(10, 10, 50, 50, colors.get("mustard"), "Pausar", button_font, (255, 255, 255))

button_despause = Button(10, 10, 50, 50, colors.get("mustard"), "Despausar", button_font, (255, 255, 255))

button_return = Button(10, 10, 200, 50, colors.get("mustard"), "Retornar", button_font, (255, 255, 255))
