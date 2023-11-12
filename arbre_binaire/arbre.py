class Arbre:
    def __init__(self, node):
        self.racine = node

    def insert(self, number):
        self.racine.insert(number)

    def insertNode(self, node):
        self.racine.insertNode(node)

    def print(self):
        self.racine.print()

    def remove(self, value):
        self.racine = self.racine.remove(value)