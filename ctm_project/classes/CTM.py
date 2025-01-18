from STM import STM
from LTM import LTM
from DownTree import DownTree
from UpTree import UpTree
from InputMap import InputMap
from OutputMap import OutputMap
from DiscreteClock import DiscreteClock


class CTM:
    
    def initialize_system(num_processors, im):
        stm = STM()
        ltm = LTM()
        uptree = UpTree()
        downtree = DownTree()
        
        ltm.configure(num_processors)
        stm.configure(downtree, input_map=im)  
        downtree.configure(uptree, ltm)
        uptree.configure(stm, ltm)
        
        return stm, ltm, uptree, downtree
    
    def __init__(self, num_processors, content):
        self.input_map = InputMap(content)
        self.stm, self.ltm, self.up_tree, self.down_tree = CTM.initialize_system(num_processors, self.input_map)
        
        self.discrete_clock = DiscreteClock()
        self.output_map = OutputMap()
        

    def run(self):
        self.discrete_clock.increment_time()
        interactions = self.input_map.input_gist
        processors_chunks = self.ltm.process_input(interactions.pop(0))
        self.up_tree.compete(level=processors_chunks)