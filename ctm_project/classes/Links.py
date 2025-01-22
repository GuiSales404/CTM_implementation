"""
Links are dynamic bidirectional connections between LTM processors that allow direct and efficient communication within the CTM.
They form and strengthen based on useful interaction between processors, facilitating internal processing and reducing the load on the STM.
Links play a crucial role in CTM efficiency and adaptability, allowing the machine to learn and adjust over time.
"""

import numpy as np

class Link:
    def __init__(self):
        self.size = None
        self.processors = None

    def configure(self, size, processors):
        self.size = size
        self.processors = processors
        self.links_matrix = self._build_link_matrix()
        self.name_reference = self._build_name_reference()
        
    def _build_link_matrix(self):
        links_matrix = np.full((self.size, self.size), np.inf)
        return links_matrix
    
    def _build_name_reference(self):
        name_reference = {}
        for i, processor in enumerate(self.processors):
            name_reference[processor.name] = i
        return name_reference

    def strengthen(self, processor1, processor2):
        print(f"Strengthening link between {processor1} and {processor2}")
        if processor1 == None or processor2 == None:
            return
        i = self.name_reference[processor1]
        j = self.name_reference[processor2]
        print(f"i: {i}, j: {j}")
        if i > j:
            i, j = j, i
        if self.links_matrix[i][j] == np.inf:
            self.links_matrix[i][j] = 1
        else:
            self.links_matrix[i][j] += 1

    def access_link(self, processor1, processor2):
        i = self.name_reference[processor1]
        j = self.name_reference[processor2]
        if i > j:
            i, j = j, i
        return self.links_matrix[i][j]
    
    def print_upper_diagonal(self):
        print()
        print("Diagonal Superior da Matriz de Links:")
        print("-" * 40)
        for i in range(self.size):
            for j in range(self.size):
                if i <= j:
                    value = self.links_matrix[i][j]
                    formatted_value = "INF" if value == np.inf else f"{value:.2f}"
                    print(f"[{i}, {j}] = {formatted_value}", end="\t")
            print()
        print("-" * 40)