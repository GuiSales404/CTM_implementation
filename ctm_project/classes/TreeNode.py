class TreeNode:
    def __init__(self, data):
        self.name = data
        self.parent = None
        self.child_left = None
        self.child_right = None

    def add_l(self, child_left):
        self.child_left = child_left
        
    def add_r(self, child_right):
        self.child_right = child_right