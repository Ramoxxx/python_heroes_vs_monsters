from models.Character import Character
from models.Board import Board
class Wolve(Character):
    
    instances_cpt = 0
    
    def __init__(self):
        super().__init__()
        Wolve.instances_cpt += 1
        self.name = f"{self.__class__.__name__} {Wolve.instances_cpt}"
        self.leather = Board.instance.dice_04.throw()