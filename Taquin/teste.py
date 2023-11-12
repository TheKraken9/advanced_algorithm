import tkinter as tk
import time
from collections import deque
from tkinter import messagebox


def get_neighbors(state):
    n = int(len(state) ** 0.25)
    i = state.index(0)
    neighbors = []
    if i % n > 0:
        neighbors.append((i - 1, "Left "))
    if i % n < n - 1:
        neighbors.append((i + 1, "Right "))
    if i - n >= 0:
        neighbors.append((i - n, "Up "))
    if i + n < len(state):
        neighbors.append((i + n, "Down "))
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
            new_node = PuzzleNode(new_state, current_node, current_node.move + move)
            queue.append(new_node)

    return None, None


def print_state(state):
    n = int(len(state) ** 0.25)
    for i in range(0, len(state), n):
        print(" ".join(map(str, state[i:i + n])))


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
                    state_str = "\n".join(" ".join(map(str, state[j:j + 4])) for j in range(0, len(state), 4))
                    solution_text.insert(tk.END, state_str + "\n\n")
                    # solution_text.insert(tk.END, f"Moves: {move}\n\n")

            solution_text.insert(tk.END, f"Steps : {moves[len(moves) - 1]}\n\n")
            for i, state in enumerate(solution):
                step = i
                if step == 0:
                    continue
                state_str = "\n".join(" ".join(map(str, state[j:j + 4])) for j in range(0, len(state), 4))

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
            taquin_window.geometry("400x400")
            taquin_window.lift(root)

            taquin_label = tk.Label(taquin_window, text="")
            taquin_label.pack()
            taquin_label.config(fg="black", font=("Courier", 18, "bold"))

            taquin_window.update()  # Mettre à jour l'affichage de la fenêtre
            time.sleep(1)  # Pause
            print("\033[K", end="")  # Effacer la ligne d'affichage précédente

            canvas = tk.Canvas(taquin_window, width=300, height=300)
            canvas.pack()

            for i, state in enumerate(solution):
                canvas.delete("all")  # Effacer le contenu précédent du canvas

                for row in range(4):
                    for col in range(4):
                        number = state[row * 4 + col]
                        x = col * 30 + 15
                        y = row * 30 + 15

                        if number == 0:
                            canvas.create_rectangle(x - 15, y - 15, x + 15, y + 15, fill="red")  # Colorer en rouge
                            canvas.create_text(x, y, text=str(number), font=("Courier", 18, "bold"))
                        else:
                            canvas.create_rectangle(x - 15, y - 15, x + 15, y + 15)
                            canvas.create_text(x, y, text=str(number), font=("Courier", 18, "bold"))

                taquin_window.update()  # Mettre à jour l'affichage de la fenêtre
                time.sleep(1)

        else:
            print("No solution found.")

    def solve_and_show():
        solve()
        show_solution()

    root = tk.Tk()
    root.title("Puzzle Solver")

    cells = []
    for i in range(16):
        cell = tk.Entry(root, width=5)
        cell.grid(row=i // 4, column=i % 4)
        cells.append(cell)

    solve_button = tk.Button(root, text="Solve", command=solve_and_show)
    solve_button.grid(row=16, column=0, columnspan=4)

    root.mainloop()


if __name__ == '__main__':
    create_puzzle_gui()
