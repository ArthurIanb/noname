from PyQt5.QtWidgets import QApplication
import sys
from manager.mang import Manager


a = QApplication(sys.argv)
w = Manager()
w.show()
a.exit(a.exec())
