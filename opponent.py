from constants import *
import random
class RandomOpponent:
    def pickMove(self, board):
        pieces = self.findMovablePieces(board)
        movePiece = random.choice(pieces)
        moves = movePiece[0].move(movePiece[1], movePiece[2], board)
        attacks = movePiece[0].attack(movePiece[1], movePiece[2], board)
        choice = random.choice(moves + attacks)
        return choice

    def findMoveablePieces(self, board):
        pieces = []
        rowCounter = 0
        colCounter = 0
        for row in board.positions:
            for piece in row:
                if(piece.color == BLACK and (len(piece.move) > 0 or len(piece.attack) > 0)):
                    pieces.append([piece, rowCounter, colCounter])
                colCounter += 1
            rowCounter += 1
            colCounter = 0
        return pieces