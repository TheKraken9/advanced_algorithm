from queue import PriorityQueue


def dijkstra(graph, start_node, end_node):
    distances = {node: float('inf') for node in graph}
    distances[start_node] = 0
    pq = PriorityQueue()
    pq.put((0, start_node))
    previous_nodes = {}

    while not pq.empty():
        current_distance, current_node = pq.get()

        if current_node == end_node:
            path = []
            while current_node != start_node:
                path.append(current_node)
                current_node = previous_nodes[current_node]
            path.append(start_node)
            path.reverse()
            return distances[end_node], path

        if current_distance > distances[current_node]:
            continue

        neighbors = graph[current_node]
        for neighbor, cost in neighbors.items():
            new_distance = current_distance + cost
            if new_distance < distances[neighbor]:
                distances[neighbor] = new_distance
                previous_nodes[neighbor] = current_node
                pq.put((new_distance, neighbor))

    return float('inf'), []


graph = {
    'A': {'B': 1, 'C': 3},
    'B': {'C': 1, 'D': 2},
    'C': {'D': 4, 'E': 6},
    'D': {'E': 1, 'F': 2},
    'E': {},
    'F': {}
}

start_node = 'A'
end_node = 'F'

if __name__ == '__main__':
    least_cost, least_cost_path = dijkstra(graph, start_node, end_node)
    if least_cost != float('inf'):
        print("Coût du chemin le moins coûteux (Dijkstra):", least_cost)
        print("Chemin emprunté :", least_cost_path)
    else:
        print("Aucun chemin trouvé (Dijkstra)")
