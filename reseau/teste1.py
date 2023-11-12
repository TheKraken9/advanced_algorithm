import heapq
import networkx as nx
import matplotlib.pyplot as plt
from urllib.parse import urlparse

class Node:
    def __init__(self, ip):
        self.ip = ip
        self.domains = {}

    def add_url(self, url, cost):
        domain = urlparse(url).netloc
        self.domains[domain] = cost

    def get_neighbors(self):
        return self.domains

    def __str__(self):
        return self.ip


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

        neighbors = graph[current_node].get_neighbors()
        for neighbor, cost in neighbors.items():
            new_cost = current_cost + cost
            if new_cost < distances[neighbor]:
                distances[neighbor] = new_cost
                previous_nodes[neighbor] = current_node
                heapq.heappush(queue, (new_cost, neighbor))

    return float('inf'), []


def display_graph(graph):
    G = nx.Graph()

    for node in graph:
        G.add_node(str(node))
        neighbors = graph[node].get_neighbors()
        for neighbor in neighbors:
            G.add_edge(str(node), str(neighbor))

    pos = nx.spring_layout(G)
    nx.draw(G, pos, with_labels=True, node_color='lightblue', edge_color='gray', font_weight='bold')
    nx.draw_networkx_edge_labels(G, pos)

    plt.show()


graph = {}

# Ajout des nœuds au graphe avec leurs adresses IP
graph['192.168.0.1'] = Node('192.168.0.1')
graph['192.168.0.2'] = Node('192.168.0.2')
graph['192.168.0.3'] = Node('192.168.0.3')
graph['192.168.0.4'] = Node('192.168.0.4')
graph['192.168.0.5'] = Node('192.168.0.5')
graph['192.168.0.6'] = Node('192.168.0.6')

# Ajout des domaines pour chaque nœud du graphe avec le coût associé
graph['192.168.0.1'].add_url('http://google.com', 10)
graph['192.168.0.1'].add_url('http://youtube.com', 5)
graph['192.168.0.2'].add_url('http://facebook.com', 2)
graph['192.168.0.2'].add_url('http://twitter.com', 8)
graph['192.168.0.3'].add_url('http://instagram.com', 2)
graph['192.168.0.3'].add_url('http://linkedin.com', 4)
graph['192.168.0.4'].add_url('http://amazon.com', 6)

start_node = '192.168.0.1'
end_node = '192.168.0.6'

if __name__ == '__main__':
    # Utilisation de l'algorithme de Dijkstra pour trouver le chemin le moins coûteux
    least_cost, least_cost_path = dijkstra(graph, start_node, end_node)
    if least_cost != float('inf'):
        print("Coût du chemin le moins coûteux:", least_cost)
        print("Chemin emprunté :", least_cost_path)
    else:
        print("Aucun chemin trouvé")

    # Affichage du graphe
    display_graph(graph)
