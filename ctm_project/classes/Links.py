class Link:
    def __init__(self, processor1, processor2):
        self.processor1 = processor1
        self.processor2 = processor2
        self.weight = 0

    def strengthen(self):
        self.weight += 1

    def weaken(self):
        self.weight -= 1