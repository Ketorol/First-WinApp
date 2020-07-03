# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mainwin.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_CharMenu(object):
    def setupUi(self, CharMenu):
        CharMenu.setObjectName("CharMenu")
        CharMenu.resize(332, 221)
        CharMenu.setStyleSheet("background-color: rgb(0, 170, 255);")
        self.centralwidget = QtWidgets.QWidget(CharMenu)
        self.centralwidget.setObjectName("centralwidget")
        self.Akuma = QtWidgets.QPushButton(self.centralwidget)
        self.Akuma.setGeometry(QtCore.QRect(30, 90, 111, 91))
        self.Akuma.setStyleSheet("font: 16pt \"Constantia\";\n"
"background-color: rgb(170, 255, 255);")
        self.Akuma.setObjectName("Akuma")
        self.Kolin = QtWidgets.QPushButton(self.centralwidget)
        self.Kolin.setGeometry(QtCore.QRect(180, 90, 111, 91))
        self.Kolin.setStyleSheet("font: 16pt \"Constantia\";\n"
"background-color: rgb(170, 255, 255);")
        self.Kolin.setObjectName("Kolin")
        self.textBrowser = QtWidgets.QTextBrowser(self.centralwidget)
        self.textBrowser.setGeometry(QtCore.QRect(30, 20, 261, 51))
        self.textBrowser.setStyleSheet("background-color: rgb(255, 255, 127);")
        self.textBrowser.setObjectName("textBrowser")
        CharMenu.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(CharMenu)
        self.statusbar.setObjectName("statusbar")
        CharMenu.setStatusBar(self.statusbar)

        self.retranslateUi(CharMenu)
        QtCore.QMetaObject.connectSlotsByName(CharMenu)

    def retranslateUi(self, CharMenu):
        _translate = QtCore.QCoreApplication.translate
        CharMenu.setWindowTitle(_translate("CharMenu", "MainWindow"))
        self.Akuma.setText(_translate("CharMenu", "Akuma"))
        self.Kolin.setText(_translate("CharMenu", "Kolin"))
        self.textBrowser.setHtml(_translate("CharMenu", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt; font-weight:600;\">Какого персонажа будем изучать?</span></p></body></html>"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    CharMenu = QtWidgets.QMainWindow()
    ui = Ui_CharMenu()
    ui.setupUi(CharMenu)
    CharMenu.show()
    sys.exit(app.exec_())
