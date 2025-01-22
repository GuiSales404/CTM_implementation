class Chunk:
    def __init__(self, address, time, gist, weight, intensity, mood):
        self.address = address
        self.time = time
        self.gist = gist
        self.weight = weight
        self.intensity = intensity
        self.mood = mood

    def __repr__(self):
        return (f"Chunk(address={self.address}, time={self.time}, "
                f"gist={self.gist}, weight={self.weight}, "
                f"intensity={self.intensity}, mood={self.mood})")