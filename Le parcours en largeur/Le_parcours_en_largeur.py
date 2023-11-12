from collections import deque

def bfs_shortest_path(graph, start, goal):
    queue = deque([(start, [])])
    visited = set()

    while queue:
        node, path = queue.popleft()
        visited.add(node)

        print("Visiting node:", node)

        if node == goal:
            return path  # Retourne le chemin si le nœud atteint est l'objectif

        for neighbor in graph[node]:
            if neighbor not in visited:
                queue.append((neighbor, path + [neighbor]))
                visited.add(neighbor)  # Ajouter le voisin à l'ensemble des nœuds visités
                print("Adding neighbor to the queue:", neighbor)

    return None

# Exemple d'utilisation
graph = {
    'A': ['B', 'C'],
    'B': ['A', 'C', 'D'],
    'C': ['A', 'B', 'D', 'E'],
    'D': ['B', 'C', 'E', 'F'],
    'E': ['C', 'D'],
    'F': ['D']
}

start_node = 'A'
goal_node = 'F'

if __name__ == '__main__':
    shortest_path = bfs_shortest_path(graph, start_node, goal_node)
    print("Shortest path:", shortest_path)
