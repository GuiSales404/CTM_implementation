from ctm_project.classes.TreeNode import TreeNode

"""""
Is a directed tree structure used in CTM to transmit STM content to all LTM processors.
It ensures that all processors receive the winning chunk at the same time,
playing a crucial role in forming "conscious awareness" and creating the "stream of consciousness" within the CTM.

Obs: As time progresses in clear steps (discrete), we consider that all processors receive the chunk in the same unit of time without needing real parallelism.
"""""
class DownTree:
    def __init__(self, num_processors):
        self.root = TreeNode()
        self.leaves = [TreeNode() for _ in range(num_processors)]
        for leaf in self.leaves:
            self.root.add_child(leaf)

    def broadcast(self, chunk):
        self.root.broadcast(chunk)  