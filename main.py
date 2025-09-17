# Imports
import pygame, sys

# Variables
w, h = 800, 800
cw, ch = 20, 20
pygame.init()
screen = pygame.display.set_mode((w, h))
clock = pygame.time.Clock()

# Mainloop
def main():
    while True:
        # Poll for events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()   
        # Render visualiser   
        screen.fill("black")
        fill_grid(cw, ch)


        # Flips the display to put work on screen:
        pygame.display.flip()

        clock.tick(60) # limits FPS to 60


# Fills the screen with a x, y grid
def fill_grid(x, y):
    global w, h
    cw, ch = w/x, h/x
    for i in range(x+1):        
        pygame.draw.line(screen, "cyan", ((i)*cw, 0), ((i)*cw, h))
    for j in range(y+1):
        pygame.draw.line(screen, "cyan", (0, (j)*ch), (w, (j)*ch))

# Tests
if __name__ == "__main__":
    main()
    