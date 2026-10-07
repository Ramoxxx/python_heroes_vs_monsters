from models.Board import Board
from models.Character import Character

board = Board()
kinght = Character(board)
print(kinght.__dict__)

# knight = Character()
# print(knight.__dict__)
# monster = Character()
# print(monster.__dict__)


# knight.strike(monster)