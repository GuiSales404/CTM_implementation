"""""
LTM is a collection of processors that work in parallel.
Each processor in LTM has its own memory and can be viewed as a programmable and modifiable random access machine.

Is a set of processors that perform unconscious processing and compete to make their chunks part of the conscious content of the CTM.
They are responsible for much of the dynamics and functionality of the model,
acting as the source of ideas, responses, and information processing that can eventually become conscious.
"""""

from ProcessorNode import ProcessorNode

class LTM:
    def __init__(self, processors: int) -> None:
        
        if processors > 0 and (processors & processors - 1) != 0:
            raise ValueError("Number of processors must be a power of 2")
        
        self.processors = [ProcessorNode() for x in range(processors)]

    def get_processors(self) -> list:
        return self.processors

    def process(self, chunk, subject) -> None:
        result = []
        for processor in self.processors:
            result.append(processor.process_chunk_LTM(chunk, subject))
        
        return result
        # for x, y in result:
        #     print(x, ':', y)
        #     print()