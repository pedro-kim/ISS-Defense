import pygame
from constants.images import space_background_img, keys_img
from constants.buttons import button_return

def render_instructions_screen(surface):
    
    surface.blit(space_background_img.get("space_background"), (0, 0))
    surface.blit(keys_img.get("wasd"), (100, 100))
    surface.blit(keys_img.get("space"), (100, 500))

    button_return.draw(surface)
    pygame.display.update()