from PyQt5.QtWidgets import *
from PyQt5 import uic
import sys
import api
from gui.color import *
from PyQt5.QtGui import *
main_ui_form = uic.loadUiType("gui/main_gui.ui")[0]
class main_window_class(QMainWindow, main_ui_form) :
    def __init__(self) :
        super().__init__()
        self.setupUi(self)
        self.btn_getCurrentPrice.clicked.connect(self.action_btn_getCurrentPrice)
        self.btn_command.clicked.connect(self.action_btn_command)
        self.le_command.returnPressed.connect(self.action_btn_command)
        self.insert_order_data()
    def action_btn_getCurrentPrice(self):
        self.te_console.append("1800 won") # 수정필요

    # command 창 관련함수
    def action_btn_command(self):
        input_command_ = (self.le_command.text())
        self.te_console.append("command >> "+str(input_command_))
        self.le_command.clear()
        i = input_command_
        if i == "clear" or i == "c":
            self.te_console.clear()
        if i == "get_price":
            self.te_console.append("1800 won") # 수정필요
        if i == "m":
            money_ = round(float(api.get_currency_balance("KRW")))
            self.te_console.setTextColor(QColor(0,255,0)) # 돈 출력부 색을 녹색으로 출력하도록 함
            self.te_console.append(str(money_)+"₩")
            self.te_console.setTextColor(QColor(255,255,255))

    def insert_order_data(self):
        self.tb_order.setItem(1, 1, QTableWidgetItem("1행 1열"))

def init_windows():
    app = QApplication(sys.argv)
    main_window = main_window_class()
    main_window.show()
    app.exec_()

