# Implementation 01 of Conway's Game of Life

import random
import os
import time

# Create random grid
def create_grid(rows, cols):
    grid = []
    for _ in range(rows):
        row = [random.choice([0, 1]) for _ in range(cols)]
        grid.append(row)
    return grid

# Print the grid
def print_grid(grid):
    for row in grid:
        print(''.join(['#' if cell else '.' for cell in row]))

# Count number of live neighbors for a given cell
def count_live_neighbors(grid, row, col):
    live_neighbors = 0
    rows, cols = len(grid), len(grid[0])

    # Check all eight neighbors
    for i in range(-1, 2):
        for j in range(-1, 2):
            if i == 0 and j == 0:
                continue  # Skip the current cell (a cell can't be its own neighbor)
            if 0 <= row + i < rows and 0 <= col + j < cols:
                live_neighbors += grid[row + i][col + j]

    return live_neighbors

# Update the grid based on the rules of the game
def update_grid(grid):
    new_grid = []
    rows, cols = len(grid), len(grid[0])

    for row in range(rows):
        new_row = []
        for col in range(cols):
            live_neighbors = count_live_neighbors(grid, row, col)
            if grid[row][col]:  # Cell is alive
                if live_neighbors < 2 or live_neighbors > 3:
                    new_row.append(0)  # Dies due to under- or overpopulation
                else:
                    new_row.append(1)  # Survives
            else:  # Cell is dead
                if live_neighbors == 3:
                    new_row.append(1)  # Becomes alive due to reproduction
                else:
                    new_row.append(0)  # Stays dead

        new_grid.append(new_row)

    return new_grid

# Clear terminal screen
def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

# Main function to run the game
def main(rows, cols, generations, delay):
    grid = create_grid(rows, cols)

    for _ in range(generations):
        clear_screen()
        print_grid(grid)
        grid = update_grid(grid)
        time.sleep(delay)

# Example usage
rows = 20
cols = 50
generations = 100
delay = 0.1

main(rows, cols, generations, delay)
