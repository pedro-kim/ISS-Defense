import pygame

class Button:
    def __init__(self, x, y, width, height, color, text, font, font_color):
        self.rect = pygame.Rect(x, y, width, height)
        self.color = color
        self.text = text
        self.font_color = font_color
        self.font = font

    def draw(self, surface):
        pygame.draw.rect(surface, self.color, self.rect)
        font_surface = self.font.render(self.text, True, self.font_color)
        font_rect = font_surface.get_rect(center=self.rect.center)
        surface.blit(font_surface, font_rect)

    def is_clicked(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            if self.rect.collidepoint(event.pos):
                return True
        return False