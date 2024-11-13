import random
from Processors import *
from Chunk import Chunk

class ProcessorNode():
    def __init__(self, name) -> None:
        self.name = name
        self.parent = None
        
        if len(self.name.split('_')) == 3:
            self.model_path = self.name.split('_')[-1]
            
        self.parent = None
        map_processor = {
            'sa': lambda: sentiment_analysis(),
            'ner': lambda: ner(),
            'sum': lambda: summarization(),
            'qa': lambda: question_answering(),
            'llm': lambda: llm_processor(self.model_path),
            'llama': lambda: llama_processor()
            #llm para rag e llm para definir a instrução do llama
        }
        
        if self.name.split('_')[0] in map_processor:
            self.processor = map_processor[self.name.split('_')[0]]
        else:
            raise ValueError(f"Processor {self.name} not found")
        
        
    def generate_gist():
        return random.randint(1, 100)