print("Mohd Jawwad Ali Farooqui,USN:1AY24AI070,SEC:O")
import numpy as np
import os
import time
WIDTH = 20
HEIGHT = 20
DELAY = 0.5
def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')
def print_grid(grid):
    clear_screen()
    for row in grid:
        print(''.join(['█' if cell else ' ' for cell in row]))
def count_neighbors(grid, x, y):
    total = 0
    for i in range(-1, 2):
        for j in range(-1, 2):
            if not (i == 0 and j == 0):
                ni = (x + i) % HEIGHT
                nj = (y + j) % WIDTH
                total += grid[ni][nj]
    return total
def next_generation(grid):
    new_grid = np.zeros((HEIGHT, WIDTH), dtype=int)
    for i in range(HEIGHT):
        for j in range(WIDTH):
            neighbors = count_neighbors(grid, i, j)
            if grid[i][j] == 1 and neighbors in [2, 3]:
                new_grid[i][j] = 1
            elif grid[i][j] == 0 and neighbors == 3:
                new_grid[i][j] = 1
    return new_grid
def main():
    grid = np.random.choice([0, 1], size=(HEIGHT, WIDTH), p=[0.8, 0.2])
    try:
        while True:
            print_grid(grid)
            grid = next_generation(grid)
            time.sleep(DELAY)
    except KeyboardInterrupt:
        print("\nSimulation ended.")
if __name__== "__main__":
    main()
