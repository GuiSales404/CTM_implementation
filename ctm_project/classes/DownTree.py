"""""
Is a directed tree structure used in CTM to transmit STM content to all LTM processors.
It ensures that all processors receive the winning chunk at the same time,
playing a crucial role in forming "conscious awareness" and creating the "stream of consciousness" within the CTM.

Obs: As time progresses in clear steps (discrete), we consider that all processors receive the chunk in the same unit of time without needing real parallelism.
"""""

from LTM import LTM
from STM import STM

class DownTree:
    def __init__(self, stm: STM, ltm: LTM) -> None:
        self.stm = stm
        self.ltm = ltm
        
    def broadcast(self) -> None:
        self.ltm.process(self.stm.get_chunk())
