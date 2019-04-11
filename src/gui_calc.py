# -*- coding: utf-8 -*-

##
# Form implementation generated from reading ui file 'C:\Users\42190\PycharmProjects\IVS_UI\gui_calc.ui'
# Created by: PyQt5 UI code generator 5.11.3
#
# @file gui_calc.py
# @brief GUI for fit-ivs-2 calculator.
# @author Nikolas Rada <xradan00.stud.fit.vutbr.cz>
# @author Petr Šilling <xsilli01.stud.fit.vutbr.cz>

# Project: fit-ivs-2
# Date created: 2019-03-16
# Last modified: 2019-04-11

from src.math_lib import *
from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    operation_callback = None  # currently selected operation pointer
    operand_count = -1  # number of operands necessary for the current operation (1 for sin, 2 for add and so on)

    # TODO: care about warnings (naming conventions). Also use real math characters as labels (for example '×', not '*')
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

        # number buttons
        self.zero.clicked.connect(self.print_zero)
        self.one.clicked.connect(self.print_one)
        self.two.clicked.connect(self.print_two)
        self.three.clicked.connect(self.print_three)
        self.four.clicked.connect(self.print_four)
        self.five.clicked.connect(self.print_five)
        self.six.clicked.connect(self.print_six)
        self.seven.clicked.connect(self.print_seven)
        self.eight.clicked.connect(self.print_eight)
        self.nine.clicked.connect(self.print_nine)

        # math operation buttons
        self.pow.clicked.connect(self.set_pow)
        self.pow_2.clicked.connect(self.set_pow_two)
        self.mod.clicked.connect(self.set_mod)
        self.div.clicked.connect(self.set_div)
        self.mul.clicked.connect(self.set_mul)
        self.nrt.clicked.connect(self.set_nrt)
        self.nrt_2.clicked.connect(self.set_nrt_two)
        self.sin.clicked.connect(self.set_sin)
        self.asin.clicked.connect(self.set_asin)
        self.cos.clicked.connect(self.set_cos)
        self.acos.clicked.connect(self.set_acos)
        self.add.clicked.connect(self.set_add)
        self.sub.clicked.connect(self.set_sub)
        self.xfact.clicked.connect(self.set_fact)

        # special buttons
        self.equals.clicked.connect(self.calculate_result)
        self.plusminus.clicked.connect(self.swap_sign)
        self.clear.clicked.connect(self.set_clear)
        self.dot.clicked.connect(self.print_dot)
        self.pi.clicked.connect(self.putpi)

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
        self.asin.setText(_translate("MainWindow", "asin"))
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
        self.acos.setText(_translate("MainWindow", "acos"))
        self.nrt.setText(_translate("MainWindow", "√x"))
        self.mul.setText(_translate("MainWindow", "x"))
        self.clear.setText(_translate("MainWindow", "C"))
        self.zero.setText(_translate("MainWindow", "0"))
        self.pow_2.setText(_translate("MainWindow", "x^y"))
        self.add.setText(_translate("MainWindow", "+"))

        self.label.setText("0")

    # TODO: do not allow multiple operations in selected inside the label. When switching from a dual operand to a
    #       single operand operation, use the currently written operand as the one for the single operation.
    #       Also, check for a valid result value in label_2 and use that as the first operand. This enables operation
    #       nesting, which is important.
    ##
    # @brief Sets the selected operation and its dependencies
    #
    # @param callback       Function pointer to be set
    # @param operand_count  Number of parameters necessary for the given callback
    # @param symbol         Symbol(s) to print inside the label
    def set_operation(self, callback, operand_count, symbol):
        if (operand_count != 1 and len(self.label.text()) == 0)\
                or operand_count < 1 or operand_count > 2 or callback is None:
            return

        self.operation_callback = callback
        self.operand_count = operand_count

        if operand_count == 1:
            self.label.setText(symbol + " " + self.label.text())
        else:
            self.label.setText(self.label.text() + " " + symbol + " ")

    ##
    # @brief Processes operands and, if the operation and operand count are valid, generates a result.
    #
    def calculate_result(self):
        parsed_input = self.label.text().split(" ")

        # Do not do anything when the operation does not have enough operands supplied yet.
        if len(parsed_input) < self.operand_count + 1 or parsed_input[self.operand_count] == ""\
                or parsed_input[self.operand_count] == "-":
            return

        # Try to get the result. May end up catching math library exceptions (for things like division by zero).
        result = float("nan")
        try:
            if self.operand_count == 1:
                result = self.operation_callback(float(parsed_input[0]))
            else:
                result = self.operation_callback(float(parsed_input[0]), float(parsed_input[2]))
        # TODO: Handle all the math exceptions and write an error message inside label_2. Do not forget the fact that
        #       the error message should be converted to a number (e.g. to zero) when nesting operations.
        except ValueError:
            pass
        finally:
            self.label_2.setText(str(result))

    def set_mul(self):
        self.set_operation(mul, 2, "×")

    def set_div(self):
        self.set_operation(div, 2, "÷")

    def set_pow(self):
        self.set_operation(pow, 2, "^")

    def set_pow_two(self):
        self.set_operation(pow, 2, "^")

    def set_add(self):
        self.set_operation(add, 2, "+")

    def set_sub(self):
        self.set_operation(sub, 2, "-")

    def set_mod(self):
        self.set_operation(mod, 2, "%")

    def set_nrt(self):
        self.set_operation(nrt, 2, "√")

    def set_nrt_two(self):
        self.set_operation(nrt, 2, "√")

    def swap_sign(self):
        parsed_input = self.label.text().split(" ")
        parsed_input_length = len(parsed_input)

        # Swap the sign of the currently written operand (selects the operand based on space count).
        if parsed_input_length == 1:
            if not parsed_input[0] or parsed_input[0][0] != "-":
                self.label.setText("-" + parsed_input[0])
            else:
                self.label.setText(parsed_input[0][1:])
        elif parsed_input_length == 2:
            if not parsed_input[1] or parsed_input[1][0] != "-":
                self.label.setText(parsed_input[0] + " -" + parsed_input[1])
            else:
                self.label.setText(parsed_input[0] + " " + parsed_input[1][1:])
        elif parsed_input_length == 3:
            if not parsed_input[2] or parsed_input[2][0] != "-":
                self.label.setText(parsed_input[0] + " " + parsed_input[1] + " -" + parsed_input[2])
            else:
                self.label.setText(parsed_input[0] + " " + parsed_input[1] + " " + parsed_input[2][1:])

    # TODO: combine single operand operation setters into a shared method.
    def set_fact(self):
        self.set_operation(fact, 1, "!")

    def set_cos(self):
        self.set_operation(cos, 1, "cos")

    def set_sin(self):
        self.set_operation(sin, 1, "sin")

    def set_asin(self):
        self.set_operation(asin, 1, "asin")

    def set_acos(self):
        self.set_operation(asin, 1, "acos")

    # TODO: combine print_number methods into a shared method.
    #       Look for PyQt's self.sender() reference (__init__ setup will be necessary).

    def print_zero(self):
        self.label.setText(self.label.text() + self.zero.text())

    def print_one(self):
        self.label.setText(self.label.text() + self.one.text())

    def print_two(self):
        self.label.setText(self.label.text() + self.two.text())

    def print_three(self):
        self.label.setText(self.label.text() + self.three.text())

    def print_four(self):
        self.label.setText(self.label.text() + self.four.text())

    def print_five(self):
        self.label.setText(self.label.text() + self.five.text())

    def print_six(self):
        self.label.setText(self.label.text() + self.six.text())

    def print_seven(self):
        self.label.setText(self.label.text() + self.seven.text())

    def print_eight(self):
        self.label.setText(self.label.text() + self.eight.text())

    def print_nine(self):
        self.label.setText(self.label.text() + self.nine.text())

    # TODO: Reimplement
    def set_clear(self):
            self.label.setText(" ")
            self.label.setText("0")
            self.label_2.setText(" ")
            self.first_operand = 0

    # TODO:
    #       There CAN be two dots (one in the first, one in the second operand).
    #       Please fix (for example test using the string split method).
    def print_dot(self):
            if '.' in self.label.text():
                self.label.setText(self.label.text())
            if '.' not in self.label.text():
                self.label.setText(self.label.text() + ".")

    # TODO: here check which operand is being written. Based on that replace the operand value with PI value.
    def putpi(self):
        if 'π' in self.label_2.text():
            self.label.setText("3.141592653589793")

        if 'π' not in self.label_2.text():
                self.label.setText("3.141592653589793")
                self.label_2.setText("π")


# TODO: Not sure if this is supposed to be here, really. Maybe move into something like a ui_main.py class?
if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
