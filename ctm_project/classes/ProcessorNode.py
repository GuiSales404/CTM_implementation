import random

from Processors import *
from Chunk import Chunk

class ProcessorNode():
    def __init__(self, name) -> None:
        self.name = name
        self.parent = None
        self.memory = []
        self.actual_chunk = None
        
        if len(self.name.split('_')) == 3:
            self.model_path = self.name.split('_')[-1]
            
        self.parent = None
        map_processor = {
            'sentiment': lambda: sentiment_analysis(),
            'ner': lambda: ner(),
            'summarization': lambda: summarization(),
            'qa': lambda: question_answering(),
            'llm': lambda: llm_processor(self.model_path),
            'llama': lambda: llama_processor(),
            'syntatic-stanza': lambda: syntatic_tree_stanza_processor(),
            'syntatic-spacy': lambda: syntatic_tree_spacy_processor(),
            'irony': lambda: irony_detection_processor(),
            'hate-speech': hate_speech_detection_processor(),
            'emotion': emotion_detection_processor()
            #llm para rag e llm para definir a instrução do llama
        }
        
        if self.name.split('_')[0] in map_processor:
            self.processor = map_processor[self.name.split('_')[0]]
        else:
            raise ValueError(f"Processor {self.name} not found")
        
    def receive_stm_chunk(self, chunk: Chunk) -> None:
        self.actual_chunk = chunk
        self.memory.append(chunk)
        
        
    def process_chunk(self) -> Chunk:
        chunk_process = self.processor.process(self.actual_chunk)
        result_chunk = self.generate_chunk(chunk_process)
        return result_chunk
        
    def generate_chunk(self, processor_content) -> Chunk:
        
        weight = random.uniform(-10, 10)
        intensity = abs(weight)
        mood = 'positive' if weight > 0 else 'negative' if weight < 0 else 'neutral'
        
        return Chunk(
            address=self.name,
            time=0,
            gist=processor_content,
            weight=weight,
            intensity=intensity,
            mood=mood
        )