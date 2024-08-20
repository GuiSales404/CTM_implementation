class TreeNode:
    def __init__(self):
        self.data = None
        self.children = []

    def add_child(self, child_node):
        self.children.append(child_node)

    def broadcast(self, chunk):
        self.data = chunk
        for child in self.children:
            child.broadcast(chunk)  