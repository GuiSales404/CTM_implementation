from ctm_project.classes.STM import STM
from ctm_project.classes.LTM import LTM
from ctm_project.classes.DownTree import DownTree
from ctm_project.classes.UpTree import UpTree
from ctm_project.classes.InputMap import InputMap
from ctm_project.classes.OutputMap import OutputMap

class CTM:
    def __init__(self, num_processors):
        self.stm = STM()
        self.ltm = LTM(num_processors)
        self.down_tree = DownTree(num_processors)
        self.up_tree = UpTree(num_processors)
        self.input_map = InputMap()
        self.output_map = OutputMap()
        self.time = 0

    def run(self, total_time):
        for t in range(total_time):
            self.time = t
            input_chunk = self.input_map.get_input(t)
            if input_chunk:
                self.ltm.process(input_chunk)
            chunks = self.ltm.produce_chunks(t)
            self.up_tree.compete(chunks)
            winner_chunk = self.up_tree.get_winner()
            self.stm.set_chunk(winner_chunk)
            self.down_tree.broadcast(winner_chunk)
            self.ltm.process(winner_chunk)
            feedback = self.stm.get_chunk()
            for processor in self.ltm.processors:
                processor.adjust_weights(feedback)
            self.output_map.add_output(winner_chunk)

    def add_input(self, input_data):
        self.input_map.add_input(input_data)

    def get_output(self, time):
        return self.output_map.get_output(time)
