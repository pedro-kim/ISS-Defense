from pygame import Rect

class GameObject(Rect):
    def __init__(self, x, y, width, height, image):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.image = image
        
    def draw(self, surface):
        surface.blit(self.image, (self.x, self.y))
    