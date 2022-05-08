from constants import *
class Rook:
    def __init__(self, color):
        self.color = color
        self.turns = 0
        if(color == BLACK):
            self.image = 'img/rook_b.png'
        else:
            self.image = 'img/rook_w.png'
    
    def attack(self, row, column, board):
        attacks = []
        nextRow = row + 1
        while(nextRow <= 7):
            if(board[nextRow][column]):
                if(board[nextRow][column].color != self.color):
                    attacks.append([nextRow, column])
                break
            nextRow += 1
        nextRow = row - 1
        while(nextRow >= 0):
            if(board[nextRow][column]):
                if(board[nextRow][column].color != self.color):
                    attacks.append([nextRow, column])
                break
            nextRow -= 1
        nextCol = column + 1
        while(nextCol <= 7):
            if(board[row][nextCol]):
                if(board[row][nextCol].color != self.color):
                    attacks.append([row, nextCol])
                break
            nextCol += 1
        nextCol = column - 1
        while(nextCol >= 0):
            if(board[row][nextCol]):
                if(board[row][nextCol].color != self.color):
                    attacks.append([row, nextCol])
                break
            nextCol -= 1
        
        return attacks
    
    def move(self, row, column, board):
        moves = []
        nextRow = row + 1
        while(nextRow <= 7):
            if(board[nextRow][column]):
                break
            moves.append([nextRow, column])
            nextRow += 1
        nextRow = row - 1
        while(nextRow >= 0):
            if(board[nextRow][column]):
                break
            moves.append([nextRow, column])
            nextRow -= 1
        nextCol = column + 1
        while(nextCol <= 7):
            if(board[row][nextCol]):
                break
            moves.append([row, nextCol])
            nextCol += 1
        nextCol = column - 1
        while(nextCol >= 0):
            if(board[row][nextCol]):
                break
            moves.append([row, nextCol])
            nextCol -= 1
        
        return moves