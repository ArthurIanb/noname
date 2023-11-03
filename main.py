from menu.menuh import Menu
from PyQt5.QtWidgets import QApplication
import sys

app = QApplication(sys.argv)
m = Menu()
m.show()
app.exit(app.exec())