def remove(self, value):
    if self is None:
        return self

    # Find the node to remove
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

    # Remove the node
    if current.getLeft() is None:
        child = current.getRight()
    elif current.getRight() is None:
        child = current.getLeft()
    else:
        successor = current.getRight()
        while successor.getLeft() is not None:
            successor = successor.getLeft()
        successorValue = successor.getValue()
        self.remove(successorValue)
        current.setValue(successorValue)
        return self

    if parent is None:
        return child
    elif current == parent.getLeft():
        parent.putToLeft(child)
    else:
        parent.putToRight(child)

    return self
