# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Users\42190\PycharmProjects\IVS_UI\IVS_UI.ui'
#
# ##
# @file gui_calc.py
# @brief Graphical user interface for calculator
# @author Nikolas Rada <xradan00.stud.fit.vutbr.cz>
#
# Project: fit-ivs-2
# Date created: 2019-03-17
# Last modified: 2019-03-24
#
#
# 

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
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
"QFrame{background-color: \"transparent\";}")
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
        self.textBrowser = QtWidgets.QTextBrowser(self.frame_3)
        self.textBrowser.setGeometry(QtCore.QRect(70, 110, 281, 91))
        self.textBrowser.setObjectName("textBrowser")
        self.label = QtWidgets.QLabel(self.frame_3)
        self.label.setGeometry(QtCore.QRect(80, 40, 261, 51))
        self.label.setText("")
        self.label.setObjectName("label")
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
        self.pow.clicked.connect(self.printpow)
        self.pow.clicked.connect(self.printpow)
        self.clear.clicked.connect(self.printclear)
        self.plusminus.clicked.connect(self.printplusminus)
        self.mod.clicked.connect(self.printmod)
        self.div.clicked.connect(self.printdiv)
        self.mul.clicked.connect(self.printmul)
        self.nrt.clicked.connect(self.printnrt)
        self.nrt.clicked.connect(self.printnrt)
        self.sin.clicked.connect(self.printsin)
        self.asin.clicked.connect(self.printasin)
        self.cos.clicked.connect(self.printcos)
        self.acos.clicked.connect(self.printacos)
        self.add.clicked.connect(self.printadd)
        self.sub.clicked.connect(self.printsub)
        self.dot.clicked.connect(self.printdot)
        self.equals.clicked.connect(self.printequals)
        self.pi.clicked.connect(self.printpi)
        self.xfact.clicked.connect(self.printxfact)

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

    def print0(self):
        #print("0") # UP line
        self.label.setText("0")
        
    def print1():
        x = 1
        self.label.setText("1") # UP line
        return x
        
    def print2(self):
        self.label.setText("2") # UP line
        y = 2
        return y
        
    def print3(self):
        self.label.setText("3") # UP line
        
    def print4(self):
        self.label.setText("4") # UP line
        
    def print5(self):
        self.label.setText("5") # UP line
        
    def print6(self):
       self.label.setText("6") # UP line
        
    def print7(self):
       self.label.setText("7") # UP line
        
    def print8(self):
        self.label.setText("8") # UP line
        
    def print9(self):
        self.label.setText("9") # UP line
        
            ##
    # @brief Nth root of a number.
    # @param x Number of which root is calculated.
    # @param n Exponent.
    # @return Nth root of given number.
    # @exception ValueError if n is lower than 0 and n isn't 1.
    # @exception ZeroDivisionError if n equals to 0.
    #
    def printnrt(x, n):
        self.label.setText("√") # UP line
        if x < 0 and n != 1:
            raise ValueError('This library doesn\'t support complex numbers.')
        try:
            return x ** (1 / n)
        except ZeroDivisionError:
            raise ValueError('Can\'t get 0th root of any number.')

            ##
    # @brief Power of a number.
    # @param x Number of which power is calculated.
    # @param exp Exponent.
    # @return Power of given number.
    # @exception ValueError if exp is not a natural number.
    #
    def printpow(x, exp):
        self.label.setText("^") # UP line
        if exp <= 0 or not isinstance(exp, int):
            raise ValueError('This function supports natural exponent only.')
        return x ** exp
        
    def printclear(self):
        print(" ") # UP line
        
    def printplusminus(self):
        self.label.setText("±") # UP line
          
            ##
    # @brief Modulo of 2 numbers.
    # @param x Dividend.
    # @param y Divisor.
    # @return The remainder after division of 1st and 2nd number.
    # @exception ZeroDivisionError if y (divisor) equals to 0.
    #
    def printmod(x, y):
        self.label.setText("%") # UP line
        try:
            return x % y
        except ZeroDivisionError as ex:
            raise ex
        
            ##
    # @brief Multiplication of 2 numbers.
    # @param x 1st number.
    # @param y 2nd number.
    # @return Product of 1st and 2nd number.
    #
    def printmul(x, y):
        self.label.setText("x") # UP line
        return x * y
        
            ##
    # @brief Division of 2 numbers.
    # @param x Dividend.
    # @param y Divisor.
    # @return Quotient of 1st and 2nd number.
    # @exception ZeroDivisionError if y (divisor) equals to zero.
    #
    def printdiv(x, y):
        self.label.setText("÷") # UP line
        try:
            return x / y
        except ZeroDivisionError as ex:
            raise ex

            ##
    # @brief Reduce number to (-2*PI, 2*PI) range by subtracting/adding 2*PI.
    # @param x Number to be reduced.
    # @return x within (-2*PI, 2*PI) range with the same sine/cosine value as original x.
    # Subtracts/adds 2*PI from/to the x value until it's within (-2*PI, 2*PI) range. Due to limited
    # PI accuracy, this means the x gets less accurate the higher/lower it is in the beggining.
    # This is neccessary because sin(x) and cos(x) with x values set too high or too low
    # cause OverflowError.
    #
    def reduce_rad(x):
        while x > 2*PI:
            x -= 2*PI
        while x < -2*PI:
            x += 2*PI
        return x

            ##
    # @brief Sine of a number using Taylor series.
    # @param n Number of which sine is calculated in radians.
    # @return Sine of given number.
    # @see https://en.wikipedia.org/wiki/Taylor_series#Trigonometric_functions
    # Values outisde (-2*PI, 2*PI) range will be increased/decreased by 2*PI until they will
    # get to that range. This shouldn't affect the result unless the x is ludicrously small/large.
    #
    def printsin(x):
        self.label.setText("sin") # UP line
        x = reduce_rad(x)

        # Store values between iterations to prevent calculating the same values over and over again.
        sinx = 0
        odd = 1
        facx = 1
        powx = x

        n = 0
        while True:

            # Calculate sine using Taylor series.
            prev_sinx = sinx
            sinx += odd * powx / facx
            diff = sinx - prev_sinx

            # If difference between result of this and last iteration is negligible, stop iterating.
            if -acc < diff < acc:
                break

            # Increment values used in formula for next iteration.
            n += 1
            odd *= -1
            facx *= (2 * n) * (2 * n + 1)
            powx *= x * x

        return sinx

            ##
    # @brief Arcsine of a number using Taylor series.
    # @param n Number of which arcsine is calculated.
    # @return Arcsine of given number in radians.
    # @exception ValueError if x is outide the (-1, 1) range.
    # @see https://en.wikipedia.org/wiki/Taylor_series#Trigonometric_functions
    # Values close to minimal/maximal allowed values (from +-0.999) will return set value
    # of PI/2. Calculation of precise result for these values takes long time to process.
    #
    def printasin(x):
        self.label.setText("sin-1") # UP line
        if x < -1 or x > 1:
            raise ValueError('Arcus sine isn\'t defined outside the <-1, 1> range.')
        if x >= 0.999:
            return PI / 2
        if x <= -0.999:
            return -PI / 2

        # Store values between iterations to prevent calculating the same values over and over again.
        asinx = 0
        fac_even = 1
        pow_facx = 1
        pow_even = x
        pow_4 = 1

        n = 0
        while True:

            # Calculate arcsine using Taylor series.
            prev_sinx = asinx
            asinx += (fac_even / (pow_4*pow_facx*((n << 1) + 1))) * pow_even
            diff = asinx - prev_sinx

            # If difference between result of this and last iteration is negligible, stop iterating.
            if -acc < diff < acc:
                break

            # Increment values used in formula for next iteration.
            n += 1
            fac_even *= (((n << 1) - 1) * (n << 1))
            pow_facx *= n * n
            pow_even *= x * x
            pow_4 <<= 2

        return asinx

            ##
    # @brief Cosine of a number using Taylor series.
    # @param n Number of which sine is calculated in radians.
    # @return Cosine of given number.
    # @see https://en.wikipedia.org/wiki/Taylor_series#Trigonometric_functions
    # Values outisde (-2*PI, 2*PI) range will be increased/decreased by 2*PI until they will
    # get to that range. This shouldn't affect the result unless the x is ludicrously small/large.
    #
    def printcos(x):
        self.label.setText("cos") # UP line
        x = reduce_rad(x)

        # Store values between iterations to prevent calculating the same values over and over again.
        cosx = 0
        odd = 1
        facx = 1
        powx = 1

        n = 0
        while True:

            # Calculate cosine using Taylor series.
            prev_sinx = cosx
            cosx += odd * powx / facx
            diff = cosx - prev_sinx

            # If difference between result of this and last iteration is negligible, stop iterating.
            if -acc < diff < acc:
                break

            # Increment values used in formula for next iteration.
            n += 1
            odd *= -1
            facx *= (2*n - 1) * (2*n)
            powx *= x * x

        return cosx

            ##
    # @brief Arccosine of a number using Taylor series.
    # @param n Number of which arccosine is calculated.
    # @return Arccosine of given number in radians.
    # @exception ValueError if x is outide the (-1, 1) range.
    # @see https://en.wikipedia.org/wiki/Taylor_series#Trigonometric_functions
    # Values close to minimal/maximal allowed values (from +-0.999) will return set values
    # of 0 and PI. Calculation of precise result for these values takes long time to process.
    #
    def printacos(x):
        self.label.setText("cos-1") # UP line
        return PI/2 - asin(x)
    
            ##
    # @brief Addition of 2 numbers.
    # @param x 1st number.
    # @param y 2nd number.
    # @return Sum of 1st and 2nd number.
    #
    def printadd(x, y):
        self.label.setText("+") # UP line
        return x + y

            ##
    # @brief Subtraction of 2 numbers.
    # @param x 1st number.
    # @param y 2nd number.
    # @return Difference of 1st and 2nd number.
    #
    def printsub(x, y):
        self.label.setText("-") # UP line
        return x - y
        
    def printdot(self):
        self.label.setText(".") # UP line
        
    def printequals(self):
        self.label.setText("=") # UP line
        
    def printpi(x):
        self.label.setText("π") # UP line
        x = 3.141_592_653_589_793

            ##
    # @brief Factorial of a number.
    # @param n Number of which factorial is calculated.
    # @return Factorial of given number.
    # @exception ValueError if n is not an integer or if it's lower than 0.
    #
    def printxfact(n):
        self.label.setText("x!") # UP line
        if n < 0 or not isinstance(n, int):
            raise ValueError('Can\'t get factorial from non-integer or number lower than zero.')
        factorial = 1
        for i in range(1, n+1):
            factorial *= i
        return factorial

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

