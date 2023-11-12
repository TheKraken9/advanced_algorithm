from queue import PriorityQueue

def bfs_minimum_cost(graph, start, goal):
    queue = PriorityQueue()
    queue.put((0, start, []))
    visited = set()

    while not queue.empty():
        cost, node, path = queue.get()

        if node == goal:
            print("Minimum cost:", cost)  # Affiche le coût total du chemin si le nœud atteint est l'objectif
            return path  # Retourne le chemin si le nœud atteint est l'objectif

        if node not in visited:
            visited.add(node)

            for neighbor, edge_cost in graph[node]:
                if neighbor not in visited:
                    queue.put((cost + edge_cost, neighbor, path + [(node, neighbor)]))

    return None  # Aucun chemin trouvé jusqu'à l'objectif

# Exemple d'utilisation avec les coûts des arêtes
graph = {
    'A': [('B', 5), ('C', 7)],
    'B': [('A', 5), ('C', 3), ('D', 2)],
    'C': [('A', 7), ('B', 3), ('D', 4), ('E', 6)],
    'D': [('B', 2), ('C', 4), ('E', 8), ('F', 1)],
    'E': [('C', 6), ('D', 8)],
    'F': [('D', 1)]
}

start_node = 'A'
goal_node = 'F'

if __name__ == '__main__':
    minimum_cost_path = bfs_minimum_cost(graph, start_node, goal_node)
    print("Minimum cost path:", minimum_cost_path)
