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
        self.ui = Ui_GlavOkno()
        self.ui.setupUi(self)
        self.ui.Akuma.clicked.connect(partial(self.LOL1, "Akuma"))
        self.ui.Kolin.clicked.connect(partial(self.LOL2, "Kolin"))
        self.Ak = AkumaWin ()
        self.Ko = KolinWin ()
    def LOL1(self):
        self.Ak.show()
    def LOL2(self):
        self.Ko.show()

class AkumaWin(QtWidgets.QWidget):
    def __init__(self, parent=None):
        QtWidgets.QWidget.__init__(self, parent)
        self.Ak = Ui_AKUMA()
        self.Ak.setupUi(self)
        self.Ak.mkakuma.clicked.connect(partial(self.LOL3, "mkakuma"))
        self.Ak.hpakuma.clicked.connect(partial(self.LOL4, "hpakuma"))
    
    def mbox(self, body, title='Выбрана атака:'):
        dialog = Qmessagebox(Qmessagebox.Information, title, body)
        dialog.exec_()

    def LOL3(self):
        self.mbox("5MK")


    def LOL4(self):
        self.mbox("2HP")


class KolinWin(QtWidgets.QWidget):
    def __init__(self, parent=None):
        QtWidgets.QWidget.__init__(self, parent)
        self.Ko = Ui_KOLIN()
        self.Ko.setupUi(self)
        self.Ko.mkkolin.clicked.connect(partial(self.LOL5, "mkkolin"))
        self.Ko.hpkolin.clicked.connect(partial(self.LOL6, "hpkolin"))
    
    def mbox(self, body, title='Выбрана атака:'):
        dialog = Qmessagebox(Qmessagebox.Information, title, body)
        dialog.exec_()
    
    def LOL5(self):
        self.mbox("2MK")

    def LOL6(self):
        self.mbox("2HP")

def run():
    application = QApplication(sys.argv)
    myapp = MainOkno()
    myapp.show()
    application.exec_()
run()
