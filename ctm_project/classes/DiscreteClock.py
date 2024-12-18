from threading import Lock

class DiscreteClock:
    _instance = None 
    _lock = Lock()   

    def __new__(cls):
        with cls._lock: 
            if cls._instance is None:
                cls._instance = super(DiscreteClock, cls).__new__(cls)
                cls._instance._elapsed_time = 0
            return cls._instance

    def increment_time(self):
        self._elapsed_time += 1
