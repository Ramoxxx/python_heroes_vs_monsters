from models.Dice import Dice
from models.Board import Board
class Character:
    
    instances_cpt = 0
    
    def __init__(self,board:Board):
        Character.instances_cpt += 1
        self._board = board
        self._name = f"{self.__class__.__name__} {self.instances_cpt}"
        self._endurance = Character.get_init_value()
        self._force = Character.get_init_value()
        self.health = self.endurance + self.get_modifier(self.endurance)
      
    @property
    def name(self)->str:
        return self._name   
    @property
    def endurance(self)->int:
        return self._endurance
    @property
    def force(self)->int:
        return self._force
    @property
    def health(self)->int:
        return self._health
    @health.setter
    def health(self,new_health:int):
        self._health = new_health
        
    def strike(self,other:Character):
        strike_strength = self.get_strike_strength()
        print(f"{self.name} strikes {other.name} with a strength of {strike_strength}")
     
    @staticmethod
    def get_init_value()->int:
        dice = Dice()
        throws = list()
        while len(throws) < 4:
            throws.append(dice.throw())     
        throws.sort()
        return sum(throws[1:])    
    
    def get_strike_strength(self)->int:
        return 0
    
    @staticmethod
    def get_modifier(attribute_value:int)->int:
        if attribute_value < 5:
            return -1
        elif attribute_value < 10:
            return 0
        elif attribute_value < 15:
            return 1
        else:
            return 2
