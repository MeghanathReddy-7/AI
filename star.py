import heapq

class Node:
    def __init__(self, name, g=0, h=0, parent=None):
        self.name = name
        self.g = g  # Cost from start to node
        self.h = h  # Heuristic cost from node to goal
        self.f = g + h  # Total cost
        self.parent = parent

    def __lt__(self, other):
        return self.f < other.f

def a_star_search(start, goal, graph, heuristic):
    open_list = []
    closed_list = set()

    start_node = Node(start, h=heuristic[start])
    goal_node = Node(goal, h=heuristic[goal])
    heapq.heappush(open_list, start_node)

    while open_list:
        current_node = heapq.heappop(open_list)
        closed_list.add(current_node.name)

        if current_node.name == goal:
            return reconstruct_path(current_node)

        for neighbor, cost in graph[current_node.name].items():
            if neighbor in closed_list:
                continue

            g_cost = current_node.g + cost
            h_cost = heuristic[neighbor]
            neighbor_node = Node(neighbor, g_cost, h_cost, current_node)

            if add_to_open(open_list, neighbor_node):
                heapq.heappush(open_list, neighbor_node)

    return None

def reconstruct_path(node):
    path = []
    while node:
        path.append(node.name)
        node = node.parent
    return path[::-1]

def add_to_open(open_list, neighbor_node):
    for node in open_list:
        if neighbor_node.name == node.name and neighbor_node.f >= node.f:
            return False
    return True

# Example usage
graph = {
    'A': {'B': 1, 'C': 3},
    'B': {'A': 1, 'D': 1},
    'C': {'A': 3, 'D': 2},
    'D': {'B': 1, 'C': 2, 'E': 1},
    'E': {'D': 1}
}

heuristic = {
    'A': 7,
    'B': 6,
    'C': 2,
    'D': 5,
    'E': 0
}

start = 'A'
goal = 'E'
path = a_star_search(start, goal, graph, heuristic)
print("Path found:", path)
