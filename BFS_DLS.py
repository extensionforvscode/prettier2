from collections import deque


def bfs(graph, start, goal):
    visited = set()
    queue = deque([(start, [start])])

    while queue:
        node, path = queue.popleft()
        if node not in visited:
            visited.add(node)
            if node == goal:
                return path
            for neighbor in graph[node]:
                queue.append((neighbor, path + [neighbor]))

    return None


def dls(graph, start, goal, depth_limit):
    visited = set()
    stack = [(start, [start], 0)]

    while stack:
        node, path, depth = stack.pop()
        if node not in visited:
            visited.add(node)
            if node == goal:
                return path
            if depth < depth_limit:
                for neighbor in graph[node]:
                    stack.append((neighbor, path + [neighbor], depth + 1))

    return None


# Example usage
graph = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F'],
    'D': [],
    'E': ['F'],

    # 'goal' = []
    # 'F': [],

}

# Breadth-First Search
bfs_path = bfs(graph, 'A', 'F')
if bfs_path:
    print("BFS Path:", " -> ".join(bfs_path))
else:
    print("BFS: No path found")

# Depth-Limited Search
dls_path = dls(graph, 'A', 'F', 2)
if dls_path:
    print("DLS Path:", " -> ".join(dls_path))
else:
    print("DLS: No path found within depth limit")