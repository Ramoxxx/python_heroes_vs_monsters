from random import randint
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from models.Character import Character
from models.Dice import Dice

class Board:
    
    instance = None
    
    def __init__(self):
        self._dice_04 = Dice(1,4)
        self._dice_06 = Dice(1,6)
        Board.instance = self
        
    @property
    def dice_04(self)->Dice:
        return self._dice_04
    @property
    def dice_06(self)->Dice:
        return self._dice_06
    
    def fight(self, char_01:Character, char_02:Character)->Character:
        first = char_01 if randint(1,2)%2 == 0 else char_02
        second = char_02 if first == char_01 else char_01
        print("=============================================")
        print(f"{first.name} starts fighting {second.name}")
        print("---------------------------------------------")
        cpt = 0
        while first.health > 0 and second.health > 0:
            # print(f"{first.name} HP : {first.health}")
            # print(f"{second.name} HP : {second.health}")
            if cpt % 2 == 0:
                first.strike(second)
            else:
                second.strike(first)
            cpt += 1
        if first.health <= 0:
            return second
        else:
            return first
    
    
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