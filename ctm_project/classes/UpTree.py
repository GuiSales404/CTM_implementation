from ctm_project.classes.TreeNode import TreeNode
from ctm_project.classes.Chunk import Chunk

class UpTree:
    def __init__(self, num_processors):
        self.root = TreeNode()
        self.leaves = [TreeNode() for _ in range(num_processors)]
        self.nodes = [self.leaves]
        self._build_tree()

    def _build_tree(self):
        current_level = self.leaves
        while len(current_level) > 1:
            next_level = []
            for i in range(0, len(current_level), 2):
                parent = TreeNode()
                parent.add_child(current_level[i])
                if i + 1 < len(current_level):
                    parent.add_child(current_level[i + 1])
                next_level.append(parent)
            self.nodes.append(next_level)
            current_level = next_level
        self.root = current_level[0]

    def compete(self, chunks):
        # Garantindo que todos os chunks nas folhas são válidos
        for i, chunk in enumerate(chunks):
            if chunk is None:
                chunks[i] = Chunk(0, 0, {'r': 0, 'g': 0, 'b': 0})  # Inicializando com valores padrão
            self.leaves[i].data = chunks[i]

        for level in reversed(self.nodes):
            for node in level:
                if len(node.children) == 2:
                    left_chunk = node.children[0].data
                    right_chunk = node.children[1].data
                    print(f"left_chunk: {left_chunk}, right_chunk: {right_chunk}")
                    node.data = self._competition_function(left_chunk, right_chunk)
                else:
                    node.data = node.children[0].data

    def _competition_function(self, left_chunk, right_chunk):
        left_value = left_chunk.intensity + 0.5 * left_chunk.mood
        right_value = right_chunk.intensity + 0.5 * right_chunk.mood
        if left_value > right_value:
            return left_chunk
        elif right_value > left_value:
            return right_chunk
        else:
            return left_chunk if left_chunk.address < right_chunk.address else right_chunk

    def get_winner(self):
        return self.root.data
