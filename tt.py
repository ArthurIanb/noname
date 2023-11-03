from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel
from PyQt5.QtCore import QTimer
import sys
from manager.mang import Manager


a = QApplication(sys.argv)
w = Manager()
w.show()
a.exit(a.exec())