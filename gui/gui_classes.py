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
        self.le_command.returnPressed.connect(self.action_btn_command)
    def action_btn_getCurrentPrice(self):
        self.te_console.append("1800 won")
    def action_btn_command(self):
        input_command_ = (self.le_command.text())
        self.te_console.append("command >> "+str(input_command_))
        self.le_command.clear()
        i = input_command_
        if i == "clear" or i == "c":
            self.te_console.clear()
        if i == "get_price":
            self.te_console.append("1800 won")



def init_windows():
    app = QApplication(sys.argv)
    main_window = main_window_class()
    main_window.show()
    app.exec_()

