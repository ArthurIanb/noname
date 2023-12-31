from PyQt5.QtWidgets import QMainWindow
from ui_water.game import Game
from wat.rep import Field
from wat.supermegageniusai import Dummy, SeaWolf, ImposibleBot
from PyQt5.QtCore import Qt
from ui_files.start import Ui_Dialog


class Menu(QMainWindow, Ui_Dialog):
    def __init__(self, parent=None):
        super().__init__(parent, Qt.WindowFlags())
        self.setWindowTitle("NO")
        self.setupUi(self)
        self.play_btn.clicked.connect(self.open_new_game)
        self.leader_btn.clicked.connect(self.show_leaders)
        self.game_widget = None
        self.size = 5
        self.ll = None
        self.bot = Dummy()
        self.mapp = Field(self.size)
        k = 0
        while self.mapp.gen_ships() == -1 and k < 100:
            k += 1
        print(k)

    def show_leaders(self):
        from db.dbwork import DbWork
        from ui_water.leaders import LeaderList
        d = DbWork()
        print(d.get_users())
        leaders = sorted([e for e in d.get_users()], key=lambda x: x[4])
        self.ll = LeaderList(leaders)
        self.ll.show()

    def set_size(self, size):
        self.size = size
    
    def set_map(self, mapp):
        self.mapp = mapp

    def set_bot(self, bot_diff):
        if bot_diff == 0:
            self.bot = Dummy()
        elif bot_diff == 1:
            self.bot = SeaWolf()
        elif bot_diff == 2:
            self.bot = ImposibleBot()

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
