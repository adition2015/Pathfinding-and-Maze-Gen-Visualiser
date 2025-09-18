# Imports
import numpy as np

WALLS = {
    "top": 1,
    "right": 2,
    "bottom": 4,
    "left": 8
}

OPPOSITE = {
    "top": "bottom",
    "right": "left",
    "bottom": "top",
    "left": "right"
}

VECTORS = {
    (0, -1): "top",
    (1, 0): "right",
    (0, 1): "bottom",
    (-1, 0): "left"
}

# Misc Functions



# Maze Gen Functions
def depth_first_search(x, y): # x, y - grid width, grid height
    # grid array
    grid = np.full((x, y), 15, dtype=np.uint8)# fills a grid with 15; 1|2|4|8, so all walls filled

    # random cell coordinates
    cell_x = np.random.random_integers(0, x, 1)
    cell_y = np.random.random_integers(0, y, 1)

    #direction vectors:
    LEFT = [-1, 0]
    RIGHT = [1, 0]
    UP = [0, 1]
    DOWN = [0, -1]

    print()

    #while grid.find(0) != False:
        #pass

    

    

