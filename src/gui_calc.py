# -*- coding: utf-8 -*-

##
# @file gui_calc.py
#
# @brief GUI for fit-ivs-2 calculator.
# Created by: PyQt5 UI code generator 5.11.3. Slightly refactored afterwards.
#
# @author Petr Šilling <xsilli01.stud.fit.vutbr.cz>
# @author Nikolas Rada <xradan00.stud.fit.vutbr.cz>

# Project: fit-ivs-2
# Date created: 2019-03-16
# Last modified: 2019-04-14

from src.math_lib import *
from PyQt5 import QtCore, QtGui, QtWidgets


class UiMainWindow(QtWidgets.QMainWindow):
    operation_callback = None  # currently selected operation pointer
    operand_count = -1  # number of operands necessary for the current operation (1 for sin, 2 for add and so on)
    operation_pointers = {
        "sin": sin,
        "cos": cos,
        "asin": asin,
        "acos": acos,
        "n!": fact,
        "+": add,
        "−": sub,
        "×": mul,
        "÷": div,
        "%": mod,
        "^": pow,
        "√": nrt
    }  # text inside button : corresponding math function pointer dictionary

    def __init__(self):
        super().__init__()

        # main window setup
        self.setObjectName("MainWindow")
        self.resize(503, 653)
        self.setStyleSheet(
            "background-color: qlineargradient(spread:pad, x1:1, y1:0.113773, x2:1, y2:0.892,"
            "stop:0 rgba(126, 123, 194, 255), stop:1 rgba(219, 129, 137, 255));"
        )
        self.central_widget = QtWidgets.QWidget(self)
        self.central_widget.setStyleSheet(
            "QWidget{background-color: \"transparent\";}\n"
            "QPushButton{color: \"white\";}\n"
            "QPushButton{background-color: \"transparent\";}\n"
            "QFrame{background-color: \"transparent\";}\n"
            "QLabel{color: \"white\";}"
        )
        self.central_widget.setObjectName("central_widget")

        # button frame setup
        self.frame = QtWidgets.QFrame(self.central_widget)
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

        # button setup
        font = QtGui.QFont()
        font.setPointSize(17)
        self.dot = QtWidgets.QPushButton(self.frame_2)
        self.dot.setGeometry(QtCore.QRect(224, 291, 64, 43))
        self.dot.setFont(font)
        self.dot.setObjectName("dot")
        self.dot.setText(".")
        self.five = QtWidgets.QPushButton(self.frame_2)
        self.five.setGeometry(QtCore.QRect(224, 167, 64, 43))
        self.five.setFont(font)
        self.five.setObjectName("five")
        self.five.setText("5")
        self.six = QtWidgets.QPushButton(self.frame_2)
        self.six.setGeometry(QtCore.QRect(295, 167, 64, 43))
        self.six.setFont(font)
        self.six.setObjectName("six")
        self.six.setText("6")
        self.nrt_2 = QtWidgets.QPushButton(self.frame_2)
        self.nrt_2.setGeometry(QtCore.QRect(11, 105, 64, 43))
        self.nrt_2.setFont(font)
        self.nrt_2.setObjectName("nrt_2")
        self.nrt_2.setText("√x")
        self.sub = QtWidgets.QPushButton(self.frame_2)
        self.sub.setGeometry(QtCore.QRect(366, 167, 64, 43))
        self.sub.setFont(font)
        self.sub.setObjectName("sub")
        self.sub.setText("−")
        self.two = QtWidgets.QPushButton(self.frame_2)
        self.two.setGeometry(QtCore.QRect(224, 229, 64, 43))
        self.two.setFont(font)
        self.two.setObjectName("two")
        self.two.setText("2")
        self.pi = QtWidgets.QPushButton(self.frame_2)
        self.pi.setGeometry(QtCore.QRect(11, 291, 64, 43))
        self.pi.setFont(font)
        self.pi.setObjectName("pi")
        self.pi.setText("π")
        self.nine = QtWidgets.QPushButton(self.frame_2)
        self.nine.setGeometry(QtCore.QRect(295, 105, 64, 43))
        self.nine.setFont(font)
        self.nine.setObjectName("nine")
        self.nine.setText("9")
        self.div = QtWidgets.QPushButton(self.frame_2)
        self.div.setGeometry(QtCore.QRect(366, 43, 64, 43))
        self.div.setFont(font)
        self.div.setObjectName("div")
        self.div.setText("÷")
        self.mod = QtWidgets.QPushButton(self.frame_2)
        self.mod.setGeometry(QtCore.QRect(295, 43, 64, 43))
        self.mod.setFont(font)
        self.mod.setObjectName("mod")
        self.mod.setText("%")
        self.equals = QtWidgets.QPushButton(self.frame_2)
        self.equals.setGeometry(QtCore.QRect(295, 291, 135, 43))
        self.equals.setFont(font)
        self.equals.setObjectName("equals")
        self.equals.setText("=")
        self.eight = QtWidgets.QPushButton(self.frame_2)
        self.eight.setGeometry(QtCore.QRect(224, 105, 64, 43))
        self.eight.setFont(font)
        self.eight.setObjectName("eight")
        self.eight.setText("8")
        self.pow = QtWidgets.QPushButton(self.frame_2)
        self.pow.setGeometry(QtCore.QRect(82, 43, 64, 43))
        self.pow.setFont(font)
        self.pow.setObjectName("pow")
        self.pow.setText("x^n")
        self.seven = QtWidgets.QPushButton(self.frame_2)
        self.seven.setGeometry(QtCore.QRect(153, 105, 64, 43))
        self.seven.setFont(font)
        self.seven.setObjectName("seven")
        self.seven.setText("7")
        self.four = QtWidgets.QPushButton(self.frame_2)
        self.four.setGeometry(QtCore.QRect(153, 167, 64, 43))
        self.four.setFont(font)
        self.four.setObjectName("four")
        self.four.setText("4")
        self.one = QtWidgets.QPushButton(self.frame_2)
        self.one.setGeometry(QtCore.QRect(153, 229, 64, 43))
        self.one.setFont(font)
        self.one.setObjectName("one")
        self.one.setText("1")
        self.three = QtWidgets.QPushButton(self.frame_2)
        self.three.setGeometry(QtCore.QRect(295, 229, 64, 43))
        self.three.setFont(font)
        self.three.setObjectName("three")
        self.three.setText("3")
        self.plusminus = QtWidgets.QPushButton(self.frame_2)
        self.plusminus.setGeometry(QtCore.QRect(224, 43, 64, 42))
        self.plusminus.setFont(font)
        self.plusminus.setObjectName("plusminus")
        self.plusminus.setText("±")
        self.xfact = QtWidgets.QPushButton(self.frame_2)
        self.xfact.setGeometry(QtCore.QRect(82, 291, 64, 43))
        self.xfact.setFont(font)
        self.xfact.setObjectName("xfact")
        self.xfact.setText("n!")
        font.setPointSize(15)
        self.asin = QtWidgets.QPushButton(self.frame_2)
        self.asin.setGeometry(QtCore.QRect(11, 229, 64, 43))
        self.asin.setFont(font)
        self.asin.setObjectName("asin")
        self.asin.setText("asin")
        self.cos = QtWidgets.QPushButton(self.frame_2)
        self.cos.setGeometry(QtCore.QRect(82, 167, 64, 43))
        self.cos.setFont(font)
        self.cos.setObjectName("cos")
        self.cos.setText("cos")
        self.sin = QtWidgets.QPushButton(self.frame_2)
        self.sin.setGeometry(QtCore.QRect(82, 229, 64, 43))
        self.sin.setFont(font)
        self.sin.setObjectName("sin")
        self.sin.setText("sin")
        self.acos = QtWidgets.QPushButton(self.frame_2)
        self.acos.setGeometry(QtCore.QRect(11, 167, 64, 43))
        self.acos.setFont(font)
        self.acos.setObjectName("acos")
        self.acos.setText("acos")
        font.setPointSize(17)
        self.nrt = QtWidgets.QPushButton(self.frame_2)
        self.nrt.setGeometry(QtCore.QRect(82, 105, 64, 43))
        self.nrt.setFont(font)
        self.nrt.setObjectName("nrt")
        self.nrt.setText("y√x")
        self.mul = QtWidgets.QPushButton(self.frame_2)
        self.mul.setGeometry(QtCore.QRect(366, 105, 64, 43))
        self.mul.setFont(font)
        self.mul.setObjectName("mul")
        self.mul.setText("×")
        self.clear = QtWidgets.QPushButton(self.frame_2)
        self.clear.setGeometry(QtCore.QRect(153, 43, 64, 43))
        self.clear.setFont(font)
        self.clear.setObjectName("clear")
        self.clear.setText("C")
        self.zero = QtWidgets.QPushButton(self.frame_2)
        self.zero.setGeometry(QtCore.QRect(153, 291, 64, 43))
        self.zero.setFont(font)
        self.zero.setObjectName("zero")
        self.zero.setText("0")
        self.pow_2 = QtWidgets.QPushButton(self.frame_2)
        self.pow_2.setGeometry(QtCore.QRect(11, 43, 64, 43))
        self.pow_2.setFont(font)
        self.pow_2.setObjectName("pow_2")
        self.pow_2.setText("x²")
        self.add = QtWidgets.QPushButton(self.frame_2)
        self.add.setGeometry(QtCore.QRect(366, 229, 64, 43))
        self.add.setFont(font)
        self.add.setObjectName("add")
        self.add.setText("+")

        # label frame setup
        self.frame_3 = QtWidgets.QFrame(self.frame)
        self.frame_3.setGeometry(QtCore.QRect(40, 30, 421, 211))
        self.frame_3.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_3.setObjectName("frame_3")

        # label setup
        font.setPointSize(18)
        self.label = QtWidgets.QLabel(self.frame_3)
        self.label.setGeometry(QtCore.QRect(70, 40, 271, 51))
        self.label.setFont(font)
        self.label.setStyleSheet("color: rgb(255, 255, 255);")
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.label.setText("0")
        self.label_2 = QtWidgets.QLabel(self.frame_3)
        self.label_2.setGeometry(QtCore.QRect(40, 110, 331, 71))
        self.label_2.setFont(font)
        self.label_2.setStyleSheet("color: rgb(255, 255, 255);")
        self.label_2.setText("")
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName("label_2")
        self.setCentralWidget(self.central_widget)

        # connect events and actions
        QtCore.QMetaObject.connectSlotsByName(self)

        # connect number button actions
        self.zero.clicked.connect(self.print_number)
        self.one.clicked.connect(self.print_number)
        self.two.clicked.connect(self.print_number)
        self.three.clicked.connect(self.print_number)
        self.four.clicked.connect(self.print_number)
        self.five.clicked.connect(self.print_number)
        self.six.clicked.connect(self.print_number)
        self.seven.clicked.connect(self.print_number)
        self.eight.clicked.connect(self.print_number)
        self.nine.clicked.connect(self.print_number)

        # connect math operation button actions
        self.add.clicked.connect(self.set_two_operand_operation)
        self.sub.clicked.connect(self.set_two_operand_operation)
        self.mod.clicked.connect(self.set_two_operand_operation)
        self.div.clicked.connect(self.set_two_operand_operation)
        self.mul.clicked.connect(self.set_two_operand_operation)
        self.sin.clicked.connect(self.set_single_operand_operation)
        self.asin.clicked.connect(self.set_single_operand_operation)
        self.cos.clicked.connect(self.set_single_operand_operation)
        self.acos.clicked.connect(self.set_single_operand_operation)
        self.xfact.clicked.connect(self.set_single_operand_operation)
        self.nrt.clicked.connect(self.set_nrt)
        self.nrt_2.clicked.connect(self.set_nrt_two)
        self.pow.clicked.connect(self.set_pow)
        self.pow_2.clicked.connect(self.set_pow_two)

        # connect special button actions
        self.equals.clicked.connect(self.calculate_result)
        self.plusminus.clicked.connect(self.swap_sign)
        self.clear.clicked.connect(self.clear_calc)
        self.dot.clicked.connect(self.print_dot)
        self.pi.clicked.connect(self.print_pi)

        # make ui visible after setup
        self.show()

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
                result = self.operation_callback(float(parsed_input[1]))

            elif self.operation_callback == (pow or nrt):
                result = self.operation_callback(float(parsed_input[0]), int(parsed_input[2]))

            elif self.operation_callback == div:
                if parsed_input[2] == '0':
                    result = "Error division by zero!"
                else:
                    result = self.operation_callback(float(parsed_input[0]), float(parsed_input[2]))
            else:
                result = self.operation_callback(float(parsed_input[0]), float(parsed_input[2]))

        # TODO: Handle all the math exceptions and write an error message inside label_2. Do not forget the fact that
        #       the error message should be converted to a number (e.g. to zero) when nesting operations.
        except ValueError:
            pass
        finally:
            self.label_2.setText(str(result))

    def set_single_operand_operation(self):
        text = self.sender().text()
        self.set_operation(self.operation_pointers[text], 1, text)

    def set_two_operand_operation(self):
        text = self.sender().text()
        self.set_operation(self.operation_pointers[text], 2, text)

    def set_pow(self):
        self.set_operation(self.operation_pointers["^"], 2, "^")

    def set_pow_two(self):
        self.set_pow()
        self.label.setText(self.label.text() + "2")

    def set_nrt(self):
        self.set_operation(self.operation_pointers["√"], 2, "√")

    def set_nrt_two(self):
        number_holder = self.label.text()
        self.label.setText("2")
        self.set_nrt()
        self.label.setText(self.label.text() + number_holder)

    def swap_sign(self):
        parsed_input = self.label.text().split(" ")
        parsed_input_length = len(parsed_input)

        # Swap the sign of the currently written operand (selects the operand based on space count).
        if parsed_input_length == 1 and parsed_input[0] and parsed_input[0][0] != "0":
            if not parsed_input[0] or parsed_input[0][0] != "-":
                self.label.setText("-" + parsed_input[0])
            else:
                self.label.setText(parsed_input[0][1:])
        elif parsed_input_length == 2 and parsed_input[1] and parsed_input[1][0] != "0":
            if not parsed_input[1] or parsed_input[1][0] != "-":
                self.label.setText(parsed_input[0] + " -" + parsed_input[1])
            else:
                self.label.setText(parsed_input[0] + " " + parsed_input[1][1:])
        elif parsed_input_length == 3 and parsed_input[2] and parsed_input[2][0] != "0":
            if not parsed_input[2] or parsed_input[2][0] != "-":
                self.label.setText(parsed_input[0] + " " + parsed_input[1] + " -" + parsed_input[2])
            else:
                self.label.setText(parsed_input[0] + " " + parsed_input[1] + " " + parsed_input[2][1:])

    def print_number(self):
        number_string = self.sender().text()
        parsed_input = self.label.text().split(" ")
        parsed_input_length = len(parsed_input)

        if parsed_input_length == 1:
            if parsed_input[0] and '0' in parsed_input[0][0] and '.' not in parsed_input[0]:
                self.label.setText(number_string)
            else:
                self.label.setText(parsed_input[0] + number_string)
        elif parsed_input_length == 2:
            if parsed_input[1] and '0' in parsed_input[1][0] and '.' not in parsed_input[1]:
                self.label.setText(parsed_input[0] + " " + number_string)
            else:
                self.label.setText(parsed_input[0] + " " + parsed_input[1] + number_string)
        elif parsed_input_length == 3:
            if parsed_input[2] and '0' in parsed_input[2][0] and '.' not in parsed_input[2]:
                self.label.setText(parsed_input[0] + " " + parsed_input[1] + " " + number_string)
            else:
                self.label.setText(parsed_input[0] + " " + parsed_input[1] + " " + parsed_input[2] + number_string)

    def print_dot(self):
        parsed_input = self.label.text().split(" ")
        parsed_input_length = len(parsed_input)

        if parsed_input_length == 1:
            if '.' not in parsed_input[0]:
                self.label.setText(parsed_input[0] + ".")
        elif parsed_input_length == 2:
            if '.' not in parsed_input[1]:
                self.label.setText(parsed_input[0] + " " + parsed_input[1] + ".")
        elif parsed_input_length == 3:
            if '.' not in parsed_input[2]:
                self.label.setText(parsed_input[0] + " " + parsed_input[1] + " " + parsed_input[2] + ".")

    def print_pi(self):
        parsed_input = self.label.text().split(" ")
        parsed_input_length = len(parsed_input)

        if parsed_input_length == 1:
            self.label.setText("3.141592653589793")
        elif parsed_input_length == 2:
            self.label.setText(parsed_input[0] + " " + "3.141592653589793")
        elif parsed_input_length == 3:
            self.label.setText(parsed_input[0] + " " + parsed_input[1] + " " + "3.141592653589793")

    def clear_calc(self):
        self.label.setText("0")
        self.label_2.setText(" ")


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = UiMainWindow()
    sys.exit(app.exec_())
