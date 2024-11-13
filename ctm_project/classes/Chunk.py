class Chunk:
    def __init__(self, address, time, gist, weight, intensity, mood):
        self.address = address
        self.time = time
        self.gist = gist
        self.weight = weight
        self.intensity = intensity
        self.mood = mood

    def __repr__(self):
        return f"Chunk(addr={self.address}, time={self.time}, gist={self.gist}, weight={self.weight}, intensity={self.intensity}, mood={self.mood})"


# Se for para QA o peso deve ser 1 para processadores LLM e 0.5 para outros
# Se for para leitura de história o peso deve ser o valor do sentiment_analysis
