import random
from ctm_project.classes.Chunk import Chunk

class Processor:
    def __init__(self, address):
        self.address = address
        self.memory = []
        self.weights = []

    def process(self, chunk):
        # Processamento específico de cada processador
        self.memory.append(chunk)
        self.adjust_weights(chunk)

    def adjust_weights(self, feedback):
        # Ajuste de pesos baseado no feedback
        pass

    def produce_chunk(self, time, weight=None, intensity=None, mood=None, gist=None):
        gist = f"Gist at time {time}"
        weight = random.uniform(-1, 1)
        intensity = abs(weight)
        mood = weight
        return Chunk(self.address, time, gist, weight, intensity, mood)