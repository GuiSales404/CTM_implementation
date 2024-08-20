"""""
The input maps in the CTM are responsible for transforming external sensory information into internal representations that the machine can process.
They convert the data captured by the sensors into an internal language called Brainish (which will not be used in this work),
encapsulate this information into chunks and send it to the LTM processors.
"""""

# Processar o Text com análise de sentimentos e tals

class InputMap:
    def __init__(self):
        self.inputs = []

    def add_input(self, input_data):
        self.inputs.append(input_data)

    def get_input(self, time):
        return self.inputs[time] if time < len(self.inputs) else None
