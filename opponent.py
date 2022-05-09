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

class Node:
    children = []
    board = []
    score = 0

class MinimaxOpponent(Opponent):
    def pickMove(self, board):
        curr = Node()
        curr.board = board
        self.buildTree(curr, BLACK)
        return min(curr.children, key = lambda x:x.score)
        # scores = []
        # for child in curr.children:
        #     child.buildTree(WHITE,curr.board)
        #     for node in child.children:
        #         scores.append(node.score)
        # return max(scores)


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
                [False, False, False, False, False, False, False, False],
                [False, False, False, False, False, False, False, False],
                [False, False, False, False, False, False, False, False],
                [False, False, False, False, False, False, False, False],
                [Pawn(WHITE), Pawn(WHITE), Pawn(WHITE), Pawn(WHITE), Pawn(WHITE), Pawn(WHITE), Pawn(WHITE), Pawn(WHITE)],
                [Rook(WHITE), Knight(WHITE), Bishop(WHITE), Queen(WHITE), King(WHITE), Bishop(WHITE), Knight(WHITE), Rook(WHITE)]]
opponent = MinimaxOpponent()
opponent.pickMove(position)