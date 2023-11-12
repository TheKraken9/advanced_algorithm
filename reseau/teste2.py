import heapq
import networkx as nx
import matplotlib.pyplot as plt
import webbrowser
import requests


class Node:
    def __init__(self, ip, domains):
        self.ip = ip
        self.domains = domains

    def add_neighbor(self, neighbor, domain, cost):
        self.domains.append((neighbor, domain, cost))

    def get_neighbors(self):
        return self.domains

    def __str__(self):
        return self.ip


def dijkstra(graph, start, end_domain):
    distances = {node: float('inf') for node in graph}
    distances[start] = 0
    previous_nodes = {}
    queue = [(0, start)]

    while queue:
        current_cost, current_node = heapq.heappop(queue)

        if any(domain == end_domain for _, domain, _ in graph[current_node].get_neighbors()):
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
        for neighbor, domain, cost in neighbors:
            new_cost = current_cost + cost
            if new_cost < distances[neighbor]:
                distances[neighbor] = new_cost
                previous_nodes[neighbor] = current_node
                heapq.heappush(queue, (new_cost, neighbor))

    return float('inf'), []


def display_graph(graph, path=None):
    G = nx.Graph()

    for node in graph:
        neighbors = graph[node].get_neighbors()
        for neighbor, domain, cost in neighbors:
            G.add_edge(node, neighbor, domain=domain, cost=cost)

    pos = nx.spring_layout(G)
    nx.draw(G, pos, with_labels=False, node_color='lightblue', edge_color='gray', font_weight='bold')

    node_labels = {}
    for node in graph:
        domains = [domain for _, domain, _ in graph[node].get_neighbors()]
        node_labels[node] = '\n'.join([node] + domains)

    nx.draw_networkx_labels(G, pos, labels=node_labels, font_size=6)  # Spécifier la taille de police (par exemple 10)

    edge_labels = {(u, v): str(attr['cost']) for u, v, attr in G.edges(data=True)}
    nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels)

    if path:
        path_edges = [(path[i], path[i + 1]) for i in range(len(path) - 1)]
        nx.draw_networkx_edges(G, pos, edgelist=path_edges, edge_color='red', width=2.0)

        if path_edges:
            last_node = path_edges[-1][1]
            domain = None
            for neighbor, neighbor_domain, _ in graph[last_node].get_neighbors():
                if neighbor == path_edges[-1][0]:
                    domain = neighbor_domain
                    break
            if domain:
                webbrowser.open_new_tab(domain)

    plt.show()


graph = {
    '192.168.12.1': Node('192.168.12.1', [('168.152.14.12', 'https://www.google.com', 10),
                                          ('145.125.135.12', 'https://www.facebook.com', 5)]),
    '168.152.14.12': Node('168.152.14.12', [('145.125.135.12', 'https://www.youtube.com', 2),
                                            ('124.123.142.14', 'https://www.facebook.com', 8)]),
    '145.125.135.12': Node('145.125.135.12', [('168.152.14.12', 'https://www.youtube.com', 2),
                                              ('145.124.12.2', 'https://www.twitter.com', 4)]),
    '145.124.12.2': Node('145.124.12.2', [('145.169.368.12', 'https://www.instagram.com', 6)]),
    '124.123.142.14': Node('124.123.142.14', [('145.169.368.12', 'https://www.linkedin.com', 3)]),
    '145.169.368.12': Node('145.169.368.12', [('192.168.12.1', 'https://www.google.com', 7),
                                              ('145.124.12.2', 'https://www.twitter.com', 4)])
}


def open_url(url):
    try:
        response = requests.get(url)
        if response.status_code == 200:  # Vérifie le code d'état de la réponse (200 pour une requête réussie)
            webbrowser.open(url)
        else:
            print("La requête a échoué avec le code d'état :", response.status_code)
    except requests.RequestException as e:
        print("Une erreur s'est produite lors de la requête :", str(e))


def remove_node(node_to_remove):
    del graph[node_to_remove]
    for node in graph.values():
        node.domains = [(neighbor, domain, cost) for neighbor, domain, cost in node.domains if
                        neighbor != node_to_remove]


start_node = '192.168.12.1'
end_domain = 'https://www.instagram.com'

if __name__ == '__main__':
    url = end_domain
    # remove_node('145.125.135.12')
    least_cost, least_cost_path = dijkstra(graph, start_node, end_domain)
    if least_cost != float('inf'):
        print("Coût du chemin le moins coûteux :", least_cost)
        print("Chemin emprunté :", least_cost_path)
        open_url(url)
    else:
        print("Aucun chemin trouvé")

    display_graph(graph, least_cost_path)
