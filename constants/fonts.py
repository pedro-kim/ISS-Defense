import pygame, os

pygame.font.init()

root_directory = os.path.dirname(os.path.dirname(__file__))

button_font = pygame.font.Font(os.path.join(root_directory, "assets", 'fonts', 'RobotoMono-Light.ttf'), 30)

title_font = pygame.font.Font(os.path.join(root_directory, "assets", 'fonts', 'RobotoMono-Regular.ttf'), 54)

score_font = pygame.font.Font(os.path.join(root_directory, "assets", "fonts", "kenvector_future_thin.ttf"), 20)

history_font = pygame.font.Font(os.path.join(root_directory, "assets", 'fonts', 'RobotoMono-Light.ttf'), 18)