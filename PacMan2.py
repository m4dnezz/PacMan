import pygame
import sys

WIDTH = 1280
HEIGHT = 720
BLACK = (0, 0, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)
VERSION = "0.1.2"

maze_data = [
    ["#", "#", "#", "#", "#", "#", "#", "#", "#", "#", "#", "#", "#", "#", "#", "#"],
    ["#", ".", ".", ".", ".", ".", "#", ".", ".", ".", ".", ".", ".", ".", ".", "#"],
    ["#", "#", "#", "#", "#", ".", "#", ".", "#", "#", "#", "#", ".", "#", ".", "#"],
    ["#", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", "#", ".", "#", ".", "#"],
    ["#", ".", "#", "#", "#", "#", "#", ".", "#", ".", "#", "#", ".", "#", ".", "#"],
    ["#", ".", ".", ".", ".", ".", ".", ".", "#", ".", ".", ".", ".", ".", ".", "#"],
    ["#", ".", ".", ".", ".", ".", ".", ".", "#", ".", ".", ".", ".", ".", ".", "#"],
    ["#", "#", "#", "#", "#", "#", "#", "#", "#", "#", "#", "#", "#", "#", "#", "#"]
]


class Sprite(pygame.sprite.Sprite):  # Super Class made by pygame
    def __init__(self, image, startx, starty):
        super().__init__()

        self.image = pygame.image.load(image)
        self.rect = self.image.get_rect()

        self.rect.center = [startx, starty]

    def update(self):
        pass

    def draw(self, screen):
        screen.blit(self.image, self.rect)


class Player(Sprite):  # Player class, representing PacMan
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

    def get_position(self):
        return self.rect.x, self.rect.y

    def update(self, walls):
        key = pygame.key.get_pressed()  # Returns pressed keys
        # Collision detection, should probably be separate function
        collision = pygame.sprite.spritecollideany(self, walls)

        if collision and self.direction == "left":
            self.left = False
            self.move(self.speed, 0)  # Bounce back slightly (less likely to get stuck)
        if collision and self.direction == "right":
            self.right = False
            self.move(-self.speed, 0)  # Bounce back slightly
        if collision and self.direction == "up":
            self.up = False
            self.move(0, self.speed)  # Bounce back slightly
        if collision and self.direction == "down":
            self.down = False
            self.move(0, -self.speed)  # Bounce back slightly

        if key[pygame.K_LEFT] and self.left == True:  # What to do if left arrow is pressed
            self.move(-self.speed, 0)  # Move player
            self.move_left_img()  # Change image of player
            self.direction = "left"  # Store direction, used for collision
            self.right = True  # Reverts previous collision block
            self.down = True
            self.up = True
            if not pygame.mixer_music.get_busy():
                pygame.mixer_music.load("sound/pacman_chomp.wav")
                pygame.mixer_music.play(1)

        elif key[pygame.K_RIGHT] and self.right == True:  # What to do if right arrow is pressed
            self.move(self.speed, 0)
            self.move_right_img()
            self.direction = "right"
            self.left = True
            self.down = True
            self.up = True
            if not pygame.mixer_music.get_busy():
                pygame.mixer_music.load("sound/pacman_chomp.wav")
                pygame.mixer_music.play(1)

        elif key[pygame.K_UP] and self.up == True:  # What to do if up arrow is pressed
            self.move(0, -self.speed)
            self.move_up_img()
            self.direction = "up"
            self.down = True
            self.left = True
            self.right = True
            if not pygame.mixer_music.get_busy():
                pygame.mixer_music.load("sound/pacman_chomp.wav")
                pygame.mixer_music.play(1)

        elif key[pygame.K_DOWN] and self.down == True:  # What to do if down arrow is pressed
            self.move(0, self.speed)
            self.move_down_img()
            self.direction = "down"
            self.up = True
            self.left = True
            self.right = True
            if not pygame.mixer_music.get_busy():
                pygame.mixer_music.load("sound/pacman_chomp.wav")
                pygame.mixer_music.play(1)


class Wall(pygame.sprite.Sprite):
    def __init__(self, x, y, width, height):
        super().__init__()
        self.image = pygame.Surface([width, height])
        self.image.fill((0, 0, 255))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y


class Point(pygame.sprite.Sprite):
    def __init__(self, x, y, radius):
        super().__init__()
        self.radius = radius
        self.image = pygame.Surface([radius * 2, radius * 2], pygame.SRCALPHA)
        self.rect = self.image.get_rect(center=(x, y))

    def draw(self, screen):
        pygame.draw.circle(screen, YELLOW, self.rect.center, self.radius)


def main():
    pygame.init()
    pygame.mixer.init()
    pygame.display.set_caption(f"Pac-Man Game Version {VERSION}")
    pygame.mixer_music.load("sound/pacman_beginning.wav")
    pygame.mixer_music.play(1)
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    clock = pygame.time.Clock()
    player = Player(300, 300)

    cell_width = WIDTH // len(maze_data[0])
    cell_height = (HEIGHT // len(maze_data)) - 10  # This makes no sense but is needed (Top bar takes space?)
    dot_radius = min(cell_width, cell_height) // 8
    print(dot_radius)

    walls = pygame.sprite.Group()  # Create a group since we will create a LOT of wall-segments
    points = pygame.sprite.Group()  # Create a group of points

    for row in range(len(maze_data)):
        for col in range(len(maze_data[row])):
            if maze_data[row][col] == "#":
                x = col * cell_width
                y = row * cell_height
                wall = Wall(x, y, cell_height, cell_width)
                walls.add(wall)
            elif maze_data[row][col] == ".":
                x = col * cell_width + cell_height // 2
                y = row * cell_width + cell_height // 2
                dot = Point(x, y, dot_radius)
                points.add(dot)

    while True:
        screen.fill(BLACK) # Make screen Black
        pygame.event.pump() # internally process pygame event handlers
        player.update(walls)
        player.draw(screen) # Draw player
        walls.draw(screen) # Draw walls
        for dot in points: # Draw points
            dot.draw(screen)
        pygame.display.flip() # Update the full display Surface to the screen
        clock.tick(60) # Limits FPS (affects game speed aswell)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:  # if "X" is pressed on window, close application
                pygame.quit()
                sys.exit()


if __name__ == "__main__":
    main()

# TODO: Add interaction with "points"
# TODO: Add the ghost(s)
# TODO: Improve interface, sound controll, scoreboard, restart
# TODO: Player class and update function is WHACK, clean that shit up
