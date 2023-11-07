from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QLabel, QVBoxLayout
from ui_water.game import Game
from wat.rep import Field, Ship
from wat.supermegageniusai import Dummy, SeaWolf
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
        self.size = 5
        self.bot = Dummy()
        self.mapp = Field(self.size)
        k = 0
        while self.mapp.gen_ships() == -1 and k < 100:
            k += 1
        print(k)

    def set_size(self, size):
        self.size = size
    
    def set_map(self, mapp):
        self.mapp = mapp

    def set_bot(self, bot_diff):
        if bot_diff == 0:
            self.bot = Dummy()
        elif bot_diff == 1:
            self.bot = SeaWolf()

    def open_new_game(self):
        computer_field = Field(self.size)
        human_field = self.mapp.field
        k = 0
        while computer_field.gen_ships() == -1 and k < 100:
            k += 1
        print(k)
        self.close()
        self.game_widget = Game(human_field, computer_field, self.bot)
        self.game_widget.show()
