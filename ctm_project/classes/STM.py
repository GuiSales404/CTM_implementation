"""""
Each and every time tick t = 0, 1, 2, …, T holds exactly one chunk.
This single chunk becomes the entirety of CTMs

The "chunk" winner of the competition in the Up-Tree competition is transmitted to all Long Term Memory (LTM) processors.
"""""
from Chunk import Chunk
from groq import Groq
from DiscreteClock import DiscreteClock as clock
from OutputMap import OutputMap
import os
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
        self.im = None # InputMap
        self.dt = None # DownTree
        self._initialized = True
        self.limit_maladaptive_daydreaming = 0
        self.past_address = None
        self.past_answer = None
        self.lc = None # LinkCentral
        self.om = OutputMap()
        self.reference = None
        self.counter = 0
        
    def configure(self, down_tree, input_map, links):
        self.dt = down_tree
        self.im = input_map
        self.lc = links
        self.reference = self.im.partitioned

    def set_chunk(self, chunk, first=False):
        if first:
            self.actual_chunk = chunk
            self.history.append(chunk)
        else:
            self.om.print_question(self.reference[self.counter])
            self.lc.strengthen(self.past_address, chunk.address)
            self.past_address = chunk.address
            self.past_answer = chunk.gist
            self.om.conscious_content(Chunk=chunk)

            result = self.evaluate_interaction(chunk.gist)
            if result == "0" and self.limit_maladaptive_daydreaming < 1:
                self.limit_maladaptive_daydreaming += 1
                self.actual_chunk = chunk
                self.history.append(chunk) 
                self.dt.broadcast(chunk)
            elif result == "1" or self.limit_maladaptive_daydreaming == 1:
                self.limit_maladaptive_daydreaming = 0 
                
                if len(self.reference)-1 == self.counter:
                    self.om.qa(self.reference[self.counter], chunk.gist)
                    self.om.output(self.actual_chunk)
                    self.om.generate_report()
                    self.lc.print_upper_diagonal()
                    return
                
                
                # If the chunk is too long, summarize the history and add the new information. Only Apply for history compreehension.
                # if self.naive_tokenizer(chunk.gist) > 25:
                #     summarized_story = self.summarize_history()
                #     ambient_input = self.im.input_gist.pop(0)
                #     self.im.reference_input.pop(0)
                #     new_gist = f"Histórico:{summarized_story} \n Informação Atual:{ambient_input}"
                #     self.actual_chunk = Chunk(address='STM', time=f'{clock.get_actual_time}', gist=new_gist, weight=chunk.weight, intensity=chunk.intensity, mood=chunk.mood)
                #     self.dt.broadcast(self.actual_chunk)
                #     self.om.output(self.actual_chunk)
                
                else:
                    self.om.qa(self.reference[self.counter], chunk.gist)
                    ambient_input = self.im.input_gist.pop(0)
                    self.counter += 1
                    self.actual_chunk = Chunk(address='STM', time=f'{clock.get_actual_time}', gist=ambient_input, weight=chunk.weight, intensity=chunk.intensity, mood=chunk.mood)
                    self.history.append(self.actual_chunk)
                    self.dt.broadcast(self.actual_chunk)
                    self.om.output(self.actual_chunk)
                    

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

        if isinstance(interaction, str):
            messages = []
            messages.append(
                {
                    "role": "system",
                    "content": self.reference[self.counter]
                }
            )
            messages.append(
                {
                    "role": "system",
                    "content": interaction
                }
            )
            messages.append(
                {
                    "role": "user",
                    "content": f"is the answer correct? if not return 0; if it is correct return 1. Do not return any additional text." if self.past_answer is None else f"Knowing that your previous answer to this same question was {self.past_answer}, is the  current answer right? if is not right return 0; if it is already right, return 1. Do not return any additional text."
                }
            )
            
            # print('\nHistórico de Avaliação:')
            # for message in messages:
            #     print(f"\t{message}")
                
            response = self.client.chat.completions.create(
                                                            model='llama3-70b-8192',
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
                                                        model='llama3-70b-8192',
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