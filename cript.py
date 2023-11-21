from itertools import permutations

def is_valid(puzzle, solution):
    """
    Check if the current solution is valid for the given puzzle.
    """
    puzzle_vars = set("".join(puzzle))
    if len(puzzle_vars) != 10:
        return False  
    if solution[puzzle.index(puzzle[0])] == 0:
        return False  

    values = {var: solution[puzzle.index(var)] for var in puzzle_vars}
    
    send = values[puzzle[0]] * 1000 + values[puzzle[1]] * 100 + values[puzzle[2]] * 10 + values[puzzle[3]]
    more = values[puzzle[4]] * 1000 + values[puzzle[5]] * 100 + values[puzzle[6]] * 10 + values[puzzle[7]]
    money = values[puzzle[8]] * 10000 + values[puzzle[9]] * 1000 + values[puzzle[10]] * 100 + values[puzzle[11]] * 10 + values[puzzle[12]]

    return send + more == money

def solve_cryptarithmetic(puzzle):
    """
    Solve the Cryptarithmetic puzzle.
    """
    puzzle_vars = set("".join(puzzle))
    if len(puzzle_vars) > 10:
        print("Invalid puzzle. Too many unique letters.")
        return

    digits = range(10)
    for perm in permutations(digits, len(puzzle_vars)):
        solution = dict(zip(puzzle_vars, perm))
        if is_valid(puzzle, solution):
            print("Solution found:")
            for var in puzzle_vars:
                print(f"{var}: {solution[var]}")
            return

    print("No solution found.")


puzzle = ["S", "E", "N", "D", "M", "O", "R", "E", "M", "O", "N", "E", "Y"]
solve_cryptarithmetic(puzzle)
