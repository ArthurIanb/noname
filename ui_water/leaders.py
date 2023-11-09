from PyQt5.QtWidgets import QWidget, QLabel
from ui_files.leader_list import Ui_Form


class LeaderList(QWidget, Ui_Form):
    def __init__(self, leaders):
        super().__init__()
        self.setupUi(self)
        n = 0
        self.close_btn.clicked.connect(self.close)
        for i in leaders:
            n += 1
            user_id = i[0]
            name = i[1]
            file_path = i[2]
            player_date = i[3]
            time = i[4]
            lb = QLabel(self)
            lb.setText(f"{n} {name} wiv time {time} at {player_date}")
            self.leader_vl.addWidget(lb)

