import sys
from pawn import *
from PySide6.QtWidgets import QApplication, QWidget, QPushButton, QGridLayout
from PySide6.QtGui import QIcon
from PySide6.QtCore import QSize, Slot
from functools import partial

class Board:
    p1_black = Pawn(BLACK)
    p2_black = Pawn(BLACK)
    p3_black = Pawn(BLACK)
    p4_black = Pawn(BLACK)
    p5_black = Pawn(BLACK)
    p6_black = Pawn(BLACK)
    p7_black = Pawn(BLACK)
    p8_black = Pawn(BLACK)

    p1_white = Pawn(WHITE)
    p2_white = Pawn(WHITE)
    p3_white = Pawn(WHITE)
    p4_white = Pawn(WHITE)
    p5_white = Pawn(WHITE)
    p6_white = Pawn(WHITE)
    p7_white = Pawn(WHITE)
    p8_white = Pawn(WHITE)

    app = QApplication(sys.argv)
    win = QWidget()
    grid = QGridLayout()

    position = [[False, False, False, False, False, False, False, False, False],
            [p1_black, p2_black, p3_black, p4_black, p5_black, p6_black, p7_black, p8_black],
            [False, False, False, False, False, False, False, False, False],
            [False, False, False, False, False, False, False, False, False],
            [False, False, False, False, False, False, False, False, False],
            [False, False, False, False, False, False, False, False, False],
            [p1_white, p2_white, p3_white, p4_white, p5_white, p6_white, p7_white, p8_white],
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

    def display(self):
        self.win.setLayout(self.grid)
        self.win.setWindowTitle("Chess")
        self.win.setGeometry(50,50,800,800)
        self.win.show()
        sys.exit(self.app.exec())

    def selectPiece(self, i, j):
        if(self.position[i][j]):
            print("You chose ", i, j)
            print("Possible attacks: ")
            attacks = self.position[i][j].attack(i,j)
            for attack in attacks:
                self.grid.itemAtPosition(attack[0], attack[1]).widget().setStyleSheet("background-color: red")
            moves = self.position[i][j].move(i, j)
            for move in moves:
                self.grid.itemAtPosition(move[0], move[1]).widget().setStyleSheet("background-color: green")
