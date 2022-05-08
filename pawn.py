from constants import *
class Pawn:
    def __init__(self, color):
        self.color = color
        self.turns = 0
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
        moves = []
        if(self.color == BLACK):
            newRow1 = row + 1
            newRow2 = row + 2
        else:
            newRow1 = row - 1
            newRow2 = row - 2

        if(self.turns == 0):
            moves.append([newRow2, column])
        if(newRow1 >= 0 and newRow1 <= 7):
            moves.append([newRow1, column])
        
        return moves