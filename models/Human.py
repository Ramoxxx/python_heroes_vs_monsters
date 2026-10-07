from models.Character import Character
class Human(Character):
    def __init__(self,name = None):
        super().__init__()
        if not name is None:
            self.name = name
            self.max_hp = self.health
            self.strength += 1
            self.endurance += 1
        