from constants import *
class Bishop:
    def __init__(self, color):
        self.color = color
        self.turns = 0
        if(color == BLACK):
            self.image = 'img/bishop_b.png'
        else:
            self.image = 'img/bishop_w.png'
    
    def attack(self, row, column, board):
        attacks = []
        nextRow = row + 1
        nextCol = column + 1
        while(nextRow <= 7 and nextCol <= 7):
            if(board[nextRow][nextCol]):
                if(board[nextRow][nextCol].color != self.color):
                    attacks.append([nextRow, nextCol])
                break
            nextRow += 1
            nextCol += 1
        nextRow = row + 1
        nextCol = column - 1
        while(nextRow <= 7 and nextCol >= 0):
            if(board[nextRow][nextCol]):
                if(board[nextRow][nextCol].color != self.color):
                    attacks.append([nextRow, nextCol])
                break
            nextRow += 1
            nextCol -= 1
        nextRow = row - 1
        nextCol = column - 1
        while(nextRow >= 0 and nextCol >= 0):
            if(board[nextRow][nextCol]):
                if(board[nextRow][nextCol].color != self.color):
                    attacks.append([nextRow, nextCol])
                break
            nextRow -= 1
            nextCol -= 1
        nextRow = row - 1
        nextCol = column + 1
        while(nextRow >= 0 and nextCol <= 7):
            if(board[nextRow][nextCol]):
                if(board[nextRow][nextCol].color != self.color):
                    attacks.append([nextRow, nextCol])
                break
            nextRow -= 1
            nextCol += 1
    
        return attacks
    
    def move(self, row, column, board):
        moves = []
        nextRow = row + 1
        nextCol = column + 1
        while(nextRow <= 7 and nextCol <= 7):
            if(board[nextRow][nextCol]):
                break
            moves.append([nextRow, nextCol])
            nextRow += 1
            nextCol += 1
        nextRow = row + 1
        nextCol = column - 1
        while(nextRow <= 7 and nextCol >= 0):
            if(board[nextRow][nextCol]):
                break
            moves.append([nextRow, nextCol])
            nextRow += 1
            nextCol -= 1
        nextRow = row - 1
        nextCol = column - 1
        while(nextRow >= 0 and nextCol >= 0):
            if(board[nextRow][nextCol]):
                break
            moves.append([nextRow, nextCol])
            nextRow -= 1
            nextCol -= 1
        nextRow = row - 1
        nextCol = column + 1
        while(nextRow >= 0 and nextCol <= 7):
            if(board[nextRow][nextCol]):
                break
            moves.append([nextRow, nextCol])
            nextRow -= 1
            nextCol += 1
        
        return moves