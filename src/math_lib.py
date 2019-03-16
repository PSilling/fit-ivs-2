#!usr/bin/python
# -*- coding: utf-8 -*-

##
# @file math_lib.py
# @brief Mathematical library for fit-ivs-2 calculator.
# @author František Maštera <xmaste02.stud.fit.vutbr.cz>
#
# Project: fit-ivs-2
# Date created: 2019-03-05
# Last modified: 2019-03-15
#

PI = 3.141_592_653_589_793

##
# @brief Decimal accuracy of methods using Taylor series.
#
acc = 1e-10


##
# @brief Addition of 2 numbers.
# @param x 1st number.
# @param y 2nd number.
# @return Sum of 1st and 2nd number.
#
def add(x, y):
    return x + y


##
# @brief Subtraction of 2 numbers.
# @param x 1st number.
# @param y 2nd number.
# @return Difference of 1st and 2nd number.
#
def sub(x, y):
    return x - y


##
# @brief Multiplication of 2 numbers.
# @param x 1st number.
# @param y 2nd number.
# @return Product of 1st and 2nd number.
#
def mul(x, y):
    return x * y


##
# @brief Division of 2 numbers.
# @param x Dividend.
# @param y Divisor.
# @return Quotient of 1st and 2nd number.
# @exception ZeroDivisionError if y (divisor) equals to zero.
#
def div(x, y):
    try:
        return x / y
    except ZeroDivisionError as ex:
        raise ex


##
# @brief Modulo of 2 numbers.
# @param x Dividend.
# @param y Divisor.
# @return The remainder after division of 1st and 2nd number.
# @exception ZeroDivisionError if y (divisor) equals to 0.
#
def mod(x, y):
    try:
        return x % y
    except ZeroDivisionError as ex:
        raise ex


##
# @brief Factorial of a number.
# @param n Number of which factorial is calculated.
# @return Factorial of given number.
# @exception ValueError if n is not an integer or if it's lower than 0.
#
def fact(n):
    if n < 0 or n % 1 != 0:
        raise ValueError('Can\'t get factorial from non-integer or number lower than zero.')
    factorial = 1
    for i in range(1, n+1):
        factorial *= i
    return factorial


##
# @brief Power of a number.
# @param x Number of which power is calculated.
# @param exp Exponent.
# @return Power of given number.
# @exception ValueError if x is not an integer and is lower than 0.
#
def pow(x, exp):
    if x < 0 and exp % 1 != 0:
        raise ValueError('This library doesn\'t support complex numbers.')
    return x ** exp


##
# @brief Nth root of a number.
# @param x Number of which root is calculated.
# @param n Exponent.
# @return Nth root of given number.
# @exception ValueError if n is lower than 0 and n isn't 1.
# @exception ZeroDivisionError if n equals to 0.
#
def nrt(x, n):
    if x < 0 and n != 1:
        raise ValueError('This library doesn\'t support complex numbers.')
    try:
        return x ** (1 / n)
    except ZeroDivisionError:
        raise ValueError('Can\'t get 0th root of any number.')


# TODO: rad reduction to <-2*PI; 2*PI> interval
def reduce_rad(x):
    return 0


# TODO: sin of x
def sin(x):
    return 0


# TODO: arcsin of x
def asin(x):
    return 0


# TODO: cos of x
def cos(x):
    return 0


# TODO: arccos of x
def acos(x):
    return 0
