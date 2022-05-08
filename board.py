import sys
from pawn import *
from PySide6.QtWidgets import QApplication, QWidget, QPushButton, QGridLayout
from PySide6.QtGui import QIcon
from PySide6.QtCore import QSize, Slot
from functools import partial

class Board:
    app = QApplication(sys.argv)
    win = QWidget()
    grid = QGridLayout()

    position = [[False, False, False, False, False, False, False, False, False],
            [Pawn(BLACK), Pawn(BLACK), Pawn(BLACK), Pawn(BLACK), Pawn(BLACK), Pawn(BLACK), Pawn(BLACK), Pawn(BLACK)],
            [False, False, False, False, False, False, False, False, False],
            [False, False, False, False, False, False, False, False, False],
            [False, False, False, False, False, False, False, False, False],
            [False, False, False, False, False, False, False, False, False],
            [Pawn(WHITE), Pawn(WHITE), Pawn(WHITE), Pawn(WHITE), Pawn(WHITE), Pawn(WHITE), Pawn(WHITE), Pawn(WHITE)],
            [False, False, False, False, False, False, False, False, False]
            ]

    def __init__(self):
        for i in range(8):
            for j in range(8):
                button = QPushButton()
                button.setFixedSize(100,100)
                button.setIconSize(QSize(50,50))
                first = "white"
                second = "grey"
                if(i%2 == 1):
                    first = "grey"
                    second = "white"
                if(j % 2 == 0):
                    button.setStyleSheet("background-color: "+first)
                else:
                    button.setStyleSheet("background-color: "+second)
                if(self.position[i][j]):
                    button.setIcon(QIcon(self.position[i][j].image))
                button.clicked.connect(partial(self.selectPiece, i, j))
                self.grid.addWidget(button, i, j)

    def resetTiles(self):
        for i in range(8):
            for j in range(8):
                button = QPushButton()
                button.setFixedSize(100,100)
                button.setIconSize(QSize(50,50))
                first = "white"
                second = "grey"
                if(i%2 == 1):
                    first = "grey"
                    second = "white"
                if(j % 2 == 0):
                    button.setStyleSheet("background-color: "+first)
                else:
                    button.setStyleSheet("background-color: "+second)
                if(self.position[i][j]):
                    button.setIcon(QIcon(self.position[i][j].image))
                button.clicked.connect(partial(self.selectPiece, i, j))
                self.grid.removeWidget(self.grid.itemAtPosition(i, j).widget())
                self.grid.addWidget(button, i, j)
                
    def showPossibleMoves(self, piece, moves, attacks):
        for i in range(8):
            for j in range(8):
                button = QPushButton()
                button.setFixedSize(100,100)
                button.setIconSize(QSize(50,50))
                first = "white"
                second = "grey"
                if(i%2 == 1):
                    first = "grey"
                    second = "white"
                if(j % 2 == 0):
                    button.setStyleSheet("background-color: "+first)
                else:
                    button.setStyleSheet("background-color: "+second)
                if(self.position[i][j]):
                    button.setIcon(QIcon(self.position[i][j].image))
                button.clicked.connect(partial(self.selectPiece, i, j))
                for move in moves:
                    if(move[0] == i and move[1] == j):
                        button.setStyleSheet("background-color: green")
                        button.clicked.connect(partial(self.move, piece[0], piece[1], move[0], move[1]))
                        break
                for attack in attacks:
                    if(attack[0] == i and attack[1] == j and self.position[attack[0]][attack[1]]):
                        button.setStyleSheet("background-color: red")
                        button.clicked.connect(partial(self.move, piece[0], piece[1], attack[0], attack[1]))
                        break
                self.grid.removeWidget(self.grid.itemAtPosition(i, j).widget())
                self.grid.addWidget(button, i, j)

    def display(self):
        self.win.setLayout(self.grid)
        self.win.setWindowTitle("Chess")
        self.win.setGeometry(50,50,800,800)
        self.win.show()
        sys.exit(self.app.exec())

    def selectPiece(self, i, j):
        self.resetTiles()
        if(self.position[i][j]):
            print("You chose ", i, j)
            attacks = self.position[i][j].attack(i,j)
            moves = self.position[i][j].move(i,j)
            self.showPossibleMoves([i,j], moves, attacks)
            # for move in moves:
            #     self.grid.itemAtPosition(move[0], move[1]).widget().setStyleSheet("background-color: green")

    
    def move(self, currRow, currCol, nextRow, nextCol):
        print(currRow, currCol)
        print(nextRow, nextCol)
        self.position[nextRow][nextCol] = self.position[currRow][currCol]
        self.position[currRow][currCol] = False
        self.resetTiles()
        print("Moving piece")
