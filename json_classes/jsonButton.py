import pygame as pg

class Button:
    def __init__(self, x, y, width, height, is_rect, image, color=None, text=None, font=None, font_color=None):
        self.rect = pg.Rect(x, y, width, height)
        self.x = x
        self.y = y
        self.is_rect = is_rect
        if self.is_rect:
            self.color = color
            self.text = text
            self.font_color = font_color
            self.font = font
        else: #image
            self.image = image

    def draw(self, surface):
        if self.is_rect:
            pg.draw.rect(surface, self.color, self.rect)
            font_surface = self.font.render(self.text, True, self.font_color)
            font_rect = font_surface.get_rect(center=self.rect.center)
            surface.blit(font_surface, font_rect)
        else:
            surface.blit(self.image, (self.x, self.y))

    def is_clicked(self, event):
        if event.type == pg.MOUSEBUTTONDOWN:
            if self.rect.collidepoint(event.pos):
                return True
        return False