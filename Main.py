from models.Board import Board
from models.Character import Character
from models.Hero import Hero
from models.Wolve import Wolve
from models.Ork import Ork
from models.Dragonet import Dragonet


def fight(char_01:Character, char_02:Character):
    print(f"{char_01.name} starts fighting {char_02.name}")
    cpt = 0
    while char_01.health > 0 and char_02.health > 0:
        if cpt % 2 == 0:
            char_01.strike(char_02)
        else:
            char_02.strike(char_01)
        cpt += 1



board = Board()  

 
    
hero_01 = Hero("The black knight")
# monster_01 = Wolve()
# monster_01 = Ork()
monster_01 = Dragonet()

fight(hero_01,monster_01)

print(hero_01.__str__())
print(monster_01.__str__())