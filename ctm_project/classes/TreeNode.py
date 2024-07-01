class TreeNode:
    def __init__(self):
        self.children = []
        self.data = None

    def add_child(self, node):
        self.children.append(node)