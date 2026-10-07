from models.Character import Character
class Hero(Character):
    def __init__(self,name = None):
        super().__init__()
        if not name is None:
            self.name = name
        