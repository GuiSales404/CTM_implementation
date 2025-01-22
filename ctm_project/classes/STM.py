"""""
Each and every time tick t = 0, 1, 2, …, T holds exactly one chunk.
This single chunk becomes the entirety of CTMs

The "chunk" winner of the competition in the Up-Tree competition is transmitted to all Long Term Memory (LTM) processors.
"""""
from Chunk import Chunk
from groq import Groq
from DiscreteClock import DiscreteClock as clock
import os

import emoji
class STM:
    _instance = None 

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(STM, cls).__new__(cls)
            cls._instance._initialized = False 
        return cls._instance
    
    def __init__(self) -> None:
        self.actual_chunk = None
        self.history = []
        self.client = Groq(api_key=os.getenv('GROQ_API_KEY'))
        self.im = None
        self.dt = None
        self._initialized = True
        self.limit_maladaptive_daydreaming = 0
    def configure(self, down_tree, input_map):
        self.dt = down_tree
        self.im = input_map
        
    def set_chunk(self, chunk, first=False):
        if first:
            self.actual_chunk = chunk
            self.history.append(chunk)
        else:
            print("\n💭Conteúdo Consciente:", chunk.gist)
            result = self.evaluate_interaction(chunk.gist)
            if result == "0" and self.limit_maladaptive_daydreaming < 3:
                self.limit_maladaptive_daydreaming += 1
                self.actual_chunk = chunk
                self.history.append(chunk) 
                self.dt.broadcast(chunk)
            elif result == "1":
                if len(self.im.input_gist) <= 0:
                    return
                
                if self.naive_tokenizer(chunk.gist) > 25:
                    summarized_story = self.summarize_history()
                    ambient_input = self.im.input_gist.pop(0)
                    print("Informação do Ambiente: ", ambient_input)
                    new_gist = f"Histórico:{summarized_story} \n Informação Atual:{ambient_input}"
                    self.actual_chunk = Chunk(address='STM', time=f'{clock.get_actual_time}', gist=new_gist, weight=chunk.weight, intensity=chunk.intensity, mood=chunk.mood)
                    print("\n💭Pensamento Gerado:", self.actual_chunk.gist)
                    self.dt.broadcast(self.actual_chunk)

    def get_chunk(self):
        return self.actual_chunk
    
    def evaluate_interaction(self, interaction):
        """
        Evaluates an interaction based on the history of previous interactions.
        Args:
            interaction (str): The new interaction to be evaluated.
        Returns:
            str: The response from the model indicating whether to develop the idea further (0) or add new information (1).
        """
        
        messages = []
        for element in self.history:
            if isinstance(element, Chunk):
                messages.append(
                    {
                        "role": "system",
                        "content": element.gist
                    }
                )
        messages.append(
            {
                "role": "user",
                "content": f"Baseado no que foi apresentado até agora, é necessário desenvolver mais essa ideia: {interaction} ou ela já traz consigo uma informação suficiente e é melhor adicionar mais informações novas no sistema ? Se for necessário desenvolver mais a ideia retorne 0, caso já esteja suficiente e vamos adicionar mais informações retorne 1. Não retorne nenhum texto adicional."
            }
        )
        
        response = self.client.chat.completions.create(
                                                        model='llama3-8b-8192',
                                                        messages=messages,
                                                        temperature=0.2
                                                    )
        return response.choices[0].message.content
    
    def summarize_history(self):
        """
        Summarizes the history of interactions.
        Returns:
            str: The summary of the history of interactions.
        """
        summary = ""
        for element in self.history:
            if isinstance(element, Chunk):
                summary += f"{element.gist}\n"
        message = [
            {
                "role": "system",
                "content": f"Faça um resumo dessas informações: {summary}. Não retorne nenhum texto adicional, apenas o resumo."
            }
        ]
        response = self.client.chat.completions.create(
                                                        model='llama3-8b-8192',
                                                        messages=message,
                                                        temperature=0.1
                                                    )
        return response.choices[0].message.content     
    
    def naive_tokenizer(self, text):
        """
        Tokenizes a text.
        Args:
            text (str): The text to be tokenized.
        Returns:
            list: The tokenized text.
        """
        return len(text.split())