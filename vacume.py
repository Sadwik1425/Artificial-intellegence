import random

class VacuumCleaner:
    def __init__(self, rows, columns):
        self.rows = rows
        self.columns = columns
        self.grid = [[0] * columns for _ in range(rows)]  
        self.current_position = (0, 0)

    def place_dirty_cells(self, num_dirty_cells):
        for _ in range(num_dirty_cells):
            row = random.randint(0, self.rows - 1)
            col = random.randint(0, self.columns - 1)
            self.grid[row][col] = 1  

    def print_grid(self):
        for row in self.grid:
            print(row)
        print()

    def clean(self):
        while any(1 in row for row in self.grid):
            self.print_grid()
            print(f"Current position: {self.current_position}")
            if self.grid[self.current_position[0]][self.current_position[1]] == 1:
                print("Cleaning dirty cell...")
                self.grid[self.current_position[0]][self.current_position[1]] = 0  
            else:
                print("Cell is already clean.")
            self.move()

        print("All dirty cells cleaned.")

    def move(self):
        
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        random_direction = random.choice(directions)
        new_position = (
            self.current_position[0] + random_direction[0],
            self.current_position[1] + random_direction[1]
        )

    
        if 0 <= new_position[0] < self.rows and 0 <= new_position[1] < self.columns:
            self.current_position = new_position
            print("Moving to new position...")
        else:
            print("Cannot move to the new position. Staying in the current position.")
