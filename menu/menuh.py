from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QLabel, QVBoxLayout
from ui_water.game import Game
from wat.rep import Field, Ship
from wat.supermegageniusai import Dummy
from PyQt5.QtCore import Qt
from ui_files.start import Ui_Dialog
import sys


class Menu(QMainWindow, Ui_Dialog):
    def __init__(self, parent=None):
        super().__init__(parent, Qt.WindowFlags())
        self.setWindowTitle("NO")
        self.setupUi(self)
        self.play_btn.clicked.connect(self.open_new_game)
        self.game_widget = None
        

    def open_new_game(self):
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
        self.close()
        d = Dummy()
        self.game_widget = Game(human_field, computer_field, d)
        self.game_widget.show()
