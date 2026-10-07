from models.Board import Board
from models.Human import Human
from models.Dwarf import Dwarf
from models.Wolve import Wolve
from models.Ork import Ork
from models.Dragonet import Dragonet

import random
      

board = Board()  
heroes = [
    Human("Lancelot"),
    Human("The black knight"),
    Dwarf("Gimly"),
    Dwarf("Tirion")
]
all_heroes = set(heroes)
monsters = [
    Wolve(),
    Dragonet(),
    Wolve(),
    Dragonet(),
    Ork(),
    Ork()
]

while len(monsters) > 0 and len(heroes) > 0:
    current_hero = heroes[0]
    current_monster = monsters[0]
    winner = board.fight(current_hero, current_monster)
    print(f"-----------\n{winner.name} won.")
    if winner == current_hero:
        loot = current_monster.loot()
        winner.gold += loot.get("gold")
        print(f"{winner.name}'s gold : {winner.gold}")
        winner.leather += loot.get("leather")
        print(f"{winner.name}'s leather : {winner.leather}")
        current_hero.health = current_hero.max_hp
        print(f"restored {winner.name}'s health to {current_hero.max_hp}")
        monsters.remove(current_monster)
    else:
        heroes.remove(current_hero) 
    print("==========")
        
        
        
if len(monsters) > 0:
    print("\033[31m------------------\033[0m")
    print("\033[31m- MONSTERS WON ! -\033[0m")
    print("\033[31m------------------\033[0m")
else:
    print("\033[32m----------------\033[0m")
    print("\033[32m- HEROES WON ! -\033[0m")
    print("\033[32m----------------\033[0m")
    heroes_gold = 0
    heroes_leather = 0
    for hero in all_heroes:
        heroes_gold += hero.gold
        heroes_leather += hero.leather
    print(f"Heroes total gold : {heroes_gold}")
    print(f"Heroes total leather : {heroes_leather}")
    print("\n\n\n\n")
    

    
# hero_01 = Hero("The black knight")
# monster_01 = Wolve()
# monster_01 = Ork()
# monster_01 = Dragonet()

# fight(hero_01,monster_01)


# print(hero_01.__str__())
# print(monster_01.__str__())