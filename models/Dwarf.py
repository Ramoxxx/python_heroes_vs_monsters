from models.Character import Character
class Dwarf(Character):
    def __init__(self,name = None):
        super().__init__()
        if not name is None:
            self.name = name
            self.max_hp = self.health
            self.endurance += 2