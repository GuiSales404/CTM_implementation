from STM import STM
from LTM import LTM
from DownTree import DownTree
from UpTree import UpTree
from InputMap import InputMap
from OutputMap import OutputMap
from DiscreteClock import DiscreteClock


class CTM:
    def __init__(self, num_processors, content):
        self.stm = STM()
        self.ltm = LTM(num_processors)
        self.up_tree = UpTree(self.stm, self.ltm)
        self.down_tree = DownTree(self.stm, self.ltm)
        self.input_map = InputMap(content)
        self.discrete_clock = DiscreteClock()
        self.output_map = OutputMap()

    def run(self):
        interactions = self.input_map.input_gist
        for interaction in interactions:
            self.discrete_clock.increment_time()
            processors_chunks = self.ltm.process(interaction, 'user')
            self.up_tree.compete(level=processors_chunks)