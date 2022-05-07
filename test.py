import sys
from PySide6.QtWidgets import QApplication, QWidget, QPushButton, QGridLayout
from PySide6.QtGui import QIcon
from PySide6.QtCore import Slot, QSize


app = QApplication(sys.argv)
win = QWidget()
grid = QGridLayout()

def setBoard():
    grid.itemAtPosition(7,0).widget().setIcon(QIcon('img/rook_w.png'))
    grid.itemAtPosition(7,1).widget().setIcon(QIcon('img/knight_w.png'))
    grid.itemAtPosition(7,2).widget().setIcon(QIcon('img/bishop_w.png'))
    grid.itemAtPosition(7,3).widget().setIcon(QIcon('img/queen_w.png'))
    grid.itemAtPosition(7,4).widget().setIcon(QIcon('img/king_w.png'))
    grid.itemAtPosition(7,5).widget().setIcon(QIcon('img/bishop_w.png'))
    grid.itemAtPosition(7,6).widget().setIcon(QIcon('img/knight_w.png'))
    grid.itemAtPosition(7,7).widget().setIcon(QIcon('img/rook_w.png'))
    for i in range(8):
        grid.itemAtPosition(6,i).widget().setIcon(QIcon('img/pawn_w.png'))
    
    grid.itemAtPosition(0,0).widget().setIcon(QIcon('img/rook_b.png'))
    grid.itemAtPosition(0,1).widget().setIcon(QIcon('img/knight_b.png'))
    grid.itemAtPosition(0,2).widget().setIcon(QIcon('img/bishop_b.png'))
    grid.itemAtPosition(0,3).widget().setIcon(QIcon('img/queen_b.png'))
    grid.itemAtPosition(0,4).widget().setIcon(QIcon('img/king_b.png'))
    grid.itemAtPosition(0,5).widget().setIcon(QIcon('img/bishop_b.png'))
    grid.itemAtPosition(0,6).widget().setIcon(QIcon('img/knight_b.png'))
    grid.itemAtPosition(0,7).widget().setIcon(QIcon('img/rook_b.png'))
    for i in range(8):
        grid.itemAtPosition(1,i).widget().setIcon(QIcon('img/pawn_b.png'))

def makeUI():
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
            grid.addWidget(button, i, j)

makeUI()
setBoard()
win.setLayout(grid)
win.setWindowTitle("Chess")
win.setGeometry(50,50,800,800)
win.show()
sys.exit(app.exec())
