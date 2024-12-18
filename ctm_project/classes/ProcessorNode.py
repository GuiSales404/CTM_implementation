from Processors import sentiment_analysis, llm_processor, llama_processor
from Chunk import Chunk

class ProcessorNode():
    def __init__(self, name) -> None:
        self.name = name
        self.parent = None
        self.memory = []
        self.actual_stm_chunk = None
        self.actual_input_chunk = None
        
        if len(self.name.split('_')) == 3:
            self.model_path = self.name.split('_')[-1]
        if len(self.name.split('_')) == 1:
            self.model_path = None
            
        self.parent = None
        map_processor = {
            'llm': lambda: llm_processor(self.model_path),
            'llama': lambda: llama_processor(),
        }
        
        if self.name.split('_')[0] in map_processor:
            self.processor = map_processor[self.name.split('_')[0]]
        else:
            raise ValueError(f"Processor {self.name} not found")

    def format_to_memory(self, subject, gist):
        return {
            'subject': subject,
            'gist': gist
            }  
        
    def receive_stm_chunk(self, chunk: Chunk) -> None:
        self.actual_stm_chunk = chunk
        self.memory.append(self.format_to_memory('CTM', chunk['gist']))
        
    def receive_input_chunk(self, chunk: Chunk) -> None:
        self.actual_input_chunk = chunk
        self.memory.append(self.format_to_memory('Input', chunk['gist']))
        
    def process_chunk(self, chunk, subject) -> Chunk:
        self.memory.append(self.format_to_memory(subject, chunk))
        chunk_process = self.processor().process(self.memory)
        result_chunk = self.generate_chunk(chunk_process)
        print('Processor:', self.name, 'processed:', result_chunk)
        return result_chunk
        
    def generate_chunk(self, processor_content) -> Chunk:
        sa = sentiment_analysis()
        weight = sa.process(processor_content)[0]['score']
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