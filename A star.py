import heapq

def astar(graph, start, goal, cost_matrix, heuristic_values):

    # Initialize the open and closed sets
    open_set = []
    closed_set = set()

    # Initialize the start node
    heapq.heappush(open_set, (heuristic_values[start], 0, start, [start]))

    # Iterate until the open set is empty or the goal is reached
    while open_set:
        # Get the node with the lowest cost
        f_cost, g_cost, current_node, path = heapq.heappop(open_set)

        # Check if the goal is reached
        if current_node == goal:
            return path

        # Add the current node to the closed set
        closed_set.add(current_node)

        # Explore the neighbors of the current node
        for neighbor in graph[current_node]:
            if neighbor not in closed_set:
                # Calculate the new cost to reach the neighbor
                new_g_cost = g_cost + cost_matrix[current_node][neighbor]
                new_h_cost = heuristic_values[neighbor]
                new_f_cost = new_g_cost + new_h_cost

                # Add the neighbor to the open set
                heapq.heappush(open_set, (new_f_cost, new_g_cost, neighbor, path + [neighbor]))

    # If the goal cannot be reached, return None
    return None

# Example usage
graph = {
    'A': ['B', 'C'],
    'B': ['A', 'D', 'E'],
    'C': ['A', 'F'],
    'D': ['B'],
    'E': ['B', 'F'],
    'F': ['C', 'E']
}

cost_matrix = {
    'A': {'A': 0, 'B': 12, 'C': 10, 'D': 0, 'E': 0, 'F': 0},
    'B': {'A': 12, 'B': 0, 'C': 0, 'D': 9, 'E': 8, 'F': 0},
    'C': {'A': 10, 'B': 0, 'C': 0, 'D': 0, 'E':0, 'F': 6},
    'D': {'A': 0, 'B': 9, 'C': 0, 'D': 0, 'E': 0, 'F': 0},
    'E': {'A': 0, 'B': 8, 'C': 0, 'D': 0, 'E': 0, 'F': 2},
    'F': {'A': 0, 'B': 0, 'C': 6, 'D': 0, 'E': 2, 'F': 0}
}

heuristic_values = {
    'A': 15,
    'B': 10,
    'C': 5,
    'D': 7,
    'E': 3,
    'F': 0
}

start_node = 'E'
goal_node = 'A'

path = astar(graph, start_node, goal_node, cost_matrix, heuristic_values)
if path:
    print(f"Shortest path from {start_node} to {goal_node}: {' -> '.join(path)}")
else:
    print(f"No path found from {start_node} to {goal_node}")


