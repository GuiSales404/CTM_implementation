from ctm_project.classes.TreeNode import TreeNode

class DownTree:
    def __init__(self, num_processors):
        self.root = TreeNode()
        self.leaves = [TreeNode() for _ in range(num_processors)]
        for leaf in self.leaves:
            self.root.add_child(leaf)

    def broadcast(self, chunk):
        for leaf in self.leaves:
            leaf.data = chunk