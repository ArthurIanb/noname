from PyQt5.QtWidgets import QWidget, QHBoxLayout, QVBoxLayout, QLabel
from wat.rep import Field
from PyQt5 import QtCore
from ui_water.ui_maph import UiField
from wat.supermegageniusai import SeaWolf
from menu.endgame import EndGame


class Game(QWidget):
    def __init__(self, users_field: Field, computers_field: Field, robot: SeaWolf, parent=None):
        super().__init__(parent, QtCore.Qt.WindowFlags())
        self.timer = QtCore.QTimer()
        self.timer.timeout.connect(self.show_time)
        self.timer.start(1000)
        self.time = {
            'hours': 0,
            'minutes': 0,
            'seconds': 0
        }
        self.clock = QLabel(self)
        self.end_game = EndGame()
        self.humans_field = UiField(users_field)
        self.robots_field = UiField(computers_field)
        self.humans_field.update_cells()
        self.robots_field.update_cells()
        self.change_state_human(True)
        self.humans_field.shooted.shooted.connect(self.pass_the_queue)
        self.robots_field.shooted.shooted.connect(self.pass_the_queue)
        self.robot_shoot = False

        self.sf = robot
        self.sf.set_field(self.humans_field.field)

        self.vb = QVBoxLayout(self)
        self.bl = QHBoxLayout(self)
        self.bl.addWidget(self.robots_field)
        self.bl.addWidget(self.humans_field)
        self.setLayout(self.bl)
        self.vb.addLayout(self.bl)
        self.vb.addWidget(self.clock)
    
    def pass_the_queue(self):
        if self.robot_shoot:
            self.sf.shoot()
            self.humans_field.update_cells()
            self.robot_shoot = False
            self.change_state_human(True)
            if not self.humans_field.field.check_status():
                self.robot_win()
        else:
            self.change_state_robot(False)
            self.robot_shoot = True
            self.robots_field.update_cells()
            self.robots_field.shooted.shooted.emit()
            if not self.robots_field.field.check_status():
                self.human_win()
    
    def change_state_human(self, state):
        for i in range(len(self.humans_field.field.cells)):
            for j in range(len(self.humans_field.field.cells[i])):
                self.humans_field.buttons[i][j].setDisabled(state)

    def change_state_robot(self, state):
        for i in range(len(self.robots_field.field.cells)):
            for j in range(len(self.robots_field.field.cells[i])):
                self.robots_field.buttons[i][j].setDisabled(state)
    
    def human_win(self):
        self.end_game.win_or_loose(True, self.time)
        self.close()
        self.end_game.show()

    def robot_win(self):
        self.end_game.win_or_loose(False)
        self.close()
        self.end_game.show()
    
    def show_time(self):
        self.time['seconds'] += 1
        self.manage_time()
        self.clock.setText(f"{self.time['hours']}h {self.time['minutes']}m {self.time['seconds']}s")
    
    def manage_time(self):
        if self.time['seconds'] >= 60:
            k = self.time['seconds'] // 60
            self.time['seconds'] %= 60
            self.time['minutes'] += k
        if self.time['minutes'] >= 60:
            k = self.time['minutes'] // 60
            self.time['minutes'] %= 60
            self.time['hours'] += k
        if self.time['hours'] >= 24:
            self.time['hours'] %= 24

    def to_seconds(self):
        out = 0
        out += self.time['hours'] * 60 * 60
        out += self.time['minutes'] * 60
        out += self.time['seconds']
