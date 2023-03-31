import pygame as pg
import os
from constants.dimensions import width_dimensions,height_dimensions

background_img = {
    "first_background": pg.transform.scale(
        pg.image.load(os.path.join("Images", "background.png")), (width_dimensions.get("screen"), height_dimensions.get("screen"))
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
