from constants.images import planet_background_img
from constants.dimensions import width, height

def render_planet(surface, frame):
    surface.blit(planet_background_img["planet_background"][frame], (
        (width["screen"] - width["planet"])/2,
        (height["screen"] - height["planet"])/2))
    frame += 1
    if frame >= 2025*4: frame = 0
    return frame