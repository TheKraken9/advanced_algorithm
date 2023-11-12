def remove(self, value):
    if self is None:
        return self
    if value < self.getValue():
        self.left = self.left.remove(value)
    elif value > self.getValue():
        self.right = self.right.remove(value)
    else:
        if self.left is None and self.right is None:
            return None
        elif self.left is None:
            return self.right
        elif self.right is None:
            return self.left
        else:
            successor = self.right
            while successor.left is not None:
                successor = successor.left
            self.setValue(successor.getValue())
            self.right = self.right.remove(successor.getValue())

    return self
