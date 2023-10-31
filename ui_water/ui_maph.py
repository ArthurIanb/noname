from PyQt5.QtWidgets import QWidget, QPushButton, QGridLayout
from wat.rep import Field


class UI_Field(QWidget):
    def __init__(self, field: Field, user=False):
        super().__init__()
        self.field = field
        self.end_turn = False
        self.cells = QGridLayout(self)
        self.buttons = []
        for i in range(len(self.field.cells)):
            self.buttons.append([])
            for j in range(len(self.field.cells[i])):
                if self.field.cells[i][j].p == '#':
                    self.buttons[i].append(QPushButton('_', self))
                else:
                    self.buttons[i].append(QPushButton(self.field.cells[i][j].p, self))
                self.cells.addWidget(self.buttons[i][j], i, j)
                if not user:
                    self.buttons[i][j].clicked.connect(self.btn_clicked)
                self.buttons[i][j].setFixedSize(75, 75)               
        print([e.text()  for k in self.buttons for e in k])
        self.setLayout(self.cells)
    
    def btn_clicked(self):
        bt = self.sender()
        for i in self.buttons:
            if bt in i:
                y = self.buttons.index(i)
                x = self.buttons[y].index(bt)
        self.hit_cell(x, y)

    def hit_cell(self, x, y):
        self.field.hit_cell(x, y)
        self.buttons[y][x].setText(self.field.cells[y][x].p)
        
        
