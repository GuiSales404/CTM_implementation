"""""
LTM is a collection of processors that work in parallel.
Each processor in LTM has its own memory and can be viewed as a programmable and modifiable random access machine.

Is a set of processors that perform unconscious processing and compete to make their chunks part of the conscious content of the CTM.
They are responsible for much of the dynamics and functionality of the model,
acting as the source of ideas, responses, and information processing that can eventually become conscious.
"""""

from ctm_project.classes.Processor import Processor

class LTM:
    def __init__(self, num_processors):
        self.processors = [Processor(i) for i in range(num_processors)]

    def process(self, chunk):
        for processor in self.processors:
            processor.process(chunk)

    def produce_chunks(self, time):
        return [processor.produce_chunk(time) for processor in self.processors]