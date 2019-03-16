#!usr/bin/python
# -*- coding: utf-8 -*-

##
# @file math_lib.py
# @brief Mathematical library for fit-ivs-2 calculator.
# @author František Maštera <xmaste02.stud.fit.vutbr.cz>
#
# Project: fit-ivs-2
# Date created: 2019-03-05
# Last modified: 2019-03-16
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
def sin(x):
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
def asin(x):
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
def cos(x):
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
def acos(x):
    return PI/2 - asin(x)

