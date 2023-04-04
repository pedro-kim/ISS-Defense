import os
import pygame as pg
from constants.dimensions import width,height

background_img = {
    "first_background": pg.transform.scale(
        pg.image.load(os.path.join("images", "background.png")), (width.get("screen"), height.get("screen"))
    )
}


# Salvando os frames do planeta em uma lista
planet_frames = []
frames_img = pg.image.load(os.path.join("images", "planet_background.png"))

for j in range(25):
    for i in range(81):
        #frames_img.subsurface(i*128,0,128,128),
        frame = pg.transform.scale(frames_img.subsurface(i*200,j*200,200,200),(width.get("planet"), height.get("planet")))
        planet_frames.append(frame)

planet_background_img = { "planet_background": planet_frames}

space_background_img = {
    "space_background": pg.transform.scale(
        pg.image.load(os.path.join("images", "space_background.png")).subsurface(400,0,353,360), (width.get("screen"), height.get("screen"))
    )
}

iss_img = {
    "first_iss":pg.transform.scale(
        pg.image.load(os.path.join("images", "Station Center.png")),
        (width.get("iss"), height.get("iss")),
    )
}

spaceships_img = {
    # PLAYER SPACESHIPS #
    "player_red2":pg.transform.scale(
        pg.image.load(os.path.join("images", "playerShip2_red.png")),
        (width.get("spaceship"), height.get("spaceship"))
    ),
    "player_blue3":pg.transform.scale(
        pg.image.load(os.path.join("images", "playerShip3_blue.png")),
        (width.get("spaceship"), height.get("spaceship")),
    ),
    # ENEMY SPACESHIPS #
    "enemy_black2": pg.transform.scale(
        pg.image.load(os.path.join("images", "enemyBlack2.png")),
        (width.get("spaceship"), height.get("spaceship")),
    )
}

bullets_img = {
    # PLAYER BULLETS (facing upwards) #
    "player_blue": pg.transform.scale(
        pg.image.load(os.path.join("images", "laserBlue16.png")),
        (width.get("bullet"), height.get("bullet")),
    ),
    "player_green": pg.transform.scale(
        pg.image.load(os.path.join("images", "laserGreen13.png")),
        (width.get("bullet"), height.get("bullet")),
    ),
    # ENEMY BULLETS (facing downwards) #
    "enemy_red": pg.transform.rotate(
        pg.transform.scale(pg.image.load(os.path.join("images", "laserRed16.png")), (width.get("bullet"), height.get("bullet"))),
        180,
    )
}

meteors_img = {
    "brown1": pg.transform.scale(
        pg.image.load(os.path.join("images", "meteorBrown_big1.png")),
        (width.get("meteor"), height.get("meteor")),
    ),
    "grey1": pg.transform.scale(
        pg.image.load(os.path.join("images", "meteorGrey_big1.png")),
        (width.get("meteor"), height.get("meteor")),
    )
}
