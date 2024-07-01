from ctm_project.classes.Processor import Processor

class LTM:
    def __init__(self, num_processors):
        self.processors = [Processor(i) for i in range(num_processors)]

    def process(self, chunk):
        for processor in self.processors:
            processor.process(chunk)

    def produce_chunks(self, time):
        return [processor.produce_chunk(time) for processor in self.processors]