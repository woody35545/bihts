from PyQt5.QtWidgets import *
from PyQt5 import uic
import sys

main_ui_form = uic.loadUiType("gui/main_gui.ui")[0]
class main_window_class(QMainWindow, main_ui_form) :
    def __init__(self) :
        super().__init__()
        self.setupUi(self)
        self.btn_getCurrentPrice.clicked.connect(self.action_btn_getCurrentPrice)
        self.btn_command.clicked.connect(self.action_btn_command)
    def action_btn_getCurrentPrice(self):
        self.te_console.append("1800 won")
    def action_btn_command(self):
        input_command_ = (self.te_command.toPlainText())
        self.te_console.append(input_command_)

        self.te_command.clear()

def init_windows():
    app = QApplication(sys.argv)
    main_window = main_window_class()
    main_window.show()
    app.exec_()

