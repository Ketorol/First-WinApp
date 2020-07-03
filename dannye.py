# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'dannye.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_DATA(object):
    def setupUi(self, DATA):
        DATA.setObjectName("DATA")
        DATA.resize(337, 220)
        DATA.setStyleSheet("background-color: rgb(0, 170, 255);")
        self.textBrowser = QtWidgets.QTextBrowser(DATA)
        self.textBrowser.setGeometry(QtCore.QRect(40, 20, 261, 51))
        self.textBrowser.setStyleSheet("background-color: rgb(255, 255, 127);")
        self.textBrowser.setObjectName("textBrowser")
        self.label = QtWidgets.QLabel(DATA)
        self.label.setGeometry(QtCore.QRect(40, 100, 261, 91))
        self.label.setStyleSheet("font: 20pt \"Constantia\";\n"
"color: #7FFF00;\n"
"background-color: #000000;\n"
"border: none;")
        self.label.setText("")
        self.label.setObjectName("label")

        self.retranslateUi(DATA)
        QtCore.QMetaObject.connectSlotsByName(DATA)

    def retranslateUi(self, DATA):
        _translate = QtCore.QCoreApplication.translate
        DATA.setWindowTitle(_translate("DATA", "Dialog"))
        self.textBrowser.setHtml(_translate("DATA", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt; font-weight:600;\">Сведения об атаке</span></p>\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt; font-weight:600;\">(имя, стартап, кадры на блоке):</span></p></body></html>"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    DATA = QtWidgets.QDialog()
    ui = Ui_DATA()
    ui.setupUi(DATA)
    DATA.show()
    sys.exit(app.exec_())
