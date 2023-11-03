from ui_files.manager import Ui_Form
from PyQt5.QtWidgets import QWidget
from menu.menuh import Menu


class Manager(QWidget, Ui_Form):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.menu = Menu()
        self.play_btn.clicked.connect(self.show_window2)
    
    def show_window2(self):
        self.close()
        self.menu.show()

