"""""
Is an upward-directed binary tree structure used in CTM to organize and perform competition between chunks generated by LTM processors.
Through this competition, a single chunk is selected to be transmitted to the STM, where it becomes part of the CTM's conscious content.
The Up-Tree is essential for the model to function, as it ensures that only the most relevant or important information becomes conscious.

Weight and Intensity: Weight and intensity indicate its importance and urgency.Chunks with higher values are more likely to win the Up-Tree competition.
Temporal Context: More recent chunks or those responding to current stimuli may have an advantage.
Relevance: A chunk closely related to the CTM's current task or decision has a higher chance of winning.

LTM and InputMap chunks compete here in the Up-Tree
"""""

import random

from TreeNode import TreeNode
from Chunk import Chunk


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
        
    def coin_flip_neuron(self, a, b):
        elements = [a, b]
        if a == 0 and b == 0:
            probabilities = [0.5, 0.5]
        else:
            prob_a = a/(a+b)
            prob_b = 1 - prob_a
            probabilities = [prob_a, prob_b]
        return random.choices(elements, weights=probabilities, k=1)[0]

    def compete(self, chunks):
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
        if left_value == self.coin_flip_neuron(left_value, right_value):
            selected_chunk = left_chunk
        else:
            selected_chunk = right_chunk
        return selected_chunk

    def get_winner(self):
        return self.root.data