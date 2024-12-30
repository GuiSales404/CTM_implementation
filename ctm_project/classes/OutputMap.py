"""
Is responsible for converting the machine's internal representations into signals or commands that can be sent to actuators or external systems,
allowing the CTM to interact with the environment.
They translate CTM intentions, decisions, or responses into physical actions, verbal expressions, or other forms of output that impact the external world.
"""
from classes.Chunk import Chunk

class OutputMap:
    def __init__(self):
        self.outputs = []

    def add_output(self, output_data):
        self.outputs.append(output_data)

    def get_output(self, time):
        return self.outputs[time] if time < len(self.outputs) else None
    
    def output(self, Chunk):
        self.add_output(Chunk)
        print("\n\n OUTPUT: ", Chunk)