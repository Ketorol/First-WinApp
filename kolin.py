# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'kolin.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_KOLIN(object):
    def setupUi(self, KOLIN):
        KOLIN.setObjectName("KOLIN")
        KOLIN.resize(337, 220)
        KOLIN.setStyleSheet("background-color: rgb(0, 170, 255);")
        self.mkkolin = QtWidgets.QPushButton(KOLIN)
        self.mkkolin.setGeometry(QtCore.QRect(40, 90, 111, 91))
        self.mkkolin.setStyleSheet("font: 16pt \"Constantia\";\n"
"background-color: rgb(170, 255, 255);")
        self.mkkolin.setObjectName("mkkolin")
        self.hpkolin = QtWidgets.QPushButton(KOLIN)
        self.hpkolin.setGeometry(QtCore.QRect(190, 90, 111, 91))
        self.hpkolin.setStyleSheet("font: 16pt \"Constantia\";\n"
"background-color: rgb(170, 255, 255);")
        self.hpkolin.setObjectName("hpkolin")
        self.textBrowser = QtWidgets.QTextBrowser(KOLIN)
        self.textBrowser.setGeometry(QtCore.QRect(40, 20, 261, 51))
        self.textBrowser.setStyleSheet("background-color: rgb(255, 255, 127);")
        self.textBrowser.setObjectName("textBrowser")

        self.retranslateUi(KOLIN)
        QtCore.QMetaObject.connectSlotsByName(KOLIN)

    def retranslateUi(self, KOLIN):
        _translate = QtCore.QCoreApplication.translate
        KOLIN.setWindowTitle(_translate("KOLIN", "Dialog"))
        self.mkkolin.setText(_translate("KOLIN", "2MK"))
        self.hpkolin.setText(_translate("KOLIN", "2HP"))
        self.textBrowser.setHtml(_translate("KOLIN", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt; font-weight:600;\">Какой удар будем изучать?</span></p></body></html>"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    KOLIN = QtWidgets.QDialog()
    ui = Ui_KOLIN()
    ui.setupUi(KOLIN)
    KOLIN.show()
    sys.exit(app.exec_())
