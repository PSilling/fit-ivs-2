# -*- coding: utf-8 -*-

##
# @file gui_calc.py
# @brief GUI for fit-ivs-2 calculator.
# @author Petr Šilling <xsilli01.stud.fit.vutbr.cz>
# @author Nikolas Rada <xradan00.stud.fit.vutbr.cz>
#
# Created by: PyQt5 UI code generator 5.11.3. Slightly refactored afterwards.
# * Project: fit-ivs-2
# * Date created: 2019-03-16
# * Last modified: 2019-04-14
#

from math_lib import *
from PyQt5 import QtCore, QtGui, QtWidgets


##
# @defgroup gui GUI
# @brief GUI connected to the mathematical library.
# @{
#


##
# @brief Main GUI window connected to the mathematical library.
#
class UiMainWindow(QtWidgets.QMainWindow):

    ##
    # Currently selected operation pointer.
    #
    operation_callback = None

    ##
    # Number of operands necessary for the current operation (1 for sin, 2 for add and so on).
    #
    operand_count = -1

    ##
    # Text inside button : corresponding math function pointer dictionary.
    #
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
    }

    ##
    # Whether label_2 currently holds a correct result value.
    #
    result_set = False

    ##
    # The currently pressed key from a keyboard event, or None.
    #
    pressed_key = None

    ##
    # Sets up the main UI window including all buttons (connecting them to actions as well) and labels,
    # setting the UI visible after it's done.
    #
    # @brief Initial setup of the main UI window for the calculator.
    #
    def __init__(self):
        super().__init__()

        # main window setup
        self.setObjectName("MainWindow")
        self.setFixedSize(503, 653)
        self.setStyleSheet(
            "background-color: qlineargradient(spread:pad, x1:1, y1:0.113773, x2:1, y2:0.892,"
            "stop:0 rgba(126, 123, 194, 255), stop:1 rgba(219, 129, 137, 255));"
        )
        self.central_widget = QtWidgets.QWidget(self)
        self.central_widget.setStyleSheet(
            "QWidget{background-color: \"transparent\";}\n"
            "QPushButton{color: \"white\"; background-color: \"transparent\" }\n"
            "QPushButton:pressed{ background-color: \"#555\"; }"
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
        font = QtGui.QFont("Monaco", 18)
        self.dot = QtWidgets.QPushButton(self.frame_2)
        self.dot.setGeometry(QtCore.QRect(224, 291, 64, 43))
        self.dot.setFont(font)
        self.dot.setObjectName("dot")
        self.dot.setText(".")
        self.dot.setFlat(True)
        self.dot.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.five = QtWidgets.QPushButton(self.frame_2)
        self.five.setGeometry(QtCore.QRect(224, 167, 64, 43))
        self.five.setFont(font)
        self.five.setObjectName("five")
        self.five.setText("5")
        self.five.setFlat(True)
        self.five.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.six = QtWidgets.QPushButton(self.frame_2)
        self.six.setGeometry(QtCore.QRect(295, 167, 64, 43))
        self.six.setFont(font)
        self.six.setObjectName("six")
        self.six.setText("6")
        self.six.setFlat(True)
        self.six.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.nrt_2 = QtWidgets.QPushButton(self.frame_2)
        self.nrt_2.setGeometry(QtCore.QRect(11, 105, 64, 43))
        self.nrt_2.setFont(font)
        self.nrt_2.setObjectName("nrt_2")
        self.nrt_2.setText("√x")
        self.nrt_2.setFlat(True)
        self.nrt_2.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.sub = QtWidgets.QPushButton(self.frame_2)
        self.sub.setGeometry(QtCore.QRect(366, 167, 64, 43))
        self.sub.setFont(font)
        self.sub.setObjectName("sub")
        self.sub.setText("−")
        self.sub.setFlat(True)
        self.sub.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.two = QtWidgets.QPushButton(self.frame_2)
        self.two.setGeometry(QtCore.QRect(224, 229, 64, 43))
        self.two.setFont(font)
        self.two.setObjectName("two")
        self.two.setText("2")
        self.two.setFlat(True)
        self.two.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pi = QtWidgets.QPushButton(self.frame_2)
        self.pi.setGeometry(QtCore.QRect(11, 291, 64, 43))
        self.pi.setFont(font)
        self.pi.setObjectName("pi")
        self.pi.setText("π")
        self.pi.setFlat(True)
        self.pi.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.nine = QtWidgets.QPushButton(self.frame_2)
        self.nine.setGeometry(QtCore.QRect(295, 105, 64, 43))
        self.nine.setFont(font)
        self.nine.setObjectName("nine")
        self.nine.setText("9")
        self.nine.setFlat(True)
        self.nine.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.div = QtWidgets.QPushButton(self.frame_2)
        self.div.setGeometry(QtCore.QRect(366, 43, 64, 43))
        self.div.setFont(font)
        self.div.setObjectName("div")
        self.div.setText("÷")
        self.div.setFlat(True)
        self.div.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.mod = QtWidgets.QPushButton(self.frame_2)
        self.mod.setGeometry(QtCore.QRect(295, 43, 64, 43))
        self.mod.setFont(font)
        self.mod.setObjectName("mod")
        self.mod.setText("%")
        self.mod.setFlat(True)
        self.mod.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.equals = QtWidgets.QPushButton(self.frame_2)
        self.equals.setGeometry(QtCore.QRect(295, 291, 135, 43))
        self.equals.setFont(font)
        self.equals.setObjectName("equals")
        self.equals.setText("=")
        self.equals.setFlat(True)
        self.equals.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.eight = QtWidgets.QPushButton(self.frame_2)
        self.eight.setGeometry(QtCore.QRect(224, 105, 64, 43))
        self.eight.setFont(font)
        self.eight.setObjectName("eight")
        self.eight.setText("8")
        self.eight.setFlat(True)
        self.eight.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pow = QtWidgets.QPushButton(self.frame_2)
        self.pow.setGeometry(QtCore.QRect(82, 43, 64, 43))
        self.pow.setFont(font)
        self.pow.setObjectName("pow")
        self.pow.setText("x^n")
        self.pow.setFlat(True)
        self.pow.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.seven = QtWidgets.QPushButton(self.frame_2)
        self.seven.setGeometry(QtCore.QRect(153, 105, 64, 43))
        self.seven.setFont(font)
        self.seven.setObjectName("seven")
        self.seven.setText("7")
        self.seven.setFlat(True)
        self.seven.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.four = QtWidgets.QPushButton(self.frame_2)
        self.four.setGeometry(QtCore.QRect(153, 167, 64, 43))
        self.four.setFont(font)
        self.four.setObjectName("four")
        self.four.setText("4")
        self.four.setFlat(True)
        self.four.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.one = QtWidgets.QPushButton(self.frame_2)
        self.one.setGeometry(QtCore.QRect(153, 229, 64, 43))
        self.one.setFont(font)
        self.one.setObjectName("one")
        self.one.setText("1")
        self.one.setFlat(True)
        self.one.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.three = QtWidgets.QPushButton(self.frame_2)
        self.three.setGeometry(QtCore.QRect(295, 229, 64, 43))
        self.three.setFont(font)
        self.three.setObjectName("three")
        self.three.setText("3")
        self.three.setFlat(True)
        self.three.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.plusminus = QtWidgets.QPushButton(self.frame_2)
        self.plusminus.setGeometry(QtCore.QRect(224, 43, 64, 42))
        self.plusminus.setFont(font)
        self.plusminus.setObjectName("plusminus")
        self.plusminus.setText("±")
        self.plusminus.setFlat(True)
        self.plusminus.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.xfact = QtWidgets.QPushButton(self.frame_2)
        self.xfact.setGeometry(QtCore.QRect(82, 291, 64, 43))
        self.xfact.setFont(font)
        self.xfact.setObjectName("xfact")
        self.xfact.setText("n!")
        self.xfact.setFlat(True)
        self.xfact.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        font.setPointSize(16)
        self.asin = QtWidgets.QPushButton(self.frame_2)
        self.asin.setGeometry(QtCore.QRect(11, 229, 64, 43))
        self.asin.setFont(font)
        self.asin.setObjectName("asin")
        self.asin.setText("asin")
        self.asin.setFlat(True)
        self.asin.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.cos = QtWidgets.QPushButton(self.frame_2)
        self.cos.setGeometry(QtCore.QRect(82, 167, 64, 43))
        self.cos.setFont(font)
        self.cos.setObjectName("cos")
        self.cos.setText("cos")
        self.cos.setFlat(True)
        self.cos.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.sin = QtWidgets.QPushButton(self.frame_2)
        self.sin.setGeometry(QtCore.QRect(82, 229, 64, 43))
        self.sin.setFont(font)
        self.sin.setObjectName("sin")
        self.sin.setText("sin")
        self.sin.setFlat(True)
        self.sin.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.acos = QtWidgets.QPushButton(self.frame_2)
        self.acos.setGeometry(QtCore.QRect(11, 167, 64, 43))
        self.acos.setFont(font)
        self.acos.setObjectName("acos")
        self.acos.setText("acos")
        self.acos.setFlat(True)
        self.acos.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        font.setPointSize(18)
        self.nrt = QtWidgets.QPushButton(self.frame_2)
        self.nrt.setGeometry(QtCore.QRect(82, 105, 64, 43))
        self.nrt.setFont(font)
        self.nrt.setObjectName("nrt")
        self.nrt.setText("y√x")
        self.nrt.setFlat(True)
        self.nrt.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.mul = QtWidgets.QPushButton(self.frame_2)
        self.mul.setGeometry(QtCore.QRect(366, 105, 64, 43))
        self.mul.setFont(font)
        self.mul.setObjectName("mul")
        self.mul.setText("×")
        self.mul.setFlat(True)
        self.mul.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.clear = QtWidgets.QPushButton(self.frame_2)
        self.clear.setGeometry(QtCore.QRect(153, 43, 64, 43))
        self.clear.setFont(font)
        self.clear.setObjectName("clear")
        self.clear.setText("C")
        self.clear.setFlat(True)
        self.clear.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.zero = QtWidgets.QPushButton(self.frame_2)
        self.zero.setGeometry(QtCore.QRect(153, 291, 64, 43))
        self.zero.setFont(font)
        self.zero.setObjectName("zero")
        self.zero.setText("0")
        self.zero.setFlat(True)
        self.zero.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pow_2 = QtWidgets.QPushButton(self.frame_2)
        self.pow_2.setGeometry(QtCore.QRect(11, 43, 64, 43))
        self.pow_2.setFont(font)
        self.pow_2.setObjectName("pow_2")
        self.pow_2.setText("x²")
        self.pow_2.setFlat(True)
        self.pow_2.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.add = QtWidgets.QPushButton(self.frame_2)
        self.add.setGeometry(QtCore.QRect(366, 229, 64, 43))
        self.add.setFont(font)
        self.add.setObjectName("add")
        self.add.setText("+")
        self.add.setFlat(True)
        self.add.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))

        # label frame setup
        self.frame_3 = QtWidgets.QFrame(self.frame)
        self.frame_3.setGeometry(QtCore.QRect(40, 30, 421, 211))
        self.frame_3.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_3.setObjectName("frame_3")

        # label setup
        font.setPointSize(18)
        self.label = QtWidgets.QLabel(self.frame_3)
        self.label.setGeometry(QtCore.QRect(15, 40, 381, 51))
        self.label.setFont(font)
        self.label.setStyleSheet("color: rgb(255, 255, 255);")
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.label.setText("0")
        self.label_2 = QtWidgets.QLabel(self.frame_3)
        self.label_2.setGeometry(QtCore.QRect(15, 110, 381, 71))
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

    ##
    # @brief Captures number and basic math operation keys and calls the corresponding events.
    # @param event Keyboard event that has been captured.
    #
    def keyPressEvent(self, event):
        key = event.key()

        if key == QtCore.Qt.Key_Shift or key == QtCore.Qt.Key_Control:
            return

        if 48 <= key <= 57:
            self.pressed_key = chr(key)
            self.print_number()
        elif key == 46 or key == 44:
            self.print_dot()
        elif key == 42:
            self.pressed_key = "×"
            self.set_two_operand_operation()
        elif key == 43 or key == 37:
            self.pressed_key = chr(key)
            self.set_two_operand_operation()
        elif key == 45:
            self.pressed_key = "−"
            self.set_two_operand_operation()
        elif key == 47:
            self.pressed_key = "÷"
            self.set_two_operand_operation()
        elif key == 67 or key == 99:
            self.clear_calc()
        elif key == QtCore.Qt.Key_Enter or key == QtCore.Qt.Key_Return:
            self.calculate_result()

    ##
    # @brief Sets the selected operation and its dependencies.
    # @param callback Function pointer to be set.
    # @param operand_count Number of parameters necessary for the given callback.
    # @param symbol Symbol(s) to print inside the label.
    #
    def set_operation(self, callback, operand_count, symbol):
        if (operand_count != 1 and len(self.label.text()) == 0)\
                or operand_count < 1 or operand_count > 2 or callback is None:
            return

        self.operation_callback = callback
        self.operand_count = operand_count

        # Use result (if correct and exists) in the operation label
        if self.result_set and "Error" not in self.label_2.text() and "nan" not in self.label_2.text():
            if operand_count == 1:
                self.label.setText(symbol + " " + self.label_2.text())
            else:
                self.label.setText(self.label_2.text() + " " + symbol + " ")
            return

        parsed_input = self.label.text().split(" ")
        parsed_input_length = len(parsed_input)

        if parsed_input_length == 1:
            if operand_count == 1:
                self.label.setText(symbol + " " + self.label.text())
            else:
                self.label.setText(self.label.text() + " " + symbol + " ")
        elif parsed_input_length == 2:
            if operand_count == 1:
                self.label.setText(symbol + " " + parsed_input[1])
            else:
                self.label.setText(parsed_input[1] + " " + symbol + " ")
        elif parsed_input_length == 3:
            if operand_count == 1:
                self.label.setText(symbol + " " + parsed_input[2])
            else:
                self.label.setText(parsed_input[0] + " " + symbol + " " + parsed_input[2])

    ##
    # @brief Processes operands and, if the operation and operand count are valid, generates a result.
    #
    def calculate_result(self):
        parsed_input = self.label.text().split(" ")

        # Do not do anything when the operation does not have enough operands supplied yet.
        if len(parsed_input) < self.operand_count + 1 or parsed_input[self.operand_count] == ""\
                or parsed_input[self.operand_count] == "-":
            return

        # Try to get the result. Also checks for library exceptions and (if possible) corrects the input.
        result = float("nan")
        try:
            if self.operand_count == 1:
                if self.operation_callback == fact:
                    abs_int_n = abs(int(float(parsed_input[1])))
                    self.label.setText(parsed_input[0] + " " + str(abs_int_n))
                    result = self.operation_callback(abs_int_n)

                elif self.operation_callback == asin or self.operation_callback == acos:
                    x = float(parsed_input[1])
                    if x < -1 or x > 1:
                        result = "Error: Undefined outside [-1, 1]!"
                    else:
                        result = self.operation_callback(x)
                else:
                    result = self.operation_callback(float(parsed_input[1]))

            elif self.operation_callback == pow:
                abs_int_exp = abs(int(float(parsed_input[2])))
                self.label.setText(parsed_input[0] + " " + parsed_input[1] + " " + str(abs_int_exp))
                result = self.operation_callback(float(parsed_input[0]), abs_int_exp)

            elif self.operation_callback == nrt:
                abs_int_n = abs(int(float(parsed_input[0])))
                if abs_int_n == 0 or parsed_input[2] == ".":
                    result = "Error: Undefined for exponent = 0!"
                float_x = float(parsed_input[2])
                if float_x < 0 and abs_int_n != 1 and abs_int_n % 2 == 0:
                    result = "Error: Undefined for real numbers!"
                else:
                    self.label.setText(str(abs_int_n) + " " + parsed_input[1] + " " + parsed_input[2])
                    result = self.operation_callback(float_x, abs_int_n)

            elif self.operation_callback == div:
                if float(parsed_input[2]) == 0.0:
                    result = "Error: Division by zero!"
                else:
                    result = self.operation_callback(float(parsed_input[0]), float(parsed_input[2]))

            elif self.operation_callback == mod:
                abs_dividend = abs(int(float(parsed_input[0])))
                abs_divisor = abs(int(float(parsed_input[2])))
                self.label.setText(str(abs_dividend) + " " + parsed_input[1] + " " + str(abs_divisor))
                if abs_divisor == 0:
                    result = "Error: Division by zero!"
                else:
                    result = self.operation_callback(abs_dividend, abs_divisor)

            elif self.operation_callback is None:
                result = float(parsed_input[0])

            else:
                result = self.operation_callback(float(parsed_input[0]), float(parsed_input[2]))
        except (ValueError, ZeroDivisionError):
            pass
        finally:
            result_string = str(result)
            self.label_2.setText(result_string)
            if "Error" not in result_string and result != float("nan"):
                self.result_set = True
            else:
                self.result_set = False

    ##
    # Sets operation with function pointer and symbol to print from self and operand count set to 1.
    #
    # @brief Sets operation requiring a single operand.
    #
    def set_single_operand_operation(self):
        text = self.sender().text()
        self.set_operation(self.operation_pointers[text], 1, text)

    ##
    # Sets operation with function pointer and symbol to print from self and operand count set to 2.
    #
    # @brief Sets operation requiring two operands.
    #
    def set_two_operand_operation(self):
        text = self.pressed_key
        if text is None:
            text = self.sender().text()
        else:
            self.pressed_key = None
        print(text)
        self.set_operation(self.operation_pointers[text], 2, text)

    ##
    # Sets operation with function pointer, symbol to print and operand count set for power function.
    #
    # @brief Sets power function.
    #
    def set_pow(self):
        self.set_operation(self.operation_pointers["^"], 2, "^")

    ##
    # Sets operation with function pointer, symbol to print and operand count set for power to 2 function.
    #
    # @brief Sets power to 2 function.
    #
    def set_pow_two(self):
        self.set_pow()
        parsed_input = self.label.text().split(" ")
        self.label.setText(parsed_input[0] + " " + parsed_input[1] + " 2")

    ##
    # Sets operation with function pointer, symbol to print and operand count set for root function.
    #
    # @brief Sets root function.
    #
    def set_nrt(self):
        self.set_operation(self.operation_pointers["√"], 2, "√")

    ##
    # Sets operation with function pointer, symbol to print and operand count set for square root function.
    #
    # @brief Sets square root function.
    #
    def set_nrt_two(self):
        self.set_nrt()
        parsed_input = self.label.text().split(" ")
        if parsed_input[2]:
            self.label.setText("2 " + parsed_input[1] + " " + parsed_input[2])
        else:
            self.label.setText("2 " + parsed_input[1] + " " + parsed_input[0])

    ##
    # @brief Swaps the sign of the currently written operand.
    #
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

    ##
    # @brief Prints number from self to current operand.
    #
    def print_number(self):
        number_string = self.pressed_key
        if number_string is None:
            number_string = self.sender().text()
        else:
            self.pressed_key = None

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

    ##
    # @brief Prints dot to current operand.
    #
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

    ##
    # @brief Prints Pi to current operand.
    #
    def print_pi(self):
        parsed_input = self.label.text().split(" ")
        parsed_input_length = len(parsed_input)

        if parsed_input_length == 1:
            self.label.setText("3.141592653589793")
        elif parsed_input_length == 2:
            self.label.setText(parsed_input[0] + " " + "3.141592653589793")
        elif parsed_input_length == 3:
            self.label.setText(parsed_input[0] + " " + parsed_input[1] + " " + "3.141592653589793")

    ##
    # @brief Resets operands to default values.
    #
    def clear_calc(self):
        self.label.setText("0")
        self.label_2.setText(" ")
        self.result_set = False


##
# @}
#


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = UiMainWindow()
    sys.exit(app.exec_())
