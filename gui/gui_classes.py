from PyQt5.QtWidgets import *
from PyQt5 import uic
import sys

main_ui_form = uic.loadUiType("gui/main_gui.ui")[0]
class main_window_class(QMainWindow, main_ui_form) :
    def __init__(self) :
        super().__init__()
        self.setupUi(self)

def init_windows():
    app = QApplication(sys.argv)
    main_window = main_window_class()
    main_window.show()
    app.exec_()

