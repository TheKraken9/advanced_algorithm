def solve_taquin(board):
  """Solve the taquin puzzle.

  Args:
    board: The initial state of the puzzle.

  Returns:
    A list of moves that solve the puzzle.
  """

  # Create a search tree.
  root = Node(board)
  open_set = [root]
  closed_set = set()

  # While there are still nodes to explore:
  while open_set:
    # Pop the node with the lowest cost from the open set.
    node = min(open_set, key=lambda n: n.cost)
    open_set.remove(node)

    # If the node is the goal state, return the solution.
    if node.is_goal():
      return node.path

    # Add the node's children to the open set.
    for child in node.children():
      if child not in closed_set:
        open_set.append(child)
        closed_set.add(child)

  # No solution was found.
  return []


class Node:
  """A node in the search tree."""

  def __init__(self, board):
    self.board = board
    self.cost = 0
    self.children = []

  def is_goal(self):
    """Returns True if the node is the goal state."""

    for i in range(len(self.board)):
      if self.board[i] != i + 1:
        return False

    return True

  def generate_children(self):
    """Generates the children of the node."""

    # Find the blank space.
    blank_index = self.board.index(0)

    # Generate all possible moves.
    for direction in [(-1, 0), (0, 1), (1, 0), (0, -1)]:
      new_index = blank_index + direction
      if 0 <= new_index < len(self.board):
        new_board = self.board[:]
        new_board[blank_index], new_board[new_index] = new_board[new_index], new_board[blank_index]
        child = Node(new_board)
        child.cost = self.cost + 1
        self.children.append(child)


def main():
  # Create the initial state of the puzzle.
  board = [1, 2, 3, 4, 5, 0, 6, 7, 8]

  # Solve the puzzle.
  solution = solve_taquin(board)

  # Print the solution.
  if solution:
    print("The solution is:")
    for move in solution:
      print(move)
  else:
    print("No solution was found.")


if __name__ == "__main__":
  main()
