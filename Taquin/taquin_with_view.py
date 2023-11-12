import tkinter as tk
import time
import random
from collections import deque
from tkinter import messagebox


def get_neighbors(state): # récupérer les voisins
    n = int(len(state) ** 0.5) # calculer la taille du taquin
    i = state.index(0) # récupérer l'indice de la case vide
    neighbors = [] # initialiser la liste des voisins
    if i % n > 0: # si la case vide n'est pas sur la première colonne
        neighbors.append((i - 1, "Left")) # ajouter le voisin de gauche
    if i % n < n - 1: # si la case vide n'est pas sur la dernière colonne
        neighbors.append((i + 1, "Right")) # ajouter le voisin de droite
    if i - n >= 0: # si la case vide n'est pas sur la première ligne
        neighbors.append((i - n, "Up")) # ajouter le voisin du haut
    if i + n < len(state): # si la case vide n'est pas sur la dernière ligne
        neighbors.append((i + n, "Down")) # ajouter le voisin du bas
    return neighbors # retourner la liste des voisins


class PuzzleNode: # noeud du taquin
    def __init__(self, state, parent=None, move=""): # initialiser le noeud
        self.state = state # état du noeud
        self.parent = parent # noeud parent
        self.move = move # mouvement effectué pour arriver au noeud


def solve_puzzle(initial_state): # résoudre le taquin
    goal_state = list(range(1, len(initial_state))) + [0] # état final
    start_node = PuzzleNode(initial_state) # initialiser le noeud de départ
    queue = deque() # initialiser la file
    queue.append(start_node) # ajouter le noeud de départ à la file

    visited = set() # initialiser l'ensemble des noeuds visités
    visited.add(tuple(initial_state)) # ajouter le noeud de départ à l'ensemble des noeuds visités

    while queue: # tant que la file n'est pas vide
        current_node = queue.popleft() # récupérer le premier noeud de la file

        if current_node.state == goal_state: # si l'état du noeud est l'état final
            # Construct the sequence of states from initial node to final node
            solution = [] # initialiser la liste des états
            moves = [] # initialiser la liste des mouvements
            while current_node: # tant que le noeud courant n'est pas None
                solution.append(current_node.state) # ajouter l'état du noeud courant à la liste des états
                moves.append(current_node.move) # ajouter le mouvement effectué pour arriver au noeud courant à la liste des mouvements
                current_node = current_node.parent # récupérer le noeud parent du noeud courant
            solution.reverse() # inverser la liste des états
            moves.reverse() # inverser la liste des mouvements
            return solution, moves # retourner la liste des états et la liste des mouvements

        neighbors = get_neighbors(current_node.state) # récupérer les voisins du noeud courant
        for neighbor_index, move in neighbors: # pour chaque voisin
            new_state = current_node.state[:] # copier l'état du noeud courant
            new_state[current_node.state.index(0)] = new_state[neighbor_index] # échanger la case vide avec le voisin
            new_state[neighbor_index] = 0 # mettre la case vide à la place du voisin
            if tuple(new_state) not in visited: # si le nouvel état n'a pas été visité
                new_node = PuzzleNode(new_state, current_node, move) # créer un nouveau noeud
                queue.append(new_node) # ajouter le nouveau noeud à la file
                visited.add(tuple(new_state)) # ajouter le nouvel état à l'ensemble des états visités

    return None, None # retourner None si aucune solution n'a été trouvée


def create_puzzle_gui(): # créer l'interface graphique du taquin
    def solve(): # résoudre le taquin
        initial_state = [int(cell.get()) for cell in cells] # récupérer l'état initial du taquin
        solution, moves = solve_puzzle(initial_state) # résoudre le taquin

        if solution: # si une solution a été trouvée
            # Calculate the height of the solution window based on the number of steps
            height = len(solution) * 200  # Adjust the factor (20) to fit the desired height

            # Create a new window to display the solution with a specified width and height
            solution_window = tk.Toplevel(root) # créer une nouvelle fenêtre
            solution_window.title("Solution") # définir le titre de la fenêtre
            solution_window.geometry(f"500x{height}") # définir la taille de la fenêtre
            solution_window.lower(root) # mettre la fenêtre en arrière-plan

            solution_text = tk.Text(solution_window, width=100, height=len(solution) * 30) # créer un widget Text
            solution_text.pack() # afficher le widget Text
            solution_text.config(fg="black", font=("Courier", 18, "bold")) # configurer le widget Text

            solution_text.insert(tk.END, "Initial State:\n") # afficher l'état initial
            for k, state in enumerate(solution): # pour chaque état
                step = k # récupérer le numéro de l'étape
                if step == 0: # si l'étape est 0
                    state_str = "\n".join( # récupérer l'état sous forme de chaîne de caractères
                        " ".join(f"{state[i]:2d}" for i in range(row * 3, row * 3 + 3)) for row in range(3)) # récupérer les 3 premiers éléments de chaque ligne
                    solution_text.insert(tk.END, state_str + "\n\n") # afficher l'état

            solution_text.insert(tk.END, f"Steps : {moves[len(moves) - 1]}\n\n") # afficher le nombre d'étapes
            for i, state in enumerate(solution): # pour chaque état
                step = i + 1 # récupérer le numéro de l'étape
                if step == 0: # si l'étape est 0
                    continue # passer à l'étape suivante
                state_str = "\n".join( # récupérer l'état sous forme de chaîne de caractères
                    " ".join(f"{state[i]:2d}" for i in range(row * 3, row * 3 + 3)) for row in range(3)) # récupérer les 3 premiers éléments de chaque ligne

                solution_text.insert(tk.END, f"Step {step}:\n") # afficher le numéro de l'étape
                solution_text.insert(tk.END, state_str + "\n\n") # afficher l'état

        else:
            messagebox.showinfo("No Solution", "No solution found.") # afficher un message d'erreur

    def show_solution(): # afficher la solution
        initial_state = [int(cell.get()) for cell in cells] # récupérer l'état initial du taquin
        solution, moves = solve_puzzle(initial_state) # résoudre le taquin

        if solution: # si une solution a été trouvée
            taquin_window = tk.Tk() # créer une nouvelle fenêtre
            taquin_window.title("Taquin") # définir le titre de la fenêtre
            taquin_window.geometry("350x350") # définir la taille de la fenêtre
            taquin_window.lift(root) # mettre la fenêtre au premier plan

            taquin_label = tk.Label(taquin_window, text="") # créer un widget Label
            taquin_label.pack() # afficher le widget Label
            taquin_label.config(fg="black", font=("Courier", 18, "bold")) # configurer le widget Label

            taquin_window.update()  # Mettre à jour l'affichage de la fenêtre
            time.sleep(1)  # Pause
            print("\033[K", end="")  # Effacer la ligne d'affichage précédente

            canvas = tk.Canvas(taquin_window, width=150, height=150) # créer un widget Canvas
            canvas.pack() # afficher le widget Canvas

            for i, state in enumerate(solution): # pour chaque état
                canvas.delete("all")  # Effacer le contenu précédent du canvas

                for row in range(3): # pour chaque ligne
                    for col in range(3): # pour chaque colonne
                        number = state[row * 3 + col] # récupérer le numéro de la case
                        x = col * 50 + 25 # calculer la position x de la case
                        y = row * 50 + 25 # calculer la position y de la case

                        if number == 0:
                            canvas.create_rectangle(x - 25, y - 25, x + 25, y + 25, fill="red")  # Colorer en rouge
                            canvas.create_text(x, y, text=str(number), font=("Courier", 18, "bold")) # Afficher le numéro
                        else:
                            canvas.create_rectangle(x - 25, y - 25, x + 25, y + 25, fill="blue") # Colorer en bleu
                            canvas.create_text(x, y, text=str(number), font=("Courier", 18, "bold")) # Afficher le numéro

                taquin_window.update()  # Mettre à jour l'affichage de la fenêtre
                time.sleep(1) # Pause

        else:
            print("No solution found.") # afficher un message d'erreur

    def randomize(): # générer un état aléatoire
        random_state = random.sample(range(9), 9) # générer un état aléatoire
        for i, cell in enumerate(cells): # pour chaque case
            cell.delete(0, tk.END) # supprimer le contenu de la case
            cell.insert(tk.END, random_state[i]) # insérer le numéro de la case

    root = tk.Tk() # créer une nouvelle fenêtre
    root.title("Puzzle Solver") # définir le titre de la fenêtre

    cells = [] # créer une liste pour stocker les cases
    for i in range(9): # pour chaque case
        cell = tk.Entry(root, width=5) # créer un widget Entry
        cell.grid(row=i // 3, column=i % 3) # afficher le widget Entry
        cells.append(cell) # ajouter la case à la liste

    randomize_button = tk.Button(root, text="Randomize", command=randomize) # créer un widget Button
    randomize_button.grid(row=9, column=0, columnspan=3, pady=10) # afficher le widget Button

    solve_button = tk.Button(root, text="Solve", command=solve) # créer un widget Button
    solve_button.grid(row=10, column=0, columnspan=3, pady=10) # afficher le widget Button

    show_solution_button = tk.Button(root, text="Show Solution", command=show_solution) # créer un widget Button
    show_solution_button.grid(row=11, column=0, columnspan=3, pady=10) # afficher le widget Button

    root.mainloop() # lancer la boucle principale


if __name__ == '__main__':
    create_puzzle_gui() # créer l'interface graphique
