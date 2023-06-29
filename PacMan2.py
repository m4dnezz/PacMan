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
    def __init__(self, startx, starty):
        super().__init__("images/pacmanimgright.png", startx, starty)
        self.speed = 4
        self.facing_right = True

    def move(self, x ,y):
        self.rect.move_ip([x, y])

    def move_left_img(self):
        self.image = pygame.image.load("images/pacmanimgleft.png")

    def move_right_img(self):
        self.image = pygame.image.load("images/pacmanimgright.png")

    def move_up_img(self):
        self.image = pygame.image.load("images/pacmanimgup.png")

    def move_down_img(self):
        self.image = pygame.image.load("images/pacmanimgdown.png")

    def update(self):
        key = pygame.key.get_pressed()
        if key[pygame.K_LEFT]:
            self.move(-self.speed, 0)
            self.move_left_img()
        elif key[pygame.K_RIGHT]:
            self.move(self.speed, 0)
            self.move_right_img()
        elif key[pygame.K_UP]:
            self.move(0, -self.speed)
            self.move_up_img()
        elif key[pygame.K_DOWN]:
            self.move(0, self.speed)
            self.move_down_img()


class Wall(Sprite):
    def __init__(self, startx, starty):
        super().__init__("images/bricks.png", startx, starty )

class Ghost(Sprite):
    def __init__(self, startx, starty, image):
        super().__init__(image, startx, starty)


def main():
    pygame.init()
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    clock = pygame.time.Clock()
    player = Player(200, 200)
    walls = pygame.sprite.Group()
    for wls in range(0,WIDTH,28):
        walls.add(Wall(wls, HEIGHT-20))
        walls.add(Wall(wls, 20))
    for wls in range(0, HEIGHT, 28):
        walls.add(Wall(20, wls))
        walls.add(Wall(WIDTH-20, wls))


    while True:
        screen.fill(BACKGROUND)
        pygame.event.pump()
        player.update()
        player.draw(screen)
        walls.draw(screen)
        pygame.display.flip()
        clock.tick(60)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()


if __name__ == "__main__":
    main()