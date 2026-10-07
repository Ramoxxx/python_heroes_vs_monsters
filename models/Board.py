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