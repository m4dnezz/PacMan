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
        self.up = True
        self.down = True
        self.right = True
        self.left = True
        self.direction = None

    def move(self, x, y):
        self.rect.move_ip([x, y])

    def move_left_img(self):
        self.image = pygame.image.load("images/pacmanimgleft.png")

    def move_right_img(self):
        self.image = pygame.image.load("images/pacmanimgright.png")

    def move_up_img(self):
        self.image = pygame.image.load("images/pacmanimgup.png")

    def move_down_img(self):
        self.image = pygame.image.load("images/pacmanimgdown.png")

    def update(self, walls):
        key = pygame.key.get_pressed()
        collision = pygame.sprite.spritecollideany(self, walls)
        if collision and self.direction == "left":
            self.left = False
        if collision and self.direction == "right":
            self.right = False
        if collision and self.direction == "up":
            self.up = False
        if collision and self.direction == "down":
            self.down = False

        if key[pygame.K_LEFT] and self.left == True:
            self.move(-self.speed, 0)
            self.move_left_img()
            self.direction = "left"
            self.right = True
            if not pygame.mixer_music.get_busy():
                chomp_sound = pygame.mixer_music.load("sound/pacman_chomp.wav")
                pygame.mixer_music.play(1)
        elif key[pygame.K_RIGHT] and self.right == True:
            self.move(self.speed, 0)
            self.move_right_img()
            self.direction = "right"
            self.left = True
            if not pygame.mixer_music.get_busy():
                chomp_sound = pygame.mixer_music.load("sound/pacman_chomp.wav")
                pygame.mixer_music.play(1)
        elif key[pygame.K_UP] and self.up == True:
            self.move(0, -self.speed)
            self.move_up_img()
            self.direction = "up"
            self.down = True
            if not pygame.mixer_music.get_busy():
                chomp_sound = pygame.mixer_music.load("sound/pacman_chomp.wav")
                pygame.mixer_music.play(1)
        elif key[pygame.K_DOWN] and self.down == True:
            self.move(0, self.speed)
            self.move_down_img()
            self.direction = "down"
            self.up = True
            if not pygame.mixer_music.get_busy():
                chomp_sound = pygame.mixer_music.load("sound/pacman_chomp.wav")
                pygame.mixer_music.play(1)


class Wall(Sprite):
    def __init__(self, startx, starty):
        super().__init__("images/bricks.png", startx, starty)


class Ghost(Sprite):
    def __init__(self, startx, starty, image):
        super().__init__(image, startx, starty)


def main():
    pygame.init()
    pygame.mixer.init()
    intro_music = pygame.mixer_music.load("sound/pacman_beginning.wav")
    pygame.mixer_music.play(1)
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    clock = pygame.time.Clock()
    player = Player(200, 200)
    walls = pygame.sprite.Group()
    for wls in range(0, WIDTH, 28):
        walls.add(Wall(wls, HEIGHT - 20))
        walls.add(Wall(wls, 20))
    for wls in range(0, HEIGHT, 28):
        walls.add(Wall(20, wls))
        walls.add(Wall(WIDTH - 20, wls))

    while True:
        screen.fill(BACKGROUND)
        pygame.event.pump()
        player.update(walls)
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
