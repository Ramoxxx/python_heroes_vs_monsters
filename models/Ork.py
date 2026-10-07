from models.Character import Character
from models.Board import Board
class Ork(Character):
    instances_cpt = 0
        
    def __init__(self):
        super().__init__()
        Ork.instances_cpt += 1
        self.name = f"{self.__class__.__name__} {Ork.instances_cpt}"
        self.strength += 1
        self.gold = Board.instance.dice_06.throw()