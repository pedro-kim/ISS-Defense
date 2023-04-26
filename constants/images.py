import os
import pygame as pg
from constants.dimensions import width,height

background_img = {
    "first_background": pg.transform.scale(
        pg.image.load(os.path.join("assets", "images", "background.png")), (width.get("screen"), height.get("screen"))
    )
}


# Salvando os frames do planeta em uma lista
planet_frames = []
frames_img = pg.image.load(os.path.join("assets", "images", "planet_background.png"))

for j in range(25):
    for i in range(81):
        #frames_img.subsurface(i*128,0,128,128),
        frame = pg.transform.scale(frames_img.subsurface(i*200,j*200,200,200),(width.get("planet"), height.get("planet")))
        planet_frames.append(frame)

mult_planet_frames = []
for item in planet_frames:
    for i in range(4):
        mult_planet_frames.append(item)

planet_background_img = { "planet_background": mult_planet_frames}

space_background_img = {
    "space_background": pg.transform.scale(
        pg.image.load(os.path.join("assets", "images", "space_background.png")).subsurface(400,0,353,360), (width.get("screen"), height.get("screen"))
    )
}

iss_img = {
    "first_iss":pg.transform.scale(
        pg.image.load(os.path.join("assets", "images", "Station Center.png")),
        (width.get("iss"), height.get("iss")),
    )
}

spaceships_img = {
    # PLAYER SPACESHIPS #
    "player_red2":pg.transform.scale(
        pg.image.load(os.path.join("assets", "images", "playerShip2_red.png")),
        (width.get("spaceship"), height.get("spaceship"))
    ),
    "player_blue3":pg.transform.scale(
        pg.image.load(os.path.join("assets", "images", "playerShip3_blue.png")),
        (width.get("spaceship"), height.get("spaceship")),
    ),
    # ENEMY SPACESHIPS #
    "enemy_black2": pg.transform.scale(
        pg.image.load(os.path.join("assets", "images", "enemyBlack2.png")),
        (width.get("spaceship"), height.get("spaceship")),
    )
}

bullets_img = {
    # PLAYER BULLETS (facing upwards) #
    "player_blue": pg.transform.scale(
        pg.image.load(os.path.join("assets", "images", "laserBlue16.png")),
        (width.get("bullet"), height.get("bullet")),
    ),
    "player_green": pg.transform.scale(
        pg.image.load(os.path.join("assets", "images", "laserGreen13.png")),
        (width.get("bullet"), height.get("bullet")),
    ),
    # ENEMY BULLETS (facing downwards) #
    "enemy_red": pg.transform.rotate(
        pg.transform.scale(pg.image.load(os.path.join("assets", "images", "laserRed16.png")), (width.get("bullet"), height.get("bullet"))),
        180,
    )
}

meteors_img = {
    "brown1": pg.transform.scale(
        pg.image.load(os.path.join("assets", "images", "meteorBrown_big1.png")),
        (width.get("meteor"), height.get("meteor")),
    ),
    "grey1": pg.transform.scale(
        pg.image.load(os.path.join("assets", "images", "meteorGrey_big1.png")),
        (width.get("meteor"), height.get("meteor")),
    )
}

ui_img = {
    "digito_0":pg.transform.scale(
        pg.image.load(os.path.join("assets", "images", "numeral0.png")),
        (width.get("health_digit"), height.get("health_digit")),
    ),
    "digito_1":pg.transform.scale(
        pg.image.load(os.path.join("assets", "images", "numeral1.png")),
        (width.get("health_digit"), height.get("health_digit")),
    ),
    "digito_2":pg.transform.scale(
        pg.image.load(os.path.join("assets", "images", "numeral2.png")),
        (width.get("health_digit"), height.get("health_digit")),
    ),
    "digito_3":pg.transform.scale(
        pg.image.load(os.path.join("assets", "images", "numeral3.png")),
        (width.get("health_digit"), height.get("health_digit")),
    ),
    "digito_4":pg.transform.scale(
        pg.image.load(os.path.join("assets", "images", "numeral4.png")),
        (width.get("health_digit"), height.get("health_digit")),
    ),
    "digito_5":pg.transform.scale(
        pg.image.load(os.path.join("assets", "images", "numeral5.png")),
        (width.get("health_digit"), height.get("health_digit")),
    ),
    "digito_6":pg.transform.scale(
        pg.image.load(os.path.join("assets", "images", "numeral6.png")),
        (width.get("health_digit"), height.get("health_digit")),
    ),
    "digito_7":pg.transform.scale(
        pg.image.load(os.path.join("assets", "images", "numeral7.png")),
        (width.get("health_digit"), height.get("health_digit")),
    ),
    "digito_8":pg.transform.scale(
        pg.image.load(os.path.join("assets", "images", "numeral8.png")),
        (width.get("health_digit"), height.get("health_digit")),
    ),
    "digito_9":pg.transform.scale(
        pg.image.load(os.path.join("assets", "images", "numeral9.png")),
        (width.get("health_digit"), height.get("health_digit")),
    ),
    "digito_x":pg.transform.scale(
        pg.image.load(os.path.join("assets", "images", "numeralX.png")),
        (width.get("x_icon"), height.get("x_icon")),
    ),
    "player_icon":pg.transform.scale(
        pg.image.load(os.path.join("assets", "images", "playerLife2_red.png")),
        (width.get("player_icon"), height.get("player_icon")),
    )
}
keys_img = {
    "wasd":pg.transform.scale(
        pg.image.load(os.path.join("assets", "images", "keys.png")).subsurface(50,0,660,450),
        (350,250 )
    ),
    "space":pg.transform.scale(
        pg.image.load(os.path.join("assets", "images", "keys.png")).subsurface(50,450,660,160),
        (350,100 )
    )
}
