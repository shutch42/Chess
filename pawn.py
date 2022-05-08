from constants import *
class Pawn:
    def __init__(self, color):
        self.color = color
        self.turns = 0
        if(color == BLACK):
            self.image = 'img/pawn_b.png'
        else:
            self.image = 'img/pawn_w.png'
    
    def attack(self, row, column, board):
        attacks = []

        if(self.color == BLACK):
            newRow = row + 1
        else:
            newRow = row - 1

        newCol1 = column + 1
        newCol2 = column - 1

        if(newRow <= 7 and newRow >= 0):
            if(newCol1 <= 7 and board[newRow][newCol1]):
                if(board[newRow][newCol1].color != self.color):
                    attacks.append([newRow, newCol1])
            if(newCol2 >= 0 and board[newRow][newCol2]):
                if(board[newRow][newCol2].color != self.color):
                    attacks.append([newRow, newCol2])

        return attacks
    
    def move(self, row, column, board):
        moves = []
        if(self.color == BLACK):
            newRow1 = row + 1
            newRow2 = row + 2
        else:
            newRow1 = row - 1
            newRow2 = row - 2

        if(not board[newRow1][column] and newRow1 >= 0 and newRow1 <= 7):
            moves.append([newRow1, column])
            if(self.turns == 0 and not board[newRow2][column]):
                moves.append([newRow2, column])
        
        return moves