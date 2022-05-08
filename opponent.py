from constants import *
import random
class RandomOpponent:
    def pickMove(self, board):
        #FIXME: Make this more readable
        pieces = self.findMoveablePieces(board)
        movePiece = random.choice(pieces)
        moves = movePiece[0].move(movePiece[1], movePiece[2], board)
        attacks = movePiece[0].attack(movePiece[1], movePiece[2], board)
        choice = random.choice(moves + attacks)
        return movePiece[1], movePiece[2], choice[0], choice[1]

    def findMoveablePieces(self, board):
        pieces = []
        rowCounter = 0
        colCounter = 0
        for row in board:
            for piece in row:
                if(piece):
                    if(piece.color == BLACK and (len(piece.move(rowCounter, colCounter, board)) > 0 or len(piece.attack(rowCounter, colCounter, board)) > 0)):
                        pieces.append([piece, rowCounter, colCounter])
                colCounter += 1
            rowCounter += 1
            colCounter = 0
        return pieces