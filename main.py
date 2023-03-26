import pygame

WIDTH, HEIGHT = 540, 960
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("ISS Defense")

FPS = 60

BACKGROUND_IMAGE = pygame.image.load("ISS-Defense/Images/background.png")

WIN.blit(BACKGROUND_IMAGE, (0, 0))

pygame.display.update()


def main():

    run = True
    while run:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

    pygame.quit()


if __name__ == "__main__":
    main()
