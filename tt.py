from PyQt5.QtWidgets import QApplication
import sys
from manager.mang import Manager
from db.db_work import DB_Work
from menu.menuh import Menu
from menu.save_result import SaveResult



app = QApplication(sys.argv)
w = SaveResult()
w.show()
app.exit(app.exec())

