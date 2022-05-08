from constants import *
class King:
    def __init__(self, color):
        self.color = color
        self.turns = 0
        if(color == BLACK):
            self.image = 'img/king_b.png'
        else:
            self.image = 'img/king_w.png'
    
    def attack(self, row, column, board):
        attacks = []
        possibleAttacks = [ [row + 1, column - 1],
                            [row + 1, column],
                            [row + 1, column + 1],
                            [row, column - 1],
                            [row, column + 1],
                            [row - 1, column - 1],
                            [row - 1, column],
                            [row - 1, column + 1] ]
        
        for attack in possibleAttacks:
            if(attack[0] >= 0 and attack[0] <= 7 and attack[1] >= 0 and attack[1] <= 7):
                if(board[attack[0]][attack[1]]):
                    if(board[attack[0]][attack[1]].color != self.color):
                        attacks.append(attack)
        
        return attacks
    
    def move(self, row, column, board):
        moves = []
        possibleMoves = [ [row + 1, column - 1],
                            [row + 1, column],
                            [row + 1, column + 1],
                            [row, column - 1],
                            [row, column + 1],
                            [row - 1, column - 1],
                            [row - 1, column],
                            [row - 1, column + 1] ]
        
        for move in possibleMoves:
            if(move[0] >= 0 and move[0] <= 7 and move[1] >= 0 and move[1] <= 7):
                if(not board[move[0]][move[1]]):
                    moves.append(move)
        
        return moves