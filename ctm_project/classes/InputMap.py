class InputMap:
    def __init__(self):
        self.inputs = []

    def add_input(self, input_data):
        self.inputs.append(input_data)

    def get_input(self, time):
        return self.inputs[time] if time < len(self.inputs) else None
