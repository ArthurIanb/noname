from ui_files.save_result import Ui_Form
from PyQt5.QtWidgets import QWidget, QFileDialog


class SaveResult(QWidget, Ui_Form):
    def __init__(self, time):
        self.seconds = time['hours'] * 3600 + time['minutes'] * 60 + time['seconds'] 
        super().__init__()
        self.setupUi(self)
        self.icon_btn.clicked.connect(self.open_icon)
        self.save_btn.clicked.connect(self.save_result)
        self.cancel_btn.clicked.connect(self.close)
        self.file = None

    def open_icon(self):
        self.file, _ = QFileDialog.getOpenFileName(self, 'Open file', '', "Image files (*.jpg *.gif)")
    
    def save_result(self):
        if self.file:
            from db.db_work import DB_Work
            from manager.mang import Manager
            db = DB_Work()
            self.mang = Manager()
            name = self.name_inp.text()
            db.add_user(name, self.file, self.seconds)
            db.save()
            self.close()
            self.mang.show()

