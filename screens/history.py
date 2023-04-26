import pygame
from classes.Button import Button
from constants.colors import colors
from constants.images import space_background_img
from constants.fonts import button_font


def render_history_screen(surface):
    button_return = Button(10, 10, 200, 50, colors.get("mustard"), "Retornar", button_font, (255, 255, 255))
    
    surface.blit(space_background_img.get("space_background"), (0, 0))
    button_return.draw(surface)
    pygame.display.update()

    return button_return