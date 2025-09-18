# Goals for this version
# Make the window resizable, with the grid being 80% of the screen when resized.

# Imports
import pygame, sys
import numpy as np

# Variables
w, h = 800, 800
x, y = 20, 20 # size in cells
grid_size = 0.8 #as proportion of screen (0 <= x <= 1)
flags = pygame.RESIZABLE 
pygame.init()
screen = pygame.display.set_mode((w, h), flags)
clock = pygame.time.Clock()

# Mainloop
def main():
    while True:
        # Poll for events
        for event in pygame.event.get():
            # Handles exit
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            """# Handles resizing
            if event.type == pygame.VIDEORESIZE:
                neww, newh = event.w, event.h
                resize_grid(neww, newh, grid_size)
                pygame.display.flip()"""
        # Render visualiser   
        screen.fill("black")
        draw_maze(maze_grid, screen, grid_size)


        # Flips the display to put work on screen:
        pygame.display.flip()

        clock.tick(60) # limits FPS to 60

# MIsc functions

# Fills 80% of the screen with a x, y grid at the center
# grid stays square

"""def fill_grid(x, y, grid_size):
    global w, h
    min_dim = min(w, h) # returns integer for 
    # base offsets from the smaller dimension
    size = grid_size*min_dim
    cw, ch = size/x, size/y
    offsetw, offseth = (w-size)/2, (h-size)/2
    for i in range(x+1):
        pygame.draw.line(screen, "cyan", (offsetw + (i*cw), offseth), (offsetw + (i*cw), offseth+size))
    for j in range(y+1):
        pygame.draw.line(screen, "cyan", (offsetw, offseth + (j*ch)), (offsetw + size, offseth + (j*ch)))


def resize_grid(neww, newh, grid_size):
    global w, h
    w, h = neww, newh
    newx, newy = int(grid_size*neww/x), int(grid_size*newh//y)
    screen.fill("black")
    fill_grid(newx, newy, grid_size)
"""
def grid(x, y): # creates a numpy grid: x rows, y columns, with walls
    grid = np.full((x, y), 15, dtype=np.uint8)
    return grid

def draw_maze(grid, surface, grid_size):
    rows, cols = grid.shape[:2]
    min_dim = min(surface.get_width(), surface.get_height())
    size = grid_size * min_dim
    cw, ch = size / cols, size / rows
    offsetw, offseth = (surface.get_width() - size) / 2, (surface.get_height() - size) / 2

    for y in range(rows):
        for x in range(cols):
            cell = grid[y, x]

            # Bitmask to determine what walls to draw:
            if cell & 1: # top
                pygame.draw.line(surface, "cyan",
                                 (offsetw + x*cw, offseth + y*cw),
                                 (offsetw + (x+1)*cw, offseth + y*ch))
            if cell & 2: # right
                pygame.draw.line(surface, "cyan",
                                 (offsetw + (x+1)*cw, offseth + y*cw),
                                 (offsetw + (x+1)*cw, offseth + (y+1)*ch))
            if cell & 4: # bottom
                pygame.draw.line(surface, "cyan",
                                 (offsetw + x*cw, offseth + (y+1)*cw),
                                 (offsetw + (x+1)*cw, offseth + (y+1)*ch))
            if cell & 8: # left
                pygame.draw.line(surface, "cyan",
                                 (offsetw + x*cw, offseth + y*cw),
                                 (offsetw + x*cw, offseth + (y+1)*ch))

# Pre-run variables
maze_grid = grid(x, y)

# Tests
if __name__ == "__main__":
    main()
    