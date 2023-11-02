from PyQt5.QtWidgets import QWidget, QPushButton, QGridLayout
from wat.rep import Field
from PyQt5.QtCore import pyqtSignal, QObject


class Comunicate(QObject):
    shooted = pyqtSignal()


class UI_Field(QWidget):
    def __init__(self, field: Field, user=False):
        self.shooted = Comunicate()
        super().__init__()
        self.field = field
        self.end_turn = False
        self.cells = QGridLayout(self)
        self.buttons = []
        for i in range(len(self.field.cells)):
            self.buttons.append([])
            for j in range(len(self.field.cells[i])):
                if self.field.cells[i][j].p == '#':
                    self.buttons[i].append(QPushButton(self))
                else:
                    self.buttons[i].append(QPushButton( self))
                    
                self.cells.addWidget(self.buttons[i][j], i, j)
                if not user:
                    self.buttons[i][j].clicked.connect(self.btn_clicked)
                self.buttons[i][j].setFixedSize(75, 75)
                self.buttons[i][j].setStyleSheet("background: rgb(50, 100, 255);")
        self.setLayout(self.cells)
    
    def btn_clicked(self):
        bt = self.sender()
        for i in self.buttons:
            if bt in i:
                y = self.buttons.index(i)
                x = self.buttons[y].index(bt)
        status = self.hit_cell(x, y)
        if status != -1:
            self.shooted.shooted.emit()

    def hit_cell(self, x, y):
        stat = self.field.hit_cell(x, y)
        if self.field.cells[y][x].p == '*':
            self.buttons[y][x].setStyleSheet("background: rgb(200, 200, 200);")
        elif self.field.cells[y][x].p == 'X':
            self.buttons[y][x].setStyleSheet('background: red')
        return stat
        
    def update_cells(self):
        for i in range(len(self.field.cells)):
            for j in range(len(self.field.cells[i])):
                if self.field.cells[i][j].p == '*':
                    self.buttons[i][j].setStyleSheet("background: rgb(200, 200, 200);")
                elif self.field.cells[i][j].p == '#':
                    self.buttons[i][j].setStyleSheet('background: rgb(50, 100, 255);')
                elif self.field.cells[i][j].p == 'X':
                    self.buttons[i][j].setStyleSheet('background: red')
