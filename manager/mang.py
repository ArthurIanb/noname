from ui_files.manager import Ui_Form
from PyQt5.QtWidgets import QWidget
from menu.menuh import Menu
from ui_water.ui_maph import UiField


class Manager(QWidget, Ui_Form):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("MANAGER")
        self.setupUi(self)
        self.field_size = 5
        self.bot = 0
        self.mapp = UiField(user=True, debug=True)
        k = 0
        while self.mapp.field.gen_ships() == -1 and k < 103:
            k += 1
        print(k)
        self.mapp.update_cells()
        self.bl_1.addWidget(self.mapp)
        self.menu = Menu()
        self.next_btn.clicked.connect(self.show_window2)
        self.generate_new.clicked.connect(self.gen_new)
    
    def gen_new(self):
        # self.mapp.update_cells()
        self.bl_1.removeWidget(self.mapp)
        self.mapp = UiField(user=True, debug=True)
        self.bl_1.addWidget(self.mapp)
        self.get_data()
        print('field_size', self.field_size)
        self.mapp.set_field_by_size(self.field_size)
        self.mapp.field.clean_ships()
        self.mapp.update_cells()
        k = 0
        while self.mapp.field.gen_ships() == -1 and k < 100:
            k += 1
            print(k)
        print(k)
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
