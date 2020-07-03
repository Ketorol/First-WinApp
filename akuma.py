# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'akuma.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_AKUMA(object):
    def setupUi(self, AKUMA):
        AKUMA.setObjectName("AKUMA")
        AKUMA.resize(335, 221)
        AKUMA.setStyleSheet("background-color: rgb(0, 170, 255);")
        self.mkakuma = QtWidgets.QPushButton(AKUMA)
        self.mkakuma.setGeometry(QtCore.QRect(40, 90, 111, 91))
        self.mkakuma.setStyleSheet("font: 16pt \"Constantia\";\n"
"background-color: rgb(170, 255, 255);")
        self.mkakuma.setObjectName("mkakuma")
        self.hpakuma = QtWidgets.QPushButton(AKUMA)
        self.hpakuma.setGeometry(QtCore.QRect(190, 90, 111, 91))
        self.hpakuma.setStyleSheet("font: 16pt \"Constantia\";\n"
"background-color: rgb(170, 255, 255);")
        self.hpakuma.setObjectName("hpakuma")
        self.textBrowser = QtWidgets.QTextBrowser(AKUMA)
        self.textBrowser.setGeometry(QtCore.QRect(40, 20, 261, 51))
        self.textBrowser.setStyleSheet("background-color: rgb(255, 255, 127);")
        self.textBrowser.setObjectName("textBrowser")

        self.retranslateUi(AKUMA)
        QtCore.QMetaObject.connectSlotsByName(AKUMA)

    def retranslateUi(self, AKUMA):
        _translate = QtCore.QCoreApplication.translate
        AKUMA.setWindowTitle(_translate("AKUMA", "Dialog"))
        self.mkakuma.setText(_translate("AKUMA", "5MK"))
        self.hpakuma.setText(_translate("AKUMA", "2HP"))
        self.textBrowser.setHtml(_translate("AKUMA", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt; font-weight:600;\">Какой удар будем изучать?</span></p></body></html>"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    AKUMA = QtWidgets.QDialog()
    ui = Ui_AKUMA()
    ui.setupUi(AKUMA)
    AKUMA.show()
    sys.exit(app.exec_())
