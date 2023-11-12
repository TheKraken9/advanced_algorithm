import heapq


def dijkstra(graph, start, end):
    distances = {node: float('inf') for node in graph}
    distances[start] = 0
    previous_nodes = {}
    queue = [(0, start)]

    while queue:
        current_cost, current_node = heapq.heappop(queue)

        if current_node == end:
            path = []
            while current_node != start:
                path.append(current_node)
                current_node = previous_nodes[current_node]
            path.append(start)
            path.reverse()
            return current_cost, path

        if current_cost > distances[current_node]:
            continue

        neighbors = graph[current_node]
        for neighbor, cost in neighbors.items():
            new_cost = current_cost + cost
            if new_cost < distances[neighbor]:
                distances[neighbor] = new_cost
                previous_nodes[neighbor] = current_node
                heapq.heappush(queue, (new_cost, neighbor))

    return float('inf'), []


graph = {
    'Router1': {'Router2': 10, 'Router3': 5},
    'Router2': {'Router3': 2, 'Server1': 8},
    'Router3': {'Router2': 2, 'Router4': 4},
    'Router4': {'Server2': 6},
    'Server1': {},
    'Server2': {}
}

start_node = 'Router1'
end_node = 'Server2'

if __name__ == '__main__':
    # Utilisation de l'algorithme de Dijkstra pour trouver le chemin le moins coûteux
    least_cost, least_cost_path = dijkstra(graph, start_node, end_node)
    if least_cost != float('inf'):
        print("Coût du chemin le moins coûteux:", least_cost)
        print("Chemin emprunté :", least_cost_path)
    else:
        print("Aucun chemin trouvé")
