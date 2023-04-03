import os
import pygame as pg
from constants.dimensions import width,height

background_img = {
    "first_background": pg.transform.scale(
        pg.image.load(os.path.join("Images", "background.png")), (width.get("screen"), height.get("screen"))
    )
}

iss_img = {
    "first_iss":pg.transform.scale(
        pg.image.load(os.path.join("Images", "Station Center.png")),
        (width.get("iss"), height.get("iss")),
    )
}

spaceships_img = {
    # PLAYER SPACESHIPS #
    "player_red2":pg.transform.scale(
        pg.image.load(os.path.join("Images", "playerShip2_red.png")),
        (width.get("spaceship"), height.get("spaceship"))
    ),
    "player_blue3":pg.transform.scale(
        pg.image.load(os.path.join("Images", "playerShip3_blue.png")),
        (width.get("spaceship"), height.get("spaceship")),
    ),
    # ENEMY SPACESHIPS #
    "enemy_black2": pg.transform.scale(
        pg.image.load(os.path.join("Images", "enemyBlack2.png")),
        (width.get("spaceship"), height.get("spaceship")),
    )
}

bullets_img = {
    # PLAYER BULLETS (facing upwards) #
    "player_blue": pg.transform.scale(
        pg.image.load(os.path.join("Images", "laserBlue16.png")),
        (width.get("bullet"), height.get("bullet")),
    ),
    "player_green": pg.transform.scale(
        pg.image.load(os.path.join("Images", "laserGreen13.png")),
        (width.get("bullet"), height.get("bullet")),
    ),
    # ENEMY BULLETS (facing downwards) #
    "enemy_red": pg.transform.rotate(
        pg.transform.scale(pg.image.load(os.path.join("Images", "laserRed16.png")), (width.get("bullet"), height.get("bullet"))),
        180,
    )
}

meteors_img = {
    "brown1": pg.transform.scale(
        pg.image.load(os.path.join("Images", "meteorBrown_big1.png")),
        (width.get("meteor"), height.get("meteor")),
    )
}
