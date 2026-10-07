import random
class Dice:
    def __init__(self,min:int = 1, max:int = 6):
        self._min = min
        self._max = max
    
    @property
    def min(self):
        return self._min
    @min.setter
    def min(self,n_min):
        self._min = n_min
    
    @property
    def max(self):
        return self._max
    @max.setter
    def max(self,n_max):
        self._max = n_max
        
    def throw(self)->int:
        return random.randint(self.min, self.max) 