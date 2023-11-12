COUNT = [10]


class Racine:
    def __init__(self, value, depth):
        self.setValue(value)
        self.putToRight(None)
        self.putToLeft(None)
        self.setDepth(depth)

    def setValue(self, value):
        self.value = value

    def getValue(self):
        return self.value

    def setDepth(self, depth):
        self.depth = depth

    def getDepth(self):
        return self.depth

    def getLeft(self):
        return self.left

    def getRight(self):
        return self.right

    def putToLeft(self, node):
        self.left = node

    def putToRight(self, node):
        self.right = node

    def insert(self, number):
        if number > self.getValue():
            self.InsertToRight(number)
        elif number < self.getValue():
            self.InsertToLeft(number)

    def insertNode(self, node):
        self.insert(node.getValue())

    def InsertToRight(self, number):
        if self.getRight() is not None:
            self.getRight().insert(number)
        else:
            leaf = Racine(number, self.getDepth() + 1)
            self.putToRight(leaf)

    def InsertToLeft(self, number):
        if self.getLeft() is not None:
            self.getLeft().insert(number)
        else:
            leaf = Racine(number, self.getDepth() + 1)
            self.putToLeft(leaf)

    def getMax(self):
        if self.getRight() is not None:
            return self.getRight().getMax()
        return self

    def getMin(self):
        if self.getLeft() is not None:
            return self.getLeft().getMin()
        return self

    def getMinIterative(self):
        current = self
        while current.getLeft() is not None:
            current = current.getLeft()
        return current

    def getMaxIterative(self):
        current = self
        while current.getRight() is not None:
            current = current.getRight()
        return current

    def delete(self, value):
        if self is None:
            return self

        # Find the node to delete
        parent = None
        current = self
        while current is not None and current.getValue() != value:
            parent = current
            if value < current.getValue():
                current = current.getLeft()
            else:
                current = current.getRight()

        if current is None:
            return self

        # delete the node
        if current.getLeft() is None:
            child = current.getRight()
        elif current.getRight() is None:
            child = current.getLeft()
        else:
            # eto toujours à gauche
            successor = current.getRight()
            while successor.getLeft() is not None:
                successor = successor.getLeft()
            successorValue = successor.getValue()
            self.delete(successorValue)
            current.setValue(successorValue)
            return self

        if parent is None:
            return child
        elif current == parent.getLeft():
            parent.putToLeft(child)
        else:
            parent.putToRight(child)

        return self

    def transform(self, space):
        if self is None:
            return
        space += COUNT[0]
        if self.getRight() is not None:
            self.getRight().transform(space)

        print()
        for i in range(COUNT[0], space):
            print(end=" ")
        print(self.value)
        if self.getLeft() is not None:
            self.getLeft().transform(space)

    def print(self):
        self.transform(0)
