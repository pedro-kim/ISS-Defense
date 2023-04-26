import pygame as pg

pg.mixer.init()

sounds = {
    "hit_sound": pg.mixer.Sound("assets/music/hit_sound.mp3"),
    "bulllet_sound": pg.mixer.Sound("assets/music/bullet_sound.wav")
}

sounds["hit_sound"].set_volume(0.5)