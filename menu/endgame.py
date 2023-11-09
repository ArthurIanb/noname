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
        self.save_result_btn.clicked.connect(self.save_result)
        self.bl.addWidget(self.message)
        self.bl.addWidget(self.ok_btn)
        self.bl.addWidget(self.save_result_btn)
        self.setLayout(self.bl)
        self.win = False
        self.ok_btn.clicked.connect(self.ok_clicked)

    def win_or_loose(self, win=True, time=None):
        self.win = win
        self.time = time
        if win and time:
            self.message.setText(f"Поздравляю!\nВы победили\nВаше время {time['hours']}ч {time['minutes']}м {time['seconds']}с")
        else:
            self.message.setText("Вы проиграли\nМожете сразиться еще раз")
            
    
    def ok_clicked(self):
        self.close()
        from manager.mang import Manager
        self.mang = Manager()
        self.mang.show()
    
    def save_result(self):
        if self.win:
            from menu.save_result import SaveResult
            self.s = SaveResult(self.time)
            self.close()
            self.s.show()
