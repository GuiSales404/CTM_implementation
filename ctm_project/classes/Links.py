"""
Links are dynamic bidirectional connections between LTM processors that allow direct and efficient communication within the CTM.
They form and strengthen based on useful interaction between processors, facilitating internal processing and reducing the load on the STM.
Links play a crucial role in CTM efficiency and adaptability, allowing the machine to learn and adjust over time.
"""

import numpy as np

class Link:
    def __init__(self, len_of_processors):
        self.size = len_of_processors
        
    def _build_link_matrix(self):
        superior_diagonal = np.zeros((self.size, self.size))
        return superior_diagonal

    def strengthen(self):
        self.weight += 1

    def weaken(self):
        self.weight -= 1
        
    #nomear os processadores na matriz