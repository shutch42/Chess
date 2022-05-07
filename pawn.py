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
        attacks = []

        if(self.color == BLACK):
            newRow = row + 1
        else:
            newRow = row - 1

        newCol1 = column + 1
        newCol2 = column - 1

        if(newRow <= 7 and newRow >= 0):
            if(newCol1 <= 7):
                attacks.append([newRow, newCol1])
            if(newCol2 >= 0):
                attacks.append([newRow, newCol2])

        return attacks
    
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