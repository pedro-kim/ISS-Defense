import pygame
from constants.images import space_background_img
from constants.buttons import button_return

def render_instructions_screen(surface):
    
    surface.blit(space_background_img.get("space_background"), (0, 0))
    button_return.draw(surface)
    pygame.display.update()