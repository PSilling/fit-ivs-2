# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Users\42190\PycharmProjects\IVS_UI\gui_calc.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from src.math_lib import *
from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    first_operand = 0
    negate_operand = 0
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(503, 653)
        MainWindow.setStyleSheet("background-color: qlineargradient(spread:pad, x1:1, y1:0.113773, x2:1, y2:0.892, stop:0 rgba(126, 123, 194, 255), stop:1 rgba(219, 129, 137, 255));\n"
"\n"
"\n"
"\n"
"")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setStyleSheet("QWidget{background-color: \"transparent\";}\n"
"\n"
"QPushButton{color: \"white\";}\n"
"\n"
"QPushButton{background-color: \"transparent\";}\n"
"\n"
"QFrame{background-color: \"transparent\";}\n"
"\n"
"QLabel{color: \"white\";}")
        self.centralwidget.setObjectName("centralwidget")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setGeometry(QtCore.QRect(0, 0, 501, 681))
        self.frame.setAutoFillBackground(False)
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.frame_2 = QtWidgets.QFrame(self.frame)
        self.frame_2.setEnabled(True)
        self.frame_2.setGeometry(QtCore.QRect(30, 240, 441, 361))
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.dot = QtWidgets.QPushButton(self.frame_2)
        self.dot.setGeometry(QtCore.QRect(295, 291, 64, 43))
        font = QtGui.QFont()
        font.setPointSize(17)
        font.setBold(False)
        font.setWeight(50)
        self.dot.setFont(font)
        self.dot.setObjectName("dot")
        self.five = QtWidgets.QPushButton(self.frame_2)
        self.five.setGeometry(QtCore.QRect(224, 167, 64, 43))
        font = QtGui.QFont()
        font.setPointSize(17)
        font.setBold(False)
        font.setWeight(50)
        self.five.setFont(font)
        self.five.setObjectName("five")
        self.six = QtWidgets.QPushButton(self.frame_2)
        self.six.setGeometry(QtCore.QRect(295, 167, 64, 43))
        font = QtGui.QFont()
        font.setPointSize(17)
        font.setBold(False)
        font.setWeight(50)
        self.six.setFont(font)
        self.six.setObjectName("six")
        self.nrt_2 = QtWidgets.QPushButton(self.frame_2)
        self.nrt_2.setGeometry(QtCore.QRect(11, 105, 64, 43))
        font = QtGui.QFont()
        font.setPointSize(17)
        font.setBold(False)
        font.setWeight(50)
        self.nrt_2.setFont(font)
        self.nrt_2.setObjectName("nrt_2")
        self.sub = QtWidgets.QPushButton(self.frame_2)
        self.sub.setGeometry(QtCore.QRect(366, 167, 64, 43))
        font = QtGui.QFont()
        font.setPointSize(17)
        font.setBold(False)
        font.setWeight(50)
        self.sub.setFont(font)
        self.sub.setObjectName("sub")
        self.two = QtWidgets.QPushButton(self.frame_2)
        self.two.setGeometry(QtCore.QRect(224, 229, 64, 43))
        font = QtGui.QFont()
        font.setPointSize(17)
        font.setBold(False)
        font.setWeight(50)
        self.two.setFont(font)
        self.two.setObjectName("two")
        self.pi = QtWidgets.QPushButton(self.frame_2)
        self.pi.setGeometry(QtCore.QRect(11, 294, 64, 37))
        font = QtGui.QFont()
        font.setFamily("MS Sans Serif")
        font.setPointSize(15)
        font.setBold(False)
        font.setWeight(50)
        self.pi.setFont(font)
        self.pi.setObjectName("pi")
        self.nine = QtWidgets.QPushButton(self.frame_2)
        self.nine.setGeometry(QtCore.QRect(295, 105, 64, 43))
        font = QtGui.QFont()
        font.setPointSize(17)
        font.setBold(False)
        font.setWeight(50)
        self.nine.setFont(font)
        self.nine.setObjectName("nine")
        self.div = QtWidgets.QPushButton(self.frame_2)
        self.div.setGeometry(QtCore.QRect(366, 43, 64, 43))
        font = QtGui.QFont()
        font.setPointSize(17)
        font.setBold(False)
        font.setWeight(50)
        self.div.setFont(font)
        self.div.setObjectName("div")
        self.asin = QtWidgets.QPushButton(self.frame_2)
        self.asin.setGeometry(QtCore.QRect(11, 232, 64, 36))
        font = QtGui.QFont()
        font.setPointSize(13)
        font.setBold(False)
        font.setWeight(50)
        font.setStrikeOut(False)
        self.asin.setFont(font)
        self.asin.setObjectName("asin")
        self.mod = QtWidgets.QPushButton(self.frame_2)
        self.mod.setGeometry(QtCore.QRect(295, 43, 64, 43))
        font = QtGui.QFont()
        font.setPointSize(17)
        font.setBold(False)
        font.setWeight(50)
        self.mod.setFont(font)
        self.mod.setObjectName("mod")
        self.equals = QtWidgets.QPushButton(self.frame_2)
        self.equals.setGeometry(QtCore.QRect(366, 291, 64, 43))
        font = QtGui.QFont()
        font.setPointSize(17)
        font.setBold(False)
        font.setWeight(50)
        self.equals.setFont(font)
        self.equals.setObjectName("equals")
        self.cos = QtWidgets.QPushButton(self.frame_2)
        self.cos.setGeometry(QtCore.QRect(82, 170, 64, 36))
        font = QtGui.QFont()
        font.setPointSize(13)
        font.setBold(False)
        font.setWeight(50)
        self.cos.setFont(font)
        self.cos.setObjectName("cos")
        self.eight = QtWidgets.QPushButton(self.frame_2)
        self.eight.setGeometry(QtCore.QRect(224, 105, 64, 43))
        font = QtGui.QFont()
        font.setPointSize(17)
        font.setBold(False)
        font.setWeight(50)
        self.eight.setFont(font)
        self.eight.setObjectName("eight")
        self.sin = QtWidgets.QPushButton(self.frame_2)
        self.sin.setGeometry(QtCore.QRect(82, 232, 64, 36))
        font = QtGui.QFont()
        font.setPointSize(13)
        font.setBold(False)
        font.setWeight(50)
        self.sin.setFont(font)
        self.sin.setObjectName("sin")
        self.pow = QtWidgets.QPushButton(self.frame_2)
        self.pow.setGeometry(QtCore.QRect(82, 43, 64, 43))
        font = QtGui.QFont()
        font.setPointSize(17)
        font.setBold(False)
        font.setWeight(50)
        self.pow.setFont(font)
        self.pow.setObjectName("pow")
        self.seven = QtWidgets.QPushButton(self.frame_2)
        self.seven.setGeometry(QtCore.QRect(153, 105, 64, 43))
        font = QtGui.QFont()
        font.setPointSize(17)
        font.setBold(False)
        font.setWeight(50)
        self.seven.setFont(font)
        self.seven.setObjectName("seven")
        self.four = QtWidgets.QPushButton(self.frame_2)
        self.four.setGeometry(QtCore.QRect(153, 167, 64, 43))
        font = QtGui.QFont()
        font.setPointSize(17)
        font.setBold(False)
        font.setWeight(50)
        self.four.setFont(font)
        self.four.setObjectName("four")
        self.one = QtWidgets.QPushButton(self.frame_2)
        self.one.setGeometry(QtCore.QRect(153, 229, 64, 43))
        font = QtGui.QFont()
        font.setPointSize(17)
        font.setBold(False)
        font.setWeight(50)
        self.one.setFont(font)
        self.one.setObjectName("one")
        self.three = QtWidgets.QPushButton(self.frame_2)
        self.three.setGeometry(QtCore.QRect(295, 229, 64, 43))
        font = QtGui.QFont()
        font.setPointSize(17)
        font.setBold(False)
        font.setWeight(50)
        self.three.setFont(font)
        self.three.setObjectName("three")
        self.plusminus = QtWidgets.QPushButton(self.frame_2)
        self.plusminus.setGeometry(QtCore.QRect(224, 43, 64, 42))
        font = QtGui.QFont()
        font.setFamily("Perpetua Titling MT")
        font.setPointSize(17)
        font.setBold(False)
        font.setWeight(50)
        self.plusminus.setFont(font)
        self.plusminus.setObjectName("plusminus")
        self.xfact = QtWidgets.QPushButton(self.frame_2)
        self.xfact.setGeometry(QtCore.QRect(82, 293, 64, 39))
        font = QtGui.QFont()
        font.setPointSize(15)
        font.setBold(False)
        font.setWeight(50)
        self.xfact.setFont(font)
        self.xfact.setObjectName("xfact")
        self.acos = QtWidgets.QPushButton(self.frame_2)
        self.acos.setGeometry(QtCore.QRect(11, 170, 64, 36))
        font = QtGui.QFont()
        font.setPointSize(13)
        font.setBold(False)
        font.setWeight(50)
        font.setStrikeOut(False)
        self.acos.setFont(font)
        self.acos.setObjectName("acos")
        self.nrt = QtWidgets.QPushButton(self.frame_2)
        self.nrt.setGeometry(QtCore.QRect(82, 105, 64, 43))
        font = QtGui.QFont()
        font.setPointSize(17)
        font.setBold(False)
        font.setWeight(50)
        self.nrt.setFont(font)
        self.nrt.setObjectName("nrt")
        self.mul = QtWidgets.QPushButton(self.frame_2)
        self.mul.setGeometry(QtCore.QRect(366, 105, 64, 43))
        font = QtGui.QFont()
        font.setPointSize(17)
        font.setBold(False)
        font.setWeight(50)
        self.mul.setFont(font)
        self.mul.setObjectName("mul")
        self.clear = QtWidgets.QPushButton(self.frame_2)
        self.clear.setGeometry(QtCore.QRect(153, 43, 64, 43))
        font = QtGui.QFont()
        font.setPointSize(17)
        font.setBold(False)
        font.setWeight(50)
        self.clear.setFont(font)
        self.clear.setObjectName("clear")
        self.zero = QtWidgets.QPushButton(self.frame_2)
        self.zero.setGeometry(QtCore.QRect(153, 291, 64, 43))
        font = QtGui.QFont()
        font.setPointSize(17)
        font.setBold(False)
        font.setWeight(50)
        self.zero.setFont(font)
        self.zero.setObjectName("zero")
        self.pow_2 = QtWidgets.QPushButton(self.frame_2)
        self.pow_2.setGeometry(QtCore.QRect(11, 43, 64, 43))
        font = QtGui.QFont()
        font.setPointSize(17)
        font.setBold(False)
        font.setWeight(50)
        self.pow_2.setFont(font)
        self.pow_2.setObjectName("pow_2")
        self.add = QtWidgets.QPushButton(self.frame_2)
        self.add.setGeometry(QtCore.QRect(366, 229, 64, 43))
        font = QtGui.QFont()
        font.setPointSize(17)
        font.setBold(False)
        font.setWeight(50)
        self.add.setFont(font)
        self.add.setObjectName("add")
        self.frame_3 = QtWidgets.QFrame(self.frame)
        self.frame_3.setGeometry(QtCore.QRect(40, 30, 421, 211))
        self.frame_3.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_3.setObjectName("frame_3")
        self.label = QtWidgets.QLabel(self.frame_3)
        self.label.setGeometry(QtCore.QRect(70, 40, 271, 51))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label.setFont(font)
        self.label.setStyleSheet("color: rgb(255, 255, 255);")
        self.label.setText("")
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.frame_3)
        self.label_2.setGeometry(QtCore.QRect(40, 110, 331, 71))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_2.setFont(font)
        self.label_2.setStyleSheet("color: rgb(255, 255, 255);")
        self.label_2.setText("")
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName("label_2")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        self.zero.clicked.connect(self.print0)
        self.one.clicked.connect(self.print1)
        self.two.clicked.connect(self.print2)
        self.three.clicked.connect(self.print3)
        self.four.clicked.connect(self.print4)
        self.five.clicked.connect(self.print5)
        self.six.clicked.connect(self.print6)
        self.seven.clicked.connect(self.print7)
        self.eight.clicked.connect(self.print8)
        self.nine.clicked.connect(self.print9)
        self.pow.clicked.connect(self.setoperationpow)
        self.pow_2.clicked.connect(self.setoperationpow_2)
        self.plusminus.clicked.connect(self.setoperationplusminus)
        self.mod.clicked.connect(self.setoperationmod)
        self.div.clicked.connect(self.setoperationdiv)
        self.mul.clicked.connect(self.setoperationmul)
        self.nrt.clicked.connect(self.setoperationnrt)
        self.nrt_2.clicked.connect(self.setoperationnrt_2)
        self.sin.clicked.connect(self.setoperationsin)
        self.asin.clicked.connect(self.setoperationasin)
        self.cos.clicked.connect(self.setoperationcos)
        self.acos.clicked.connect(self.setoperationacos)
        self.add.clicked.connect(self.setoperationadd)
        self.sub.clicked.connect(self.setoperationsub)
        self.dot.clicked.connect(self.printdot)
        self.equals.clicked.connect(self.finishoperation)
        self.pi.clicked.connect(self.putpi)
        self.xfact.clicked.connect(self.setoperationfact)
        self.clear.clicked.connect(self.printclear)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.dot.setText(_translate("MainWindow", "."))
        self.five.setText(_translate("MainWindow", "5"))
        self.six.setText(_translate("MainWindow", "6"))
        self.nrt_2.setText(_translate("MainWindow", "y√x"))
        self.sub.setText(_translate("MainWindow", "-"))
        self.two.setText(_translate("MainWindow", "2"))
        self.pi.setText(_translate("MainWindow", "π"))
        self.nine.setText(_translate("MainWindow", "9"))
        self.div.setText(_translate("MainWindow", "÷"))
        self.asin.setText(_translate("MainWindow", "sin-1"))
        self.mod.setText(_translate("MainWindow", "%"))
        self.equals.setText(_translate("MainWindow", "="))
        self.cos.setText(_translate("MainWindow", "cos"))
        self.eight.setText(_translate("MainWindow", "8"))
        self.sin.setText(_translate("MainWindow", "sin"))
        self.pow.setText(_translate("MainWindow", "x²"))
        self.seven.setText(_translate("MainWindow", "7"))
        self.four.setText(_translate("MainWindow", "4"))
        self.one.setText(_translate("MainWindow", "1"))
        self.three.setText(_translate("MainWindow", "3"))
        self.plusminus.setText(_translate("MainWindow", "±"))
        self.xfact.setText(_translate("MainWindow", "x!"))
        self.acos.setText(_translate("MainWindow", "cos-1"))
        self.nrt.setText(_translate("MainWindow", "√x"))
        self.mul.setText(_translate("MainWindow", "x"))
        self.clear.setText(_translate("MainWindow", "C"))
        self.zero.setText(_translate("MainWindow", "0"))
        self.pow_2.setText(_translate("MainWindow", "x^y"))
        self.add.setText(_translate("MainWindow", "+"))

    def finishoperation(self):
        if self.label.text() == " ":
            self.label.setText(str(self.operation_callback(self.first_operand)))
            self.label_2.setText("=")
        else:
            self.label.setText(str(self.operation_callback(self.first_operand, int(self.label.text()))))  # UP line
            self.label_2.setText("=")


    def setoperationmul(self):
        self.first_operand = float(self.label.text())
        self.operation_callback = mul
        self.label.setText(" ")
        self.label_2.setText("x")

    def setoperationdiv(self):
        self.first_operand = float(self.label.text())
        self.operation_callback = div
        self.label.setText(" ")
        self.label_2.setText("÷")

    def setoperationpow(self):
        self.first_operand = float(self.label.text())
        self.operation_callback = pow
        self.label.setText("2")
        self.label_2.setText("^")

    def setoperationpow_2(self):
        self.first_operand = float(self.label.text())
        self.operation_callback = pow
        self.label.setText(" ")
        self.label_2.setText("^")

    def setoperationadd(self):
        self.first_operand = float(self.label.text())
        self.operation_callback = add
        self.label.setText(" ")
        self.label_2.setText("+")

    def setoperationsub(self):
        self.first_operand = float(self.label.text())
        self.operation_callback = sub
        self.label.setText(" ")
        self.label_2.setText("-")

    def setoperationmod(self):
        self.first_operand = float(self.label.text())
        self.operation_callback = mod
        self.label.setText(" ")
        self.label_2.setText("%")

    def setoperationnrt(self):
        self.first_operand = float(self.label.text())
        self.operation_callback = nrt
        self.label.setText("2")
        self.label_2.setText("√")

    def setoperationnrt_2(self):
        self.first_operand = float(self.label.text())
        self.operation_callback = nrt
        self.label.setText(" ")
        self.label_2.setText("√")

    def setoperationplusminus(self):
        self.first_operand = float(self.label.text())
        self.negate_operand = str(self.first_operand * (-1))
        self.label.setText(self.negate_operand)

    def setoperationfact(self):
        self.first_operand = int(self.label.text())
        self.operation_callback = fact
        self.label.setText(" ")
        self.label_2.setText("!")

    def setoperationcos(self):
        self.first_operand = float(self.label.text())
        self.operation_callback = cos
        self.label.setText(" ")
        self.label_2.setText("cos")

    def setoperationsin(self):
        self.first_operand = float(self.label.text())
        self.operation_callback = sin
        self.label.setText(" ")
        self.label_2.setText("sin")

    def setoperationasin(self):
        self.first_operand = float(self.label.text())
        self.operation_callback = asin
        self.label.setText(" ")
        self.label_2.setText("sin-1")

    def setoperationacos(self):
        self.first_operand = float(self.label.text())
        self.operation_callback = acos
        self.label.setText(" ")
        self.label_2.setText("cos-1")



    def print0(self):
            self.label.setText(self.label.text() + "0")

    def print1(self):
            self.label.setText(self.label.text() + "1")

    def print2(self):
            self.label.setText(self.label.text() + "2")

    def print3(self):
            self.label.setText(self.label.text() + "3")

    def print4(self):
            self.label.setText(self.label.text() + "4")

    def print5(self):
            self.label.setText(self.label.text() + "5")

    def print6(self):
            self.label.setText(self.label.text() + "6")

    def print7(self):
            self.label.setText(self.label.text() + "7")

    def print8(self):
            self.label.setText(self.label.text() + "8")

    def print9(self):
            self.label.setText(self.label.text() + "9")

    def printclear(self):
            self.label.setText(" ")
            self.label_2.setText(" ")

    def printdot(self):
            self.label.setText(self.label.text() + ".")

    def putpi(self):
            self.label.setText(self.label.text() + "3.141592653589793")
            self.label_2.setText("π")


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

