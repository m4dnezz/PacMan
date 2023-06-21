import pygame
import sys
import numpy as np
version = 1
pygame.init()
width, height = 800, 600
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption(f"Pac-Man Game Version {version}")

clock = pygame.time.Clock()
game_running = True

while game_running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    pygame.display.update()
    clock.tick(60)

    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        pass
    # Move Pac-Man left
    elif keys[pygame.K_RIGHT]:
        pass
    # Move Pac-Man right
    elif keys[pygame.K_UP]:
        pass
    # Move Pac-Man up
    elif keys[pygame.K_DOWN]:
        pass
    # Move Pac-Man down

    # TODO: Update game stats
    # TODO: Draw game screen
    # TODO: Implement logic (death, collision, ghosts, points)