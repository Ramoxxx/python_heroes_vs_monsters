from models.Dice import Dice
class Board:
    def __init__(self):
        self._dice_06 = Dice(1,6)
    @property
    def dice_06(self)->Dice:
        return self._dice_06