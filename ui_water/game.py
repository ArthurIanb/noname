import sys
sys.path.append('/run/media/arthur/f88eefef-143a-4b79-ade7-247c117158ec/home/arthur/Documents/water')

from PyQt5.QtWidgets import QWidget, QHBoxLayout, QVBoxLayout, QLabel
from wat.rep import Field
from PyQt5 import QtCore
from ui_water.ui_maph import UI_Field
from wat.supermegageniusai import SeaWolf, Dummy
from menu.endgame import EndGame

class Game(QWidget):
    def __init__(self, users_field: Field, computers_field: Field, robot: SeaWolf, parent=None):
        super().__init__(parent, QtCore.Qt.WindowFlags())
        self.timer = QtCore.QTimer()
        self.timer.timeout.connect(self.show_time)
        self.timer.start(1000)
        self.time = {
            'hourse': 0,
            'minutes': 0,
            'seconds': 0
        }
        self.clock = QLabel(self)
        self.end_game = EndGame()
        self.humans_field = UI_Field(users_field)
        self.robots_field = UI_Field(computers_field)
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
        if self.robots_field.field.check_status() == False:
            self.human_win()
        elif self.humans_field.field.check_status() == False:
            self.robot_win()
        if self.robot_shoot:
            self.sf.shoot()
            self.humans_field.update_cells()
            self.robot_shoot = False
            self.change_state_human(True)
            
        else:
            self.change_state_robot(False)
            self.robot_shoot = True
            self.robots_field.update_cells()
            self.robots_field.shooted.shooted.emit()
    
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
        self.clock.setText(f"{self.time['hourse']}h {self.time['minutes']}m {self.time['seconds']}s")
    
    def manage_time(self):
        if self.time['seconds'] >= 60:
            k = self.time['seconds'] // 60
            self.time['seconds'] %= 60
            self.time['minutes'] += k
        if self.time['minutes'] >= 60:
            k = self.time['minutes'] // 60
            self.time['minutes'] %= 60
            self.time['hourse'] += k
        if self.time['hourse'] >= 24:
            self.time['hourse'] %= 24

    def to_seconds(self):
        out = 0
        out += self.time['hourse'] * 60 * 60
        out += self.time['minutes'] * 60
        out += self.time['seconds']
    
    def from_seconds(self, seconds):
        out = [0, 0, 0]
        if seconds >= 60:
            k = seconds // 60
            seconds %= 60
            out[1] += k
        if out[1] >= 60:
            k = out[1] // 60
            out[1] %= 60
            out[0] += k
        if out[0] >= 24:
            out[0] %= 24
