from constants.images import planet_background_img
from constants.dimensions import width, height

def render_planet(surface, frame):
    surface.blit(planet_background_img.get("planet_background")[frame[0]], (
        (width.get("screen") - width.get("planet"))/2,
        (height.get("screen") - height.get("planet"))/2))
    frame[0] += 1
    if frame[0] >= 2025*4: frame[0] = 0
