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
