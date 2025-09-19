# Goals for this version
# Make the window resizable, with the grid being 80% of the screen when resized.

# Imports
import pygame, sys, json
import numpy as np
import maze_gen as mg

# Variables
w, h = 800, 800
x, y = 20, 20 # size in cells
grid_size = 0.8 #as proportion of screen (0 <= x <= 1)
flags = pygame.RESIZABLE 
screen = pygame.display.set_mode((w, h), flags)
clock = pygame.time.Clock()

# Mainloop
def main():
    pygame.init()
    while True:
        # Poll for events
        for event in pygame.event.get():
            # Handles exit
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
        # Render visualiser   
        screen.fill("black")
        try:
            maze_grid, current_cell, done = next(maze_gen) # generates next step of maze
        except StopIteration:
            pass
        #draw_maze(maze_grid, screen, grid_size, current_cell, done) # updates walls as grid walls change
        load_grid("maze_1.npy")
        # Flips the display to put work on screen:
        pygame.display.flip()

        clock.tick(60) # limits FPS to 60


# Misc functions
def save_grid(grid, filename): # saves grid as numpy array
    with open(filename, "wb") as f:
        np.save(f, grid)
        print(f"File saved in {filename}")
    

def grid(x, y): # creates a numpy grid: x rows, y columns, with walls
    grid = np.full((x, y), 15, dtype=np.uint8)
    return grid


def load_grid(filename):
    with open(filename, "rb") as f:
        grid = np.load(f)
    draw_maze(grid, screen, grid_size, None, None)      

def draw_maze(grid, surface, grid_size, current_cell, done):# Draws a maze, accounting for wall removal
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
    # Highlights current cell
    if current_cell:
        x, y = current_cell
        pygame.draw.rect(surface, "white", (offsetw + x*cw, offseth + y*ch, cw, ch))
    
    # Highlights start and end cells if done:
    if done:
        pygame.draw.rect(surface, "green", (offsetw, offseth, cw, ch)) # start cell
        pygame.draw.rect(surface, "red", (offsetw + (cols-1)*cw, offseth + (rows-1)*ch, cw, ch)) # end cell
        save_grid(grid, "maze_1.npy")

# Pre-run variables
maze_grid = grid(x, y)
maze_gen = mg.depth_first_search(maze_grid)

# Tests
if __name__ == "__main__":
    main()
    