from ui_files.manager import Ui_Form
from PyQt5.QtWidgets import QWidget, QHBoxLayout
from menu.menuh import Menu
from ui_water.ui_maph import UI_Field


class Manager(QWidget, Ui_Form):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("MANAGER")
        self.setupUi(self)
        self.field_size = 5
        self.bot = 0
        self.mapp = UI_Field(user=True, debug=True)
        self.mapp.field.gen_ships()
        self.mapp.update_cells()
        self.bl.addWidget(self.mapp)
        self.bl = QHBoxLayout(self)
        self.menu = Menu()
        self.next_btn.clicked.connect(self.show_window2)
        self.generate_new.clicked.connect(self.gen_new)
    
    def gen_new(self):
        self.mapp.field.clean_ships()
        self.mapp.update_cells()
        self.mapp.field.gen_ships()
        self.mapp.update_cells()
    
    def get_data(self):
        if self.size_5.isChecked():
            self.field_size = 5
        elif self.size_7.isChecked():
            self.field_size = 7
        elif self.size_10.isChecked():
            self.field_size = 10

        if self.easy_lvl.isChecked():
            self.bot = 0
        elif self.normal_lvl.isChecked():
            self.bot = 1
        elif self.hard_lvl.isChecked():
            self.bot = 2
    
    def show_window2(self):
        self.get_data()
        self.menu.set_bot(self.bot)
        self.menu.set_map(self.mapp)
        self.menu.set_size(self.field_size)
        self.close()
        self.menu.show()

