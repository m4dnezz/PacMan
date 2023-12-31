import pygame
import sys
import numpy as np

version = 0.1
pygame.init()
width, height = 800, 600
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption(f"Pac-Man Game Version {version}")

clock = pygame.time.Clock()
game_running = True

# Set up colors for walls and dots
wall_color = (0, 0, 255)  # Blue color for walls
dot_color = (255, 255, 255)  # White color for dots
player_color = (255, 0, 0)

# Set up Maze
maze_data = [
    ["#", "#", "#", "#", "#", "#", "#", "#", "#", "#", "#", "#", "#", "#", "#", "#"],
    ["#", ".", ".", ".", ".", ".", "#", ".", ".", ".", ".", ".", ".", ".", ".", "#"],
    ["#", "#", "#", "#", "#", ".", "#", ".", "#", "#", "#", "#", ".", "#", ".", "#"],
    ["#", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", "#", ".", "#", ".", "#"],
    ["#", ".", "#", "#", "#", "#", "#", ".", "#", ".", "#", "#", ".", "#", ".", "#"],
    ["#", ".", ".", ".", ".", ".", ".", ".", "#", ".", ".", ".", ".", ".", ".", "#"],
    ["#", "#", "#", "#", "#", "#", "#", "#", "#", "#", "#", "#", "#", "#", "#", "#"],
]



class PlayerClass:
    def __init__(self):
        self.x = 70
        self.y = 85
        self.speed = 5

    def moveRight(self):
        self.x = self.x + self.speed

    def moveLeft(self):
        self.x = self.x - self.speed

    def moveUp(self):
        self.y = self.y - self.speed

    def moveDown(self):
        self.y = self.y + self.speed

    def get_pos(self):
        return self.x, self.y


class Maze:
    def __init__(self, maze_data):
        self.maze = maze_data
        self.rows = len(self.maze)
        self.columns = len(self.maze[0])

    def get_cell(self, row, col):
        """Get the value of a specific cell in the maze."""
        return self.maze[row][col]

    def set_cell(self, row, col, value):
        """Set the value of a specific cell in the maze."""
        self.maze[row][col] = value

    def is_valid_cell(self, row, col):
        """Check if the given cell coordinates are valid."""
        return 0 <= row < self.rows and 0 <= col < self.columns

    def is_wall(self, row, col):
        """Check if the given cell is a wall."""
        return self.get_cell(row, col) == "#"

    def is_dot(self, row, col):
        """Check if the given cell is a dot."""
        return self.get_cell(row, col) == "."

    def print_maze(self):
        """Print the maze grid."""
        for row in range(self.rows):
            for col in range(self.columns):
                print(self.maze[row][col], end=" ")
            print()


maze = Maze(maze_data)
player = PlayerClass()

# Set up cell dimensions
cell_width = width // maze.columns
cell_height = height // maze.rows

while game_running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    for row in range(maze.rows):
        for col in range(maze.columns):
            x = col * cell_width
            y = row * cell_height

            if maze.is_wall(row, col):
                pygame.draw.rect(screen, wall_color, (x, y, cell_width, cell_height))
            elif maze.is_dot(row, col):
                pygame.draw.circle(
                    screen,
                    dot_color,
                    (x + cell_width // 2, y + cell_height // 2),
                    cell_width // 10,
                )

    pygame.draw.circle(screen, (0,0,0), (player.get_pos()[0], player.get_pos()[1]), 20)
    pygame.draw.circle(screen, player_color, (player.get_pos()[0], player.get_pos()[1]), 20)
    pygame.display.update()
    clock.tick(60)

    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        player.moveLeft()
    # Move Pac-Man left
    elif keys[pygame.K_RIGHT]:
        player.moveRight()
    # Move Pac-Man right
    elif keys[pygame.K_UP]:
        player.moveUp()
    # Move Pac-Man up
    elif keys[pygame.K_DOWN]:
        player.moveDown()
    # Move Pac-Man down

