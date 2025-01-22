"""""
Is a directed tree structure used in CTM to transmit STM content to all LTM processors.
It ensures that all processors receive the winning chunk at the same time,
playing a crucial role in forming "conscious awareness" and creating the "stream of consciousness" within the CTM.

Obs: As time progresses in clear steps (discrete), we consider that all processors receive the chunk in the same unit of time without needing real parallelism.
"""""

from UpTree import UpTree
from DiscreteClock import DiscreteClock

class DownTree:
    _instance = None

    def __new__(cls, *args, **kwargs):
        if cls._instance is None:
            cls._instance = super(DownTree, cls).__new__(cls)
            cls._instance._initialized = False
        return cls._instance

    def __init__(self):
        if not self._initialized:
            self.uptree = None 
            self.ltm = None  
            self._initialized = True
        
    def configure(self, uptree, ltm):
        self.uptree = uptree
        self.ltm = ltm

    def broadcast(self, chunk) -> None:
        DiscreteClock().increment_time()
        chunks_2_compete = self.ltm.process_stm(chunk)
        
        self.ut = UpTree()
        self.ut.compete(level=chunks_2_compete)
        self.block = True
