"""""
Each and every time tick t = 0, 1, 2, …, T holds exactly one chunk.
This single chunk becomes the entirety of CTMs

The "chunk" winner of the competition in the Up-Tree competition is transmitted to all Long Term Memory (LTM) processors.
"""""
class STM:
    def __init__(self):
        self.chunk = None
        self.history = []
        
    def set_chunk(self, chunk):
        self.chunk = chunk
        self.history.append(chunk)  

    def get_chunk(self):
        return self.chunk