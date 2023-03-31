import pygame
import os

WIDTH, HEIGHT = 540, 960
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("ISS Defense")

BACKGROUND_IMAGE = (
    pygame.transform.scale(
        pygame.image.load(
            os.path.join('Images', 'background.png')
        ),
    (WIDTH,HEIGHT)
    )
)

WIN.blit(BACKGROUND_IMAGE, (0, 0))

pygame.display.update()

def draw_window(player_ship, enemy_ship, health_bar):


def main():

    run = True
    while run:

        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                run = False

    pygame.quit()


if __name__ == "__main__":
    main()
