import random
from ctm_project.classes.Processors import *

class ProcessorNode():
    def __init__(self, name, model_path) -> None:
        self.name = name
        self.parent = None
        map_processor = {
            'sa': lambda _: sentiment_analysis(),
            'ner': lambda _: ner(),
            'sum': lambda _: summarization(),
            'qa': lambda _: question_answering(),
            'llm': lambda _: llm_processor(model_path),
            'llama': lambda _: llama_processor()
            
        }
        if self.name.split('_')[0] in map_processor:
            self.processor = map_processor[self.name.split('_')[0]](self.name)
        else:
            raise ValueError(f"Processor {self.name} not found")
        
        
    def generate_gist():
        return random.randint(1, 100)