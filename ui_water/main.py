import sys
sys.path.append('/run/media/arthur/f88eefef-143a-4b79-ade7-247c117158ec/home/arthur/Documents/water')

from PyQt5.QtWidgets import QApplication, QWidget, QHBoxLayout, QPushButton, QLabel
from wat.rep import Field, Ship
from ui_maph import UI_Field
from wat.supermegageniusai import SeaWolf, Dummy

class Game(QWidget):
    def __init__(self, users_field: Field, computers_field: Field, robot: SeaWolf):
        super().__init__()
        self.humans_field = UI_Field(users_field)
        self.robots_field = UI_Field(computers_field)
        self.change_state_human(True)
        self.humans_field.shooted.shooted.connect(self.pass_the_queue)
        self.robots_field.shooted.shooted.connect(self.pass_the_queue)
        self.robot_shoot = False

        self.sf = robot
        self.sf.set_field(self.humans_field.field)
        bl = QHBoxLayout(self)
        bl.addWidget(self.robots_field)
        bl.addWidget(self.humans_field)
    
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
        print("HUMAN")
        sys.exit()

    def robot_win(self):
        print("ROBOT")
        sys.exit()


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
    
    d = Dummy()
    app = QApplication(sys.argv)
    w = Game(human_field, computer_field, d)
    w.show()
    app.exit(app.exec())
