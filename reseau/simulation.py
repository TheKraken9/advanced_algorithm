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
    distances = {node: float('inf') for node in graph}  # initialiser les distances à l'infini
    distances[start] = 0 # distance de départ = 0
    previous_nodes = {} # dictionnaire des noeuds précédents
    queue = [(0, start)] # file de priorité

    while queue: # tant que la file n'est pas vide
        current_cost, current_node = heapq.heappop(queue) # extraire le noeud de coût minimum

        if any(domain == end_domain for _, domain, _ in graph[current_node].get_neighbors()): # si le noeud est le noeud final
            path = [] # initialiser le chemin
            while current_node != start: # tant que le noeud n'est pas le noeud de départ
                path.append(current_node) # ajouter le noeud au chemin
                current_node = previous_nodes[current_node] # mettre à jour le noeud courant
            path.append(start) # ajouter le noeud de départ au chemin
            path.reverse() # inverser le chemin
            return current_cost, path # retourner le coût et le chemin

        if current_cost > distances[current_node]: # si le coût courant est supérieur à la distance du noeud courant
            continue # passer au noeud suivant

        neighbors = graph[current_node].get_neighbors() # récupérer les voisins du noeud courant
        for neighbor, domain, cost in neighbors: # pour chaque voisin
            new_cost = current_cost + cost # calculer le nouveau coût
            if new_cost < distances[neighbor]: # si le nouveau coût est inférieur à la distance du voisin
                distances[neighbor] = new_cost # mettre à jour la distance du voisin
                previous_nodes[neighbor] = current_node # mettre à jour le noeud précédent du voisin
                heapq.heappush(queue, (new_cost, neighbor)) # ajouter le voisin à la file de priorité

    return float('inf'), [] # retourner l'infini et une liste vide


def display_graph(graph, path=None): # afficher le graphe
    G = nx.Graph() # initialiser le graphe

    for node in graph: # pour chaque noeud
        neighbors = graph[node].get_neighbors() # récupérer les voisins
        for neighbor, domain, cost in neighbors: # pour chaque voisin
            G.add_edge(node, neighbor, domain=domain, cost=cost) # ajouter l'arête

    pos = nx.spring_layout(G) # positionner les noeuds
    nx.draw(G, pos, with_labels=False, node_color='lightblue', edge_color='gray', font_weight='bold', node_size=500) # dessiner le graphe

    node_labels = {} # initialiser les labels des noeuds
    for node in graph: # pour chaque noeud
        domains = [domain for _, domain, _ in graph[node].get_neighbors()] # récupérer les domaines
        node_labels[node] = '\n'.join([node] + domains) # ajouter le noeud et les domaines au label

    nx.draw_networkx_labels(G, pos, labels=node_labels, font_size=6)  # Spécifier la taille de police (par exemple 10)

    edge_labels = {(u, v): str(attr['cost']) for u, v, attr in G.edges(data=True)} # initialiser les labels des arêtes
    nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels) # dessiner les labels des arêtes

    if path: # si un chemin est spécifié
        path_edges = [(path[i], path[i + 1]) for i in range(len(path) - 1)] # récupérer les arêtes du chemin
        nx.draw_networkx_edges(G, pos, edgelist=path_edges, edge_color='red', width=2.0) # dessiner les arêtes du chemin

        if path_edges: # si le chemin n'est pas vide
            last_node = path_edges[-1][1] # récupérer le dernier noeud du chemin
            domain = None # initialiser le domaine
            for neighbor, neighbor_domain, _ in graph[last_node].get_neighbors(): # pour chaque voisin du dernier noeud
                if neighbor == path_edges[-1][0]: # si le voisin est le noeud précédent
                    domain = neighbor_domain # récupérer le domaine
                    break # sortir de la boucle
            if domain: # si le domaine est spécifié
                webbrowser.open_new_tab(domain) # ouvrir le domaine dans un nouvel onglet

    plt.show() # afficher le graphe


graph = { # initialiser le graphe
    '192.168.12.1': Node('192.168.12.1', [('168.152.14.12', 'https://www.google.com', 10),
                                          ('145.125.135.12', 'https://www.facebook.com', 5)]),
    '168.152.14.12': Node('168.152.14.12', [('145.125.135.12', 'https://www.youtube.com', 2),
                                            ('124.123.142.14', 'https://www.facebook.com', 8)]),
    '145.125.135.12': Node('145.125.135.12', [('168.152.14.12', 'https://www.youtube.com', 2),
                                              ('145.124.12.2', 'https://www.twitter.com', 4)]),
    '145.124.12.2': Node('145.124.12.2', [('145.169.368.12', 'https://www.instagram.com', 1)]),
    '124.123.142.14': Node('124.123.142.14', [('145.169.368.12', 'https://www.linkedin.com', 3)]),
    '145.169.368.12': Node('145.169.368.12', [('192.168.12.1', 'https://www.google.com', 7),
                                              ('145.124.12.2', 'https://www.twitter.com', 4)])
}


def open_url(url): # ouvrir une URL
    try:
        response = requests.get(url) # envoyer une requête GET
        if response.status_code == 200: # si la requête a réussi
            webbrowser.open(url) # ouvrir l'URL
        else:
            print("La requête a échoué avec le code d'état :", response.status_code) # afficher le code d'état
    except requests.RequestException as e: # si une erreur s'est produite lors de la requête
        print("Une erreur s'est produite lors de la requête :", str(e)) # afficher l'erreur


def remove_node(node_to_remove): # supprimer un noeud
    del graph[node_to_remove] # supprimer le noeud du graphe
    for node in graph.values(): # pour chaque noeud
        node.domains = [(neighbor, domain, cost) for neighbor, domain, cost in node.domains if
                        neighbor != node_to_remove] # supprimer le noeud des domaines des voisins


start_node = '192.168.12.1'
end_domain = 'https://www.instagram.com'

if __name__ == '__main__':
    url = end_domain
    # remove_node('145.125.135.12')
    least_cost, least_cost_path = dijkstra(graph, start_node, end_domain) # exécuter l'algorithme de Dijkstra
    if least_cost != float('inf'): # si un chemin a été trouvé
        print("Coût du chemin le moins coûteux :", least_cost) # afficher le coût du chemin le moins coûteux
        print("Chemin emprunté :", least_cost_path) # afficher le chemin emprunté
        open_url(url) # ouvrir l'URL
    else:
        print("Aucun chemin trouvé") # afficher qu'aucun chemin n'a été trouvé

    display_graph(graph, least_cost_path) # afficher le graphe
