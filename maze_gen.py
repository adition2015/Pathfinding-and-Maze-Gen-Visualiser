# Imports
import numpy as np
import main

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

    grid[y, x] &= ~WALLS[direction] # remove wall from current
    grid[y+dy, x+dx] &= ~WALLS[opp] # remove wall from neighbour

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
            nx, ny, direction = np.random.choice(neighbours)
            remove_wall(grid, x, y, direction)
            stack.append((x, y)) # remember current cell for backtracking
            x, y = nx, ny # updates current cell
            visited[y, x] = True # marks previous cell as visited
        elif stack: # stack > is stack not empty?
            x, y = stack.pop()
        else:
            break

    return grid
        






    
    

# Tests
if __name__ == "__main__":
    test_grid = main.grid(20, 10)
    depth_first_search(test_grid)