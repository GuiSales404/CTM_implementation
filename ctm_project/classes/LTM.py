"""""
LTM is a collection of processors that work in parallel.
Each processor in LTM has its own memory and can be viewed as a programmable and modifiable random access machine.

Is a set of processors that perform unconscious processing and compete to make their chunks part of the conscious content of the CTM.
They are responsible for much of the dynamics and functionality of the model,
acting as the source of ideas, responses, and information processing that can eventually become conscious.
"""""

from ProcessorNode import ProcessorNode

class LTM:
    _instance = None 

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(LTM, cls).__new__(cls)
            cls._instance._initialized = False 
        return cls._instance
    
    def __init__(self) -> None:
        self.processors = None
        self._initialized = True

    def get_processors(self) -> list:
        return self.processors

    def configure(self, processors) -> None:
        if processors > 0 and (processors & processors - 1) != 0:
            raise ValueError("Number of processors must be a power of 2")
        
        self.processors = [ProcessorNode() for x in range(processors)]

    def process_input(self, chunk) -> None:
        result = []
        for processor in self.processors:
            result.append(processor.process_chunk_input(chunk, 'user'))
        
        return result
    
    def process_stm(self, chunk) -> None:
        result = []
        for processor in self.processors:
            result.append(processor.process_chunk_LTM(chunk, 'system'))
        
        return result
