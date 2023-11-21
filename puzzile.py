import heapq
import itertools

class Puzzle:
    def __init__(self, state, parent=None, move=None, depth=0, cost=0):
        self.state = state
        self.parent = parent
        self.move = move
        self.depth = depth
        self.cost = cost
        self.key = self.calculate_key()

    def __lt__(self, other):
        return self.key < other.key

    def calculate_key(self):
        return self.cost + self.heuristic()

    def heuristic(self):
        # Calculate the Manhattan distance heuristic
        h = 0
        goal_state = [[0, 1, 2], [3, 4, 5], [6, 7, 8]]
        for i in range(3):
            for j in range(3):
                if self.state[i][j] != 0:
                    goal_row, goal_col = divmod(self.state[i][j] - 1, 3)
                    h += abs(i - goal_row) + abs(j - goal_col)
        return h

    def is_goal(self):
        return self.state == [[0, 1, 2], [3, 4, 5], [6, 7, 8]]

    def get_neighbors(self):
        neighbors = []
        i, j = next((i, j) for i, row in enumerate(self.state) for j, val in enumerate(row) if val == 0)
        for move in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
            new_i, new_j = i + move[0], j + move[1]
            if 0 <= new_i < 3 and 0 <= new_j < 3:
                new_state = [row[:] for row in self.state]
                new_state[i][j], new_state[new_i][new_j] = new_state[new_i][new_j], new_state[i][j]
                neighbors.append(Puzzle(new_state, self, move, self.depth + 1, self.cost + 1))
        return neighbors

def solve_puzzle(initial_state):
    initial_puzzle = Puzzle(initial_state)
    frontier = [initial_puzzle]
    explored = set()

    while frontier:
        current_puzzle = heapq.heappop(frontier)
        if current_puzzle.is_goal():
            return get_solution_path(current_puzzle)
        
        explored.add(tuple(map(tuple, current_puzzle.state)))

        for neighbor in current_puzzle.get_neighbors():
            if tuple(map(tuple, neighbor.state)) not in explored:
                heapq.heappush(frontier, neighbor)

    return None

def get_solution_path(goal_puzzle):
    path = []
    current_puzzle = goal_puzzle
    while current_puzzle:
        path.append((current_puzzle.state, current_puzzle.move))
        current_puzzle = current_puzzle.parent
    path.reverse()
    return path

def print_solution_path(solution_path):
    for step, (state, move) in enumerate(solution_path):
        print(f"Step {step + 1}: Move {move} =>")
        print_state(state)
        print()

def print_state(state):
    for row in state:
        print(row)
    print()

if __name__ == "__main__":
    initial_state = [
        [1, 2, 3],
        [4, 0, 5],
        [6, 7, 8]
    ]

    solution_path = solve_puzzle(initial_state)

    if solution_path:
        print("Solution found!")
        print_solution_path(solution_path)
    else:
        print("No solution found.")
