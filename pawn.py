from constants import *
class Pawn:
    def __init__(self, color):
        self.state = ALIVE
        self.color = color
        if(color == BLACK):
            self.image = 'img/pawn_b.png'
        else:
            self.image = 'img/pawn_w.png'
    
    def attack(self, row, column):
        if(self.color == BLACK):
            return [[row + 1, column + 1], [row + 1, column - 1]]
        else:
            return [[row - 1, column + 1], [row - 1, column - 1]]
    
    def move(self, row, column):
        if(self.color == BLACK):
            if(turns == 0):
                return [[row + 1, column], [row + 2, column]]
            else:
                return[[row + 1, column]]
        else:
            if(turns == 0):
                return [[row - 1, column], [row - 2, column]]
            else:
                return[[row - 1, column]]