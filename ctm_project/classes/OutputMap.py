class OutputMap:
    def __init__(self):
        self.outputs = []

    def add_output(self, output_data):
        self.outputs.append(output_data)

    def get_output(self, time):
        return self.outputs[time] if time < len(self.outputs) else None