import sys
sys.path.append('/run/media/arthur/f88eefef-143a-4b79-ade7-247c117158ec/home/arthur/Documents/water')

from PyQt5.QtWidgets import QApplication, QWidget, QHBoxLayout
from wat.rep import Field, Ship
from ui_maph import UI_Field


class Game(QWidget):
    def __init__(self, users_field: Field, computers_field: Field):
        super().__init__()
        f1 = UI_Field(users_field)
        f2 = UI_Field(computers_field)
        bl = QHBoxLayout(self)
        bl.addWidget(f1)
        bl.addWidget(f2)


if __name__ == '__main__':
    coords = [
        (0, 0, 3, False),
        (4, 0, 4, True),
        (1, 2, 2, False),
        (0, 4, 1, False)
    ]

    coords2 = [
        (0, 1, 3, True),
        (2, 1, 1, False),
        (4, 0, 2, True),
        (2, 3, 2, False)
    ]

    computer_field = Field(5)
    human_field = Field(5)
    for i in coords:
        s = Ship(*i)
        computer_field.add_ship(s)

    for i in coords2:
        s = Ship(*i)
        human_field.add_ship(s)
    
    app = QApplication(sys.argv)
    w = Game(human_field, computer_field)
    w.show()
    app.exit(app.exec())
