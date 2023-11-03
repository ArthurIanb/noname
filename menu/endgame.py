from PyQt5.QtWidgets import QWidget, QPushButton, QLabel, QVBoxLayout
import sys


class EndGame(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("result")
        self.setFixedSize(200, 170)
        self.bl = QVBoxLayout(self)
        self.message = QLabel(self)
        self.ok_btn = QPushButton("ok", self)
        self.save_result_btn = QPushButton("Сохранить результат", self)
        self.bl.addWidget(self.message)
        self.bl.addWidget(self.ok_btn)
        self.bl.addWidget(self.save_result_btn)
        self.setLayout(self.bl)
        self.ok_btn.clicked.connect(self.ok_clicked)

    def win_or_loose(self, win=True, time=0):
        if win:
            self.message.setText(f"Поздравляю!\nВы победили\nВаше время {time['hourse']}ч {time['minutes']}м {time['seconds']}с")
        else:
            self.message.setText("Вы проиграли, можете сразиться еще раз")
    
    def ok_clicked(self):
        self.close()
        from manager.mang import Manager
        self.mang = Manager()
        self.mang.show()
