import heapq

def find_position(value, grid):
    for i, row in enumerate(grid):
        for j, tile in enumerate(row):
            if tile == value:
                return i, j

def manhattan_distance(state, goal_state):
    distance = 0
    for i in range(3):
        for j in range(3):
            if state[i][j] != 'X':
                goal_row, goal_col = find_position(state[i][j], goal_state)
                distance += abs(i - goal_row) + abs(j - goal_col)
    return distance

def print_configuration(matrix):
    for row in matrix:
        print(row)
    print()

def generate_successors(state):
    successors = []
    blank_position = None
    for i in range(3):
        for j in range(3):
            if state[i][j] == 'X':
                blank_position = (i, j)
                break
        if blank_position:
            break

    if blank_position:
        row, col = blank_position
        potential_moves = [
            (row - 1, col),
            (row, col - 1),
            (row, col + 1),
            (row + 1, col)
        ]

        for new_row, new_col in potential_moves:
            if 0 <= new_row < 3 and 0 <= new_col < 3:
                # copy the current state
                temp_state = [row.copy() for row in state]
                temp_state[row][col], temp_state[new_row][new_col] = temp_state[new_row][new_col], temp_state[row][col]
                successors.append(temp_state)

    return successors

def a_star(initial_state, goal_state):
    if initial_state == goal_state:
        return 0  # Already at the goal state

    open_list = [(manhattan_distance(initial_state, goal_state), 0, initial_state)]
    closed_set = set()

    while open_list:
        _, cost, current_state = heapq.heappop(open_list)

        if current_state == goal_state:
            print(f"Step {cost}:")
            print_configuration(current_state)
            return cost

        if tuple(map(tuple, current_state)) in closed_set:
            continue

        closed_set.add(tuple(map(tuple, current_state)))

        print(f"Step {cost}:")
        print_configuration(current_state)

        for successor in generate_successors(current_state):
            if tuple(map(tuple, successor)) not in closed_set:
                heapq.heappush(open_list, (cost + 1 + manhattan_distance(successor, goal_state), cost + 1, successor))

    return -1  # If no solution is found

# Example usage:
initial_configuration = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 'X']
]

goal_configuration = [
    ['X', 2, 3],
    [1, 4, 6],
    [7, 5, 8]
]

result = a_star(initial_configuration, goal_configuration)

if result != -1:
    print(f"Solution found in {result} steps.")
else:
    print("No solution found.")
