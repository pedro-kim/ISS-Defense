import pygame as pg

SPACESHIP_WIDTH, SPACESHIP_HEIGHT = 50, 40
WHITE_SPACESHIP_IMAGE = pg.image.load(os.path.join('ISS-Defense/Images','spaceship.png'))

WHITE_SPACESHIP = pg.transform.scale(WHITE_SPACESHIP_IMAGE,(SPACESHIP_WIDTH, SPACESHIP_HEIGHT))

class Spaceship:
    def __init__(self, x, y, width, height, vel=5 , health=100):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.vel = vel
        self.health = health
        self.ship_img = WHITE_SPACESHIP
        self.laser_img = None
        self.lasers = []

    def draw(self, win):
        win.blit()

    def move(self, keys_pressed, DISPLAY_WIDTH, DISPLAY_HEIGHT):
        if keys_pressed[pg.K_LEFT] and self.x - self.vel > 0:
            self.x -= self.vel
        if keys_pressed[pg.K_RIGHT] and self.x + self.vel + self.width < DISPLAY_WIDTH:
            self.x += self.vel
        if keys_pressed[pg.K_UP] and self.y - self.vel - self.height > 0:
            self.y -= self.vel
        if keys_pressed[pg.K_DOWN] and self.y + self.vel + 2*self.height + 40< DISPLAY_HEIGHT:
            self.y += self.vel