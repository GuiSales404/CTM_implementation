import random
import string

from TreeNode import TreeNode
from ProcessorNode import ProcessorNode
from LTM import LTM
from STM import STM

class UpTree:
    def __init__(self, stm: STM, ltm: LTM) -> None:
        self._build_tree()
        self.root = None
        self.leaves = None
        self.height = 0
        self._build_tree()
        self._print_tree(self.root)
        self.stm = stm
        self.ltm = ltm

    def _build_tree(self):
        if len(self.processors) <= 0:
            return None
        
        self.leaves = self.ltm.get_processors()

        current_level = self.leaves
        
        count = 0
        
        while len(current_level) > 1:
            count += 1
            next_level = []
            
            for i in range(0, len(current_level), 2):
                parent = TreeNode(f'{i}_{random.choice(string.ascii_lowercase)}')
                parent.add_l(current_level[i])
                current_level[i].parent = parent
                if i + 1 < len(current_level):
                    parent.add_r(current_level[i+1])
                    current_level[i+1].parent = parent
                next_level.append(parent)
            current_level = next_level
            
        self.root = current_level[0]
        self.stm.set_chunk(current_level[0])
        self.height = count
        
    def _print_tree(self, node, level=0, side='root'):
        if node:
            if isinstance(node, ProcessorNode):
                print(" " * (level * 4) + f"{side}: Processor {node.name}")
            else:
                print(" " * (level * 4) + f"{side}: {node.name}")
                self._print_tree(node.child_left, level + 1, "left")
                self._print_tree(node.child_right, level + 1, "right")

    def coin_flip_neuron(self, a, b):
        elements = [a, b]
        if a == 0 and b == 0:
            probabilities = [0.5, 0.5]
        else:
            prob_a = a/(a+b)
            prob_b = 1 - prob_a
            probabilities = [prob_a, prob_b]
        return random.choices(elements, weights=probabilities, k=1)[0]
    
    def compete(self, level=None, run=1, new_root_name=None):
        if level != None and len(level) == 1:
            self.root.name = new_root_name
            return
        
        if not level:
            level = self.leaves
            
        competitors = []
        winners = []
        for node in level:
            if isinstance(node, ProcessorNode):
                competitors.append(node)
            else:
                competitors.append(node)
                
            if len(competitors) == 2:
                gist_a = competitors[0]
                gist_b = competitors[1]
                winner_gist = self._competition_function(gist_a, gist_b)
                winners.append(winner_gist)
                print(f'\nrun {run}')
                print('\tcompetitors:', [comp.name for comp in competitors])
                print('\twinners:', [win.name for win in winners])
                competitor = competitors[0]
                competitors = []
        competitor.parent.name = winners[-1].name
        self.compete(winners, 1+run, winners[-1].name)

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