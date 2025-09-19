# Imports
import numpy as np
import random


# bitmasks
WALLS = {"top": np.uint8(1),
         "right": np.uint8(2), 
         "bottom": np.uint8(4),
           "left": np.uint(8)}

OPPOSITE = {"top": "bottom",
            "right": "left", 
            "bottom": "top", 
            "left": "right"}

VECTORS = {"top": (0, -1), 
           "right": (1, 0), 
           "bottom": (0, 1), 
           "left": (-1, 0)}

# Misc Functions
def random_coords(grid):
    coords = [np.random.randint(0, dim) for dim in grid.shape[:2]]
    return coords

def get_unvisited_neighbours(x, y, grid, visited):
    neighbours = []
    for direction, (dx, dy) in VECTORS.items():
        nx, ny = x + dx, y + dy # neighbouring cell
        if 0 <= nx < grid.shape[1] and 0 <= ny < grid.shape[0]: # checks whether coordinate is within grid dims
            if not visited[ny, nx]: # checks whether cell has been visited
                neighbours.append((nx, ny, direction))
    return neighbours

def remove_wall(grid, x, y, direction):
    opp = OPPOSITE[direction]
    dx, dy = VECTORS[direction]

    # current cell
    grid[y, x] = grid[y, x] & (15 - WALLS[direction])

    # neighbor cell
    nx, ny = x + dx, y + dy
    if 0 <= nx < grid.shape[1] and 0 <= ny < grid.shape[0]:
        grid[ny, nx] = grid[ny, nx] & (15 - WALLS[opp])
    print(grid[y, x])
    print(grid[y+dy, x+dx])

# Maze Gen Functions
def depth_first_search(grid): 
    # Visited array, stores bool in same shape as grid
    visited = np.zeros(grid.shape, dtype=bool)

    # generate random coordinate from grid
    stack = []
    x, y = 0, 0 # start cell
    visited[y, x] = True

    while True:
        neighbours = get_unvisited_neighbours(x, y, grid, visited)
        if neighbours:
            nx, ny, direction = random.choice(neighbours)
            remove_wall(grid, x, y, direction)
            stack.append((x, y)) # remember current cell for backtracking
            x, y = nx, ny # updates current cell
            visited[y, x] = True # marks previous cell as visited
        elif stack: # stack > is stack not empty?
            x, y = stack.pop()
        else:
            break   
        yield grid
        






    
    

# Tests
if __name__ == "__main__":
    pass