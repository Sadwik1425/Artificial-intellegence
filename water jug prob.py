def water_jug_problem(capacity_jug1, capacity_jug2, target_amount):
    state = (0, 0)  # Initial state (amount in jug1, amount in jug2)
    visited_states = set()  # To keep track of visited states

    def is_valid_state(state):
        return 0 <= state[0] <= capacity_jug1 and 0 <= state[1] <= capacity_jug2

    def pour(jug_from, jug_to, current_state):
        pour_amount = min(current_state[jug_from], capacity_jug2 - current_state[jug_to])
        new_state = list(current_state)
        new_state[jug_from] -= pour_amount
        new_state[jug_to] += pour_amount
        return tuple(new_state)

    def dfs(current_state):
        if current_state[0] == target_amount or current_state[1] == target_amount:
            return [current_state]

        visited_states.add(current_state)

        next_states = [
            pour(0, 1, current_state),
            pour(1, 0, current_state),
            pour(0, 0, current_state),
            pour(1, 1, current_state),
            (current_state[0], 0),  
            (0, current_state[1]),  
            (capacity_jug1, current_state[1]), 
            (current_state[0], capacity_jug2)   
        ]

        for next_state in next_states:
            if is_valid_state(next_state) and next_state not in visited_states:
                result = dfs(next_state)
                if result:
                    return [current_state] + result

        return None

    result = dfs(state)

    if result:
        print("Solution found:")
        for step, step_state in enumerate(result):
            print(f"Step {step + 1}: Jug1={step_state[0]}, Jug2={step_state[1]}")
    else:
        print("No solution found.")

# Example usage
capacity_jug1 = int(input("Enter the capacity of jug1: "))
capacity_jug2 = int(input("Enter the capacity of jug2: "))
target_amount = int(input("Enter the target amount: "))

water_jug_problem(capacity_jug1, capacity_jug2, target_amount)
