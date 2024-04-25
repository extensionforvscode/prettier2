import heapq

def best_first_search(graph, start, goal, heuristic_values):

    # Initialize the open and closed sets
    open_set = []
    closed_set = set()

    # Initialize the start node
    heapq.heappush(open_set, (heuristic_values[start], start, [start]))

    # Iterate until the open set is empty or the goal is reached
    while open_set:
        # Get the node with the lowest heuristic cost
        heuristic_cost, current_node, path = heapq.heappop(open_set)

        # Check if the goal is reached
        if current_node == goal:
            return path

        # Add the current node to the closed set
        closed_set.add(current_node)

        # Explore the neighbors of the current node
        for neighbor in graph[current_node]:
            if neighbor not in closed_set:
                # Add the neighbor to the open set
                heapq.heappush(open_set, (heuristic_values[neighbor], neighbor, path + [neighbor]))

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

heuristic_values = {
    'A': 15,
    'B': 10,
    'C': 5,
    'D': 7,
    'E': 3,
    'F': 0
}

start_node = 'F'
goal_node = 'A'

path = best_first_search(graph, start_node, goal_node, heuristic_values)
if path:
    print(f"Shortest path from {start_node} to {goal_node}: {' -> '.join(path)}")
else:
    print(f"No path found from {start_node} to {goal_node}")
