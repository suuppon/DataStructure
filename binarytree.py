class Node:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        
        self.parent = None
        self.left = None
        self.right = None


class BinaryTree:
    def __init__(self):
        self.root = None