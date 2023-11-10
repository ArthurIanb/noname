from PyQt5.QtWidgets import QWidget, QPushButton, QGridLayout
from wat.rep import Field
from PyQt5.QtCore import pyqtSignal, QObject, Qt


class Comunicate(QObject):
    shooted = pyqtSignal()


class UiField(QWidget):
    def __init__(self, field: Field = None, user=False, debug=False, show_ships=False, parent=None):
        self.shooted = Comunicate()
        self.debug_on = debug
        self.show_ships = show_ships
        super().__init__(parent, Qt.WindowFlags())
        self.field = field
        self.end_turn = False
        self.cells = QGridLayout(self)
        self.buttons = []
        if not self.field:
            self.field = Field(5)
        size = 75
        if len(self.field.cells) == 7:
            size = 54
        elif len(self.field.cells) == 10:
            size = 38
        for i in range(len(self.field.cells)):
            self.buttons.append([])
            for j in range(len(self.field.cells[i])):
                self.buttons[i].append(QPushButton(self))
                self.buttons[i][j].setStyleSheet("background: rgb(50, 100, 255);")
                
                self.cells.addWidget(self.buttons[i][j], i, j)
                if not user:
                    self.buttons[i][j].clicked.connect(self.btn_clicked)
                self.buttons[i][j].setFixedSize(size, size)
                
        self.setLayout(self.cells)
    
    def set_field(self, field):
        self.buttons = []
        self.field = field
        if len(field.cells) == 5:
            size = 75
        elif len(field.cells) == 7:
            size = 54
        elif len(field.cells) == 10:
            size = 38
        for i in range(self.field.size):
            self.buttons.append([])
            for j in range(self.field.size):
                self.buttons[i].append(QPushButton(self))
                if self.field.cells[i][j].p == '#' or self.show_ships:
                    self.buttons[i][j].setStyleSheet("background: rgb(50, 100, 255);")
                else:
                    self.buttons[i][j].setStyleSheet("background: rgb(0, 100, 255);")
                self.cells.addWidget(self.buttons[i][j], i, j)
                self.buttons[i][j].setFixedSize(size, size)
        self.setLayout(self.cells)

    def set_field_by_size(self, size):
        f = Field(size)
        self.set_field(f)
    
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
        for i in range(self.field.size):
            for j in range(self.field.size):
                if not self.debug_on:
                    if self.field.cells[i][j].p == '*':
                        self.buttons[i][j].setStyleSheet("background: rgb(200, 200, 200);")
                    elif self.field.cells[i][j].p == '#':
                        self.buttons[i][j].setStyleSheet('background: rgb(50, 100, 255);')
                    elif self.field.cells[i][j].p == 'X':
                        self.buttons[i][j].setStyleSheet('background: red')
                else:
                    if self.field.cells[i][j].p == '#':
                        self.buttons[i][j].setStyleSheet("background: black;")
                    elif self.field.cells[i][j].p == 'X':
                        self.buttons[i][j].setStyleSheet('background: red')
                    elif self.field.cells[i][j].p == '*':
                        self.buttons[i][j].setStyleSheet("background: rgb(200, 200, 200);")
                    else:
                        self.buttons[i][j].setStyleSheet("background: rgb(0, 100, 255);")
                
