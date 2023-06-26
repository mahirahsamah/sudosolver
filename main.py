import random

def generate_and_display_sudoku():
    sudoku_grid = [[0] * 9 for _ in range(9)]  # Initialize an empty Sudoku grid

    # Fill the Sudoku grid with random numbers
    for row in range(9):
        for col in range(9):
            sudoku_grid[row][col] = random.randint(0, 9)  # Generate a random number between 1 and 9, 0 means empty

    # Display the Sudoku grid
    for row in range(9):
        if row % 3 == 0 and row != 0:
            print("- - - - - - - - - - - -")

        for col in range(9):
            if col % 3 == 0 and col != 0:
                print("| ", end="")
            print(sudoku_grid[row][col], end=" ")
        print()
        
grid = generate_and_display_sudoku()

def find_empty_cell(grid):
    for row in range(9):
        for col in range(9):
            if grid[row][col]==0:
                return [row, col]
    return None
