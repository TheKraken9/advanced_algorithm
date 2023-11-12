from collections import deque


def get_neighbors(state):
    n = int(len(state) ** 0.5)
    i = state.index(0)
    neighbors = []
    if i % n > 0:
        neighbors.append((i - 1, "Gauche "))
    if i % n < n - 1:
        neighbors.append((i + 1, "Droite "))
    if i - n >= 0:
        neighbors.append((i - n, "Haut "))
    if i + n < len(state):
        neighbors.append((i + n, "Bas "))
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
            # Construire la séquence des états du nœud initial jusqu'au nœud final
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


def print_solution(solution, moves):
    if solution:
        print("Solution found:")
        print("Mouvements : ", moves[len(moves)-1])
        for i, state in enumerate(solution):
            print("Etape ", i+1)
            print_state(state)
            print()
    else:
        print("Aucune solution trouvée.")


def print_state(state):
    n = int(len(state) ** 0.5)
    for i in range(0, len(state), n):
        print(" ".join(map(str, state[i:i+n])))


initial_state = [1, 2, 3, 4, 5, 6, 0, 7, 8]
board = [1, 2, 3, 4, 5, 0, 6, 7, 8]
# initial_state = [1, 2, 3, 0, 4, 6, 7, 5, 8]
# board = [8, 7, 6, 5, 4, 3, 2, 1, 0]

if __name__ == '__main__':
    solution, moves = solve_puzzle(initial_state)
    print_solution(solution, moves)
