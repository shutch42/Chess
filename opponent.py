from csv import QUOTE_NONE
from constants import *
import random
import copy

class Opponent:
    def findMoveablePieces(self, color, board):
        pieces = []
        rowCounter = 0
        colCounter = 0
        for row in board:
            for piece in row:
                if(piece):
                    if(piece.color == color and (len(piece.move(rowCounter, colCounter, board)) > 0 or len(piece.attack(rowCounter, colCounter, board)) > 0)):
                        pieces.append([piece, rowCounter, colCounter])
                colCounter += 1
            rowCounter += 1
            colCounter = 0
        return pieces
class RandomOpponent(Opponent):
    def pickMove(self, board):
        pieces = self.findMoveablePieces(BLACK, board)
        pieceInfo = random.choice(pieces)
        piece = pieceInfo[0]
        row = pieceInfo[1]
        col = pieceInfo[2]
        moves = piece.move(row, col, board)
        attacks = piece.attack(row, col, board)
        choice = random.choice(moves + attacks)
        nextRow = choice[0]
        nextCol = choice[1]
        return row, col, nextRow, nextCol

class GreedyOpponent(Opponent):
    def pickMove(self, board):
        score = 0
        row = -1
        col = -1
        nextRow = -1
        nextCol = -1
        pieces = self.findMoveablePieces(BLACK, board)
        for piece in pieces:
            p = piece[0]
            t_row = piece[1]
            t_col = piece[2]
            attacks = p.attack(t_row, t_col, board)
            for attack in attacks:
                t_nextRow = attack[0]
                t_nextCol = attack[1]
                piece = type(board[t_nextRow][t_nextCol])
                if piece is Bishop:
                    turnScore = BISHOP
                if piece is King:
                    turnScore = KING
                if piece is Knight:
                    turnScore = KNIGHT
                if piece is Pawn:
                    turnScore = PAWN
                if piece is Queen:
                    turnScore = QUEEN
                if piece is Rook:
                    turnScore = ROOK
                if turnScore > score:
                    print("Found move")
                    print(turnScore)
                    score = turnScore
                    row = t_row
                    col = t_col
                    nextRow = t_nextRow
                    nextCol = t_nextCol
        if score == 0:
            random = RandomOpponent()
            return random.pickMove(board)
        else:
            return row, col, nextRow, nextCol

class Node:
    children = []
    board = []
    score = 0
    startRow = 0
    startCol = 0
    moveToRow = 0
    moveToCol = 0

class MinimaxOpponent(Opponent):
    def pickMove(self, board):
        curr = Node()
        curr.board = board
        self.buildTree(curr, BLACK)
        bestMove = min(curr.children, key = lambda x:x.score)
        return bestMove.startRow, bestMove.startCol, bestMove.moveToRow, bestMove.moveToCol


    def buildTree(self, head, color):
        pieces = self.findMoveablePieces(color, head.board)
        for piece in pieces:
            p = piece[0]
            row = piece[1]
            col = piece[2]
            moves = p.move(row, col, head.board)
            attacks = p.attack(row, col, head.board)
            for move in moves:
                nextRow = move[0]
                nextCol = move[1]
                head.children.append(self.childNode(row, col, nextRow, nextCol, color, head.board))
            for attack in attacks:
                nextRow = attack[0]
                nextCol = attack[1]
                head.children.append(self.childNode(row, col, nextRow, nextCol, color, head.board))
        return

            
    def childNode(self, currRow, currCol, nextRow, nextCol, color, board):
        child = Node()
        takePiece = board[nextRow][nextCol]
        score = 0
        if(takePiece):
            piece = type(takePiece)
            if(piece is Bishop):
                score += BISHOP
            if(piece is King):
                score += KING
            if(piece is Knight):
                score += KNIGHT
            if(piece is Pawn):
                score += PAWN
            if(piece is Queen):
                score += QUEEN
            if(piece is Rook):
                score += ROOK
        if(color == BLACK):
            child.score += score
        else:
            child.score -= score
        nextBoard = copy.deepcopy(board)
        nextBoard[nextRow][nextCol] = nextBoard[currRow][currCol]
        child.board = nextBoard
        child.startRow = currRow
        child.startCol = currCol
        child.moveToRow = nextRow
        child.moveToCol = nextCol
        return child

#test
from pawn import *
from rook import *
from knight import *
from bishop import *
from queen import *
from king import *
position = [[Rook(BLACK), Knight(BLACK), Bishop(BLACK), Queen(BLACK), King(BLACK), Bishop(BLACK), Knight(BLACK), Rook(BLACK)],
                [Pawn(BLACK), Pawn(BLACK), Pawn(BLACK), Pawn(BLACK), Pawn(BLACK), Pawn(BLACK), Pawn(BLACK), Pawn(BLACK)],
                [False, False, Pawn(WHITE), False, False, False, False, False],
                [False, False, False, False, False, False, False, False],
                [False, False, False, False, False, False, False, False],
                [False, False, False, False, False, False, False, False],
                [Pawn(WHITE), Pawn(WHITE), Pawn(WHITE), Pawn(WHITE), Pawn(WHITE), Pawn(WHITE), Pawn(WHITE), Pawn(WHITE)],
                [Rook(WHITE), Knight(WHITE), Bishop(WHITE), Queen(WHITE), King(WHITE), Bishop(WHITE), Knight(WHITE), Rook(WHITE)]]
opponent = GreedyOpponent()
print(opponent.pickMove(position))