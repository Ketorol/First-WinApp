# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'kolin.ui'
#
# Created by: PyQt5 UI code generator 5.15.0
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_KOLIN(object):
    def setupUi(self, KOLIN):
        KOLIN.setObjectName("KOLIN")
        KOLIN.resize(430, 331)
        self.mkkolin = QtWidgets.QPushButton(KOLIN)
        self.mkkolin.setGeometry(QtCore.QRect(50, 200, 121, 81))
        self.mkkolin.setObjectName("mkkolin")
        self.hpkolin = QtWidgets.QPushButton(KOLIN)
        self.hpkolin.setGeometry(QtCore.QRect(250, 200, 121, 81))
        self.hpkolin.setObjectName("hpkolin")
        self.kolinlabel = QtWidgets.QLabel(KOLIN)
        self.kolinlabel.setGeometry(QtCore.QRect(80, 40, 251, 71))
        self.kolinlabel.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.kolinlabel.setStyleSheet("font: 75 italic 14pt \"Times New Roman\";\n"
"color: rgb(0, 0, 0);\n"
"background-color: rgb(255, 255, 255);")
        self.kolinlabel.setTextFormat(QtCore.Qt.RichText)
        self.kolinlabel.setObjectName("kolinlabel")

        self.retranslateUi(KOLIN)
        QtCore.QMetaObject.connectSlotsByName(KOLIN)

    def retranslateUi(self, KOLIN):
        _translate = QtCore.QCoreApplication.translate
        KOLIN.setWindowTitle(_translate("KOLIN", "Form"))
        self.mkkolin.setText(_translate("KOLIN", "2MK"))
        self.hpkolin.setText(_translate("KOLIN", "2HP"))
        self.kolinlabel.setText(_translate("KOLIN", "Какой удар будем изучать?"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    KOLIN = QtWidgets.QWidget()
    ui = Ui_KOLIN()
    ui.setupUi(KOLIN)
    KOLIN.show()
    sys.exit(app.exec_())
