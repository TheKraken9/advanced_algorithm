import tkinter as tk
import time
import random
from collections import deque
from tkinter import messagebox


def get_neighbors(state):
    n = int(len(state) ** 0.5)
    i = state.index(0)
    neighbors = []
    if i % n > 0:
        neighbors.append((i - 1, "Left"))
    if i % n < n - 1:
        neighbors.append((i + 1, "Right"))
    if i - n >= 0:
        neighbors.append((i - n, "Up"))
    if i + n < len(state):
        neighbors.append((i + n, "Down"))
    return neighbors


class PuzzleNode:
    def __init__(self, state, parent=None, move=""):
        self.state = state
        self.parent = parent
        self.move = move


def solve_puzzle(initial_state):
    goal_state = list(range(1, len(initial_state))) + [0]
    start_node = PuzzleNode(initial_state)
    queue = deque()
    queue.append(start_node)

    visited = set()
    visited.add(tuple(initial_state))

    while queue:
        current_node = queue.popleft()

        if current_node.state == goal_state:
            # Construct the sequence of states from initial node to final node
            solution = []
            moves = []
            while current_node:
                solution.append(current_node.state)
                moves.append(current_node.move)
                current_node = current_node.parent
            solution.reverse()
            moves.reverse()
            return solution, moves

        neighbors = get_neighbors(current_node.state)
        for neighbor_index, move in neighbors:
            new_state = current_node.state[:]
            new_state[current_node.state.index(0)] = new_state[neighbor_index]
            new_state[neighbor_index] = 0
            if tuple(new_state) not in visited:
                new_node = PuzzleNode(new_state, current_node, move)
                queue.append(new_node)
                visited.add(tuple(new_state))

    return None, None


def create_puzzle_gui():
    def solve():
        initial_state = [int(cell.get()) for cell in cells]
        solution, moves = solve_puzzle(initial_state)

        if solution:
            # Calculate the height of the solution window based on the number of steps
            height = len(solution) * 200  # Adjust the factor (20) to fit the desired height

            # Create a new window to display the solution with a specified width and height
            solution_window = tk.Toplevel(root)
            solution_window.title("Solution")
            solution_window.geometry(f"500x{height}")
            solution_window.lower(root)

            solution_text = tk.Text(solution_window, width=100, height=len(solution) * 30)
            solution_text.pack()
            solution_text.config(fg="black", font=("Courier", 18, "bold"))

            solution_text.insert(tk.END, "Initial State:\n")
            for k, state in enumerate(solution):
                step = k
                if step == 0:
                    state_str = "\n".join(
                        " ".join(f"{state[i]:2d}" for i in range(row * 3, row * 3 + 3)) for row in range(3))
                    solution_text.insert(tk.END, state_str + "\n\n")

            solution_text.insert(tk.END, f"Steps : {moves[len(moves) - 1]}\n\n")
            for i, state in enumerate(solution):
                step = i
                if step == 0:
                    continue
                state_str = "\n".join(
                    " ".join(f"{state[i]:2d}" for i in range(row * 3, row * 3 + 3)) for row in range(3))

                solution_text.insert(tk.END, f"Step {step}:\n")
                solution_text.insert(tk.END, state_str + "\n\n")

        else:
            messagebox.showinfo("No Solution", "No solution found.")

    def show_solution():
        initial_state = [int(cell.get()) for cell in cells]
        solution, moves = solve_puzzle(initial_state)

        if solution:
            taquin_window = tk.Tk()
            taquin_window.title("Taquin")
            taquin_window.geometry("350x350")
            taquin_window.lift(root)

            taquin_label = tk.Label(taquin_window, text="")
            taquin_label.pack()
            taquin_label.config(fg="black", font=("Courier", 18, "bold"))

            taquin_window.update()  # Mettre à jour l'affichage de la fenêtre
            time.sleep(1)  # Pause
            print("\033[K", end="")  # Effacer la ligne d'affichage précédente

            canvas = tk.Canvas(taquin_window, width=150, height=150)
            canvas.pack()

            for i, state in enumerate(solution):
                canvas.delete("all")  # Effacer le contenu précédent du canvas

                for row in range(3):
                    for col in range(3):
                        number = state[row * 3 + col]
                        x = col * 50 + 25
                        y = row * 50 + 25

                        if number == 0:
                            canvas.create_rectangle(x - 25, y - 25, x + 25, y + 25, fill="red")  # Colorer en rouge
                            canvas.create_text(x, y, text=str(number), font=("Courier", 18, "bold"))
                        else:
                            canvas.create_rectangle(x - 25, y - 25, x + 25, y + 25, fill="blue")
                            canvas.create_text(x, y, text=str(number), font=("Courier", 18, "bold"))

                taquin_window.update()  # Mettre à jour l'affichage de la fenêtre
                time.sleep(1)

        else:
            print("No solution found.")

    def randomize():
        random_state = random.sample(range(9), 9)
        for i, cell in enumerate(cells):
            cell.delete(0, tk.END)
            cell.insert(tk.END, random_state[i])

    root = tk.Tk()
    root.title("Puzzle Solver")

    cells = []
    for i in range(9):
        cell = tk.Entry(root, width=5)
        cell.grid(row=i // 3, column=i % 3)
        cells.append(cell)

    randomize_button = tk.Button(root, text="Randomize", command=randomize)
    randomize_button.grid(row=9, column=0, columnspan=3, pady=10)

    solve_button = tk.Button(root, text="Solve", command=solve)
    solve_button.grid(row=10, column=0, columnspan=3, pady=10)

    show_solution_button = tk.Button(root, text="Show Solution", command=show_solution)
    show_solution_button.grid(row=11, column=0, columnspan=3, pady=10)

    root.mainloop()


if __name__ == '__main__':
    create_puzzle_gui()
