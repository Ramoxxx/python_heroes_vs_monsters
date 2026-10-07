from models.Dice import Dice
from models.Board import Board
class Character:
    
    instances_cpt = 0
    
    def __init__(self,):
        Character.instances_cpt += 1
        self.is_alive = True
        self.name = f"{self.__class__.__name__} {self.instances_cpt}"
        self.endurance = self.get_init_value()
        self.strength = self.get_init_value()
        self.health = self.endurance + Board.get_modifier(self.endurance)
        self.gold = 0
        self.leather = 0
        
    @property
    def is_alive(self)->bool:
        return self._is_alive
    @is_alive.setter
    def is_alive(self,is_alive):
        self._is_alive = is_alive
    @property
    def name(self)->str:
        return self._name
    @name.setter
    def name(self,name:str):
        self._name = name
    @property
    def endurance(self)->int:
        return self._endurance
    @endurance.setter
    def endurance(self,endurance):
        self._endurance = endurance
    @property
    def strength(self)->int:
        return self._strength
    @strength.setter
    def strength(self,strength):
        self._strength = strength
    @property
    def health(self)->int:
        return self._health
    @health.setter
    def health(self,new_health:int):
        self._health = new_health  
    @property
    def gold(self)->int:
        return self._gold
    @gold.setter
    def gold(self,gold:int):
        self._gold = gold
    @property
    def leather(self)->int:
        return self._leather
    @leather.setter
    def leather(self,leather:int):
        self._leather = leather
        
        
        
              
    def strike(self,other:Character):
        strike_strength = self.get_strike_strength()
        other.health -= strike_strength
        print(f"{self.name} stroke {other.name} with a strength of {strike_strength}")
        
            
               

    def get_init_value(self)->int:        
        throws = list()
        while len(throws) < 4:
            throws.append(Board.instance.dice_06.throw())     
        throws.sort()
        return sum(throws[1:])    
    
    def get_strike_strength(self)->int:     
        return Board.instance.dice_04.throw() + Board.get_modifier(self.strength)
    
    def __str__(self):
        return f"-----\n{self.name} :\nHP : {self.health}\nGold : {self.gold}\nLeather : {self.leather}\n-----"
    
