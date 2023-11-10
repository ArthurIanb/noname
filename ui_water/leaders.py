from PyQt5.QtWidgets import QWidget, QLabel
from ui_files.leader_list import Ui_Form
from os.path import exists


def from_seconds(seconds):
    out = [0, 0, seconds]
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
    return out


class LeaderList(QWidget, Ui_Form):
    def __init__(self, leaders):
        super().__init__()
        self.setupUi(self)
        n = 0
        self.close_btn.clicked.connect(self.close)
        for i in leaders:
            n += 1
            name = i[1]
            file_path = i[2]
            player_date = i[3]
            time = i[4]
            lb = QLabel(self)
            time = from_seconds(time)
            if exists(file_path):
                print(time)
                lb.setText(f"<span>{n}</span><img src={file_path} "
                           f"width=100 align='top'/><span>{name} со временем {time[0]}ч {time[1]}м "
                           f"{time[2]}с|{player_date}</span>")
            else:
                lb.setText(f'<span>{n}.</span><<span>{name} со временем {time[0]}ч {time[1]}м '
                           f'{time[2]}с</span>')
            self.leader_vl.addWidget(lb)
