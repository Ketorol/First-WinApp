import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from functools import partial
from mainwin import *
from akuma import *
from kolin import *
class MainOkno(QtWidgets.QMainWindow):
    def __init__(self, parent=None):
        QtWidgets.QWidget.__init__(self, parent)
        self.ui = Ui_CharMenu()
        self.ui.setupUi(self)
        self.ui.Akuma.clicked.connect(partial(self.LOL1, "Akuma"))
        self.ui.Kolin.clicked.connect(partial(self.LOL2, "Kolin"))
        self.Ak = AkumaWin ()
        self.Ko = KolinWin ()
    def LOL1(self, char1):
        self.Ak.show()
    def LOL2(self, char2):
        self.Ko.show()

class AkumaWin(QtWidgets.QWidget):
    def __init__(self, parent=None):
        QtWidgets.QWidget.__init__(self, parent)
        self.Ak = Ui_AKUMA()
        self.Ak.setupUi(self)
        self.Ak.mkakuma.clicked.connect(partial(self.LOL3, "5MK"))
        self.Ak.hpakuma.clicked.connect(partial(self.LOL4, "2HP"))
    
    def mbox(self, body, title='Выбрана атака:'):
        dialog = QMessageBox(QMessageBox.Information, title, body)
        dialog.exec_()

    def LOL3(self, atak1):
        self.mbox("5MK")


    def LOL4(self, atak2):
        self.mbox("2HP")


class KolinWin(QtWidgets.QWidget):
    def __init__(self, parent=None):
        QtWidgets.QWidget.__init__(self, parent)
        self.Ko = Ui_KOLIN()
        self.Ko.setupUi(self)
        self.Ko.mkkolin.clicked.connect(partial(self.LOL5, "2MK"))
        self.Ko.hpkolin.clicked.connect(partial(self.LOL6, "2HP"))
    
    def mbox(self, body, title='Выбрана атака:'):
        dialog = QMessageBox(QMessageBox.Information, title, body)
        dialog.exec_()
    
    def LOL5(self, atak3):
        self.mbox("2MK")

    def LOL6(self, atak4):
        self.mbox("2HP")

def run():
    application = QApplication(sys.argv)
    myapp = MainOkno()
    myapp.show()
    application.exec_()
run()
