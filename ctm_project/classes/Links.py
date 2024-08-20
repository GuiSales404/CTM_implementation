"""
Links are dynamic bidirectional connections between LTM processors that allow direct and efficient communication within the CTM.
They form and strengthen based on useful interaction between processors, facilitating internal processing and reducing the load on the STM.
Links play a crucial role in CTM efficiency and adaptability, allowing the machine to learn and adjust over time.
"""

class Link:
    def __init__(self, processor1, processor2):
        self.processor1 = processor1
        self.processor2 = processor2
        self.weight = 0

    def strengthen(self):
        self.weight += 1

    def weaken(self):
        self.weight -= 1