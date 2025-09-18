# Goals for this version
# Make the window resizable, with the grid being 80% of the screen when resized.

# Imports
import pygame, sys

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
            # Handles resizing
            if event.type == pygame.VIDEORESIZE:
                neww, newh = event.w, event.h
                resize_grid(neww, newh, grid_size)
                pygame.display.flip()
        # Render visualiser   
        screen.fill("black")
        fill_grid(x, y, grid_size)


        # Flips the display to put work on screen:
        pygame.display.flip()

        clock.tick(60) # limits FPS to 60


# Fills 80% of the screen with a x, y grid at the center
# grid stays square
"""def fill_grid(x, y):
    global w, h
    size = 0.8 # relative to screen
    cw, ch = (size*w)//x, (size*h)//x
    offset = (1-size)/2
    for i in range(x+1):        
        pygame.draw.line(screen, "cyan", (i*cw+(offset*w), offset*h), (i*cw+(offset*w), (1-offset)*h))
    for j in range(y+1):
        pygame.draw.line(screen, "cyan", (offset*w, j*ch+(offset*h)), ((1-offset)*w, j*ch+(offset*h)))
"""

def fill_grid(x, y, grid_size):
    global w, h
    min_dim = min(w, h) # returns integer for 
    # base offsets from the smaller dimension
    cw, ch = int(grid_size*min_dim//x), int(grid_size*min_dim//y)
    size = grid_size*min_dim
    offsetw, offseth = (w-size)/2, (h-size)/2
    for i in range(x+1):
        pygame.draw.line(screen, "cyan", (offsetw + (i*cw), offseth), (offsetw + (i*cw), offseth+size))
    for j in range(y+1):
        pygame.draw.line(screen, "cyan", (offsetw, offseth + (j*ch)), (offsetw + size, offseth + (j*ch)))
    

def resize_grid(neww, newh, grid_size):
    global w, h
    w, h = neww, newh
    newx, newy = int(grid_size*neww//x), int(grid_size*newh//y)
    screen.fill("black")
    fill_grid(newx, newy, grid_size)
    

# Tests
if __name__ == "__main__":
    main()
    