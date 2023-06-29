import pygame
import sys

WIDTH = 1280
HEIGHT = 720
BACKGROUND = (0, 0, 0)


class Sprite(pygame.sprite.Sprite):
    def __init__(self, image, startx, starty):
        super().__init__()

        self.image = pygame.image.load(image)
        self.rect = self.image.get_rect()

        self.rect.center = [startx, starty]

    def update(self):
        pass

    def draw(self, screen):
        screen.blit(self.image, self.rect)

class Player(Sprite):
    def __init__(self, image, startx, starty):
        super().__init__(image, startx, starty)

class Box(Sprite):
    def __init__(self, image, startx, starty):
        super().__init__(image, startx, starty)


def main():
    pygame.init()
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    clock = pygame.time.Clock()
    player = Player("pacmanimg.png", 200, 200)

    while True:
        pygame.event.pump()
        player.update()
        screen.fill(BACKGROUND)
        pygame.display.flip()
        player.draw(screen)
        clock.tick(60)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()


if __name__ == "__main__":
    main()