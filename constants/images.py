import pygame as pg
import os
from constants.dimensions import width_dimensions,height_dimensions

background_img = {
    "first_background": pg.transform.scale(
        pg.image.load(os.path.join("Images", "background.png")), (width_dimensions.get("screen"), height_dimensions.get("screen"))
    )
}


# Salvando os frames do planeta em uma lista
planet_frames = []
frames_img = pg.image.load(os.path.join("Images", "planet_background.png"))

for j in range(25):
    for i in range(81):
        #frames_img.subsurface(i*128,0,128,128),
        frame = pg.transform.scale(frames_img.subsurface(i*200,j*200,200,200),(width_dimensions.get("planet"), height_dimensions.get("planet")))
        planet_frames.append(frame)

planet_background_img = { "planet_background": planet_frames}

space_background_img = {
    "space_background": pg.transform.scale(
        pg.image.load(os.path.join("Images", "space_background.png")).subsurface(400,0,353,360), (width_dimensions.get("screen"), height_dimensions.get("screen"))
    )
}

iss_img = {
    "first_iss":pg.transform.scale(
        pg.image.load(os.path.join("Images", "Station Center.png")),
        (width_dimensions.get("iss"), height_dimensions.get("iss")),
    )
}

spaceships_img = {
    # PLAYER SPACESHIPS #
    "player_red2":pg.transform.scale(
        pg.image.load(os.path.join("Images", "playerShip2_red.png")),
        (width_dimensions.get("spaceship"), height_dimensions.get("spaceship"))
    ),
    "player_blue3":pg.transform.scale(
        pg.image.load(os.path.join("Images", "playerShip3_blue.png")),
        (width_dimensions.get("spaceship"), height_dimensions.get("spaceship")),
    ),
    # ENEMY SPACESHIPS #
    "enemy_black2": pg.transform.scale(
        pg.image.load(os.path.join("Images", "enemyBlack2.png")),
        (width_dimensions.get("spaceship"), height_dimensions.get("spaceship")),
    )
}

bullets_img = {
    # PLAYER BULLETS (facing upwards) #
    "player_blue": pg.transform.scale(
        pg.image.load(os.path.join("Images", "laserBlue16.png")),
        (width_dimensions.get("bullet"), height_dimensions.get("bullet")),
    ),
    "player_green": pg.transform.scale(
        pg.image.load(os.path.join("Images", "laserGreen13.png")),
        (width_dimensions.get("bullet"), height_dimensions.get("bullet")),
    ),
    # ENEMY BULLETS (facing downwards) #
    "enemy_red": pg.transform.rotate(
        pg.transform.scale(pg.image.load(os.path.join("Images", "laserRed16.png")), (width_dimensions.get("bullet"), height_dimensions.get("bullet"))),
        180,
    )
}

meteors_img = {
    "brown1": pg.transform.scale(
        pg.image.load(os.path.join("Images", "meteorBrown_big1.png")),
        (width_dimensions.get("meteor"), height_dimensions.get("meteor")),
    )
}
