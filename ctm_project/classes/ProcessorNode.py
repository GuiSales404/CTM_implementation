from Processors import sentiment_analysis, llm_processor
from Chunk import Chunk

class ProcessorNode():
    def __init__(self) -> None:
        self.processor = llm_processor()
        model_name, temperature = llm_processor().get_id()
        self.name = f'{model_name}_{temperature}'
        self.parent = None
        self.memory = []
        self.actual_stm_chunk = None
        self.actual_input_chunk = None
        self.parent = None

    def format_to_memory(self, subject, gist):
        return {
            'role': subject,
            'content': gist
            }  
        
    def receive_stm_chunk(self, chunk: Chunk) -> None:
        self.actual_stm_chunk = chunk
        self.memory.append(self.format_to_memory('system', chunk['gist']))
        
    def receive_input_chunk(self, chunk: Chunk) -> None:
        self.actual_input_chunk = chunk
        self.memory.append(self.format_to_memory('user', chunk['gist']))
        
    def process_chunk_LTM(self, chunk, subject) -> Chunk:
        self.memory.append(self.format_to_memory(subject, chunk))
        chunk_process = self.processor.process(chunk, subject)
        result_chunk = self.generate_chunk(chunk_process)
        return result_chunk
    
    def process_chunk_Input(self, chunk, subject) -> Chunk:
        return
        
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
        
    def show_memory(self):
        for x in self.memory:
            print(x)