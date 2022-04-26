class Node:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None

    def insert(self, data):
        if self.key:
            if data < self.key:
                if self.left is None:
                    self.left = Node(data)
                else:
                    self.left.insert(data)
            elif data > self.key:
                if self.right is None:
                    self.right = Node(data)
                else:
                    self.right.insert(data)

    def find(self, data):
        if self.key == data:
            return True
        elif data < self.key and self.left is not None:
            return self.left.find(data)
        elif data > self.key and self.right is not None:
            return self.right.find(data)
        return False

    def prettyPrint(self, space):
        if self.right is not None:
            self.right.prettyPrint(space + 4)
        print(' ' * space + str(self.key))
        if self.left is not None:
            self.left.prettyPrint(space + 4)

    def getHeight(self):
        if self.left is None and self.right is None:
            return 1
        elif self.left is None:
            return self.right.getHeight() + 1
        elif self.right is None:
            return self.left.getHeight() + 1
        else:
            return max(self.left.getHeight(), self.right.getHeight()) + 1

    def getSize(self):

        if self.left is None and self.right is None:
            return 1
        elif self.left is None:
            return self.right.getSize() + 1
        elif self.right is None:
            return self.left.getSize() + 1
        else:
            return self.left.getSize() + self.right.getSize() + 1

    def getMin(self):
        if self.left is None:
            return self.key
        else:
            return self.left.getMin()

    def getMax(self):
        if self.right is None:
            return self.key
        else:
            return self.right.getMax()

    def inorder(self):
        if self.left:
            self.left.inorder()
        print(self.key),
        if self.right:
            self.right.inorder()
