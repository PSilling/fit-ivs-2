#!usr/bin/python
# -*- coding: utf-8 -*-

##
# @file math_lib.py
# @brief Mathematical library for fit-ivs-2 calculator.
# @author František Maštera <xmaste02.stud.fit.vutbr.cz>
#
# * Project: fit-ivs-2
# * Date created: 2019-03-05
# * Last modified: 2019-03-16
#

##
# @brief Pi (3.14...) constant.
# @see https://en.wikipedia.org/wiki/Pi
#
PI = 3.141_592_653_589_793

##
# @brief Decimal accuracy of methods using Taylor series.
#
acc = 1e-10


##
# Subtracts/adds 2*PI from/to the x value until it's within (-2*PI, 2*PI) range. Due to limited
# PI accuracy, this means the x gets less accurate the higher/lower it is in the beginning.
# This is necessary because sin(x) and cos(x) with x values set too high or too low
# cause OverflowError.
#
# @brief Reduce number to (-2*PI, 2*PI) range by subtracting/adding 2*PI.
# @param x Number to be reduced.
# @return x within (-2*PI, 2*PI) range with the same sine/cosine value as original x.
#
def reduce_rad(x):
    while x > 2*PI:
        x -= 2*PI
    while x < -2*PI:
        x += 2*PI
    return x


##
# @defgroup functions Math operations
# @brief Mathematical operations included in the mathematical library.
# @{
#


##
# @brief Addition of 2 numbers.
# @param x 1st number.
# @param y 2nd number.
# @return Sum of 1st and 2nd number.
#
def add(x, y):
    return round(x + y, 10)


##
# @brief Subtraction of 2 numbers.
# @param x 1st number.
# @param y 2nd number.
# @return Difference of 1st and 2nd number.
#
def sub(x, y):
    return round(x - y, 10)


##
# @brief Multiplication of 2 numbers.
# @param x 1st number.
# @param y 2nd number.
# @return Product of 1st and 2nd number.
#
def mul(x, y):
    return round(x * y, 10)


##
# @brief Division of 2 numbers.
# @param x Dividend.
# @param y Divisor.
# @return Quotient of 1st and 2nd number.
# @exception ZeroDivisionError if y (divisor) equals to zero.
#
def div(x, y):
    try:
        return round(x / y, 10)
    except ZeroDivisionError as ex:
        raise ex


##
# @brief Modulo of 2 numbers.
# @param x Dividend.
# @param y Divisor.
# @return The remainder after division of 1st and 2nd number.
# @exception ZeroDivisionError if y (divisor) equals to 0.
# @exception ValueError if x or y aren't whole numbers.
#
def mod(x, y):
    if round(y, 0) == 0:
        raise ZeroDivisionError
    elif not isinstance(x, int) or not isinstance(y, int):
        raise ValueError('Modulo is defined for whole numbers only.');
    else:
        return round(x % y, 10)


##
# @brief Factorial of a number.
# @param n Number of which factorial is calculated.
# @return Factorial of given number.
# @exception ValueError if n is not an integer or if it's lower than 0.
#
def fact(n):
    if n < 0 or not isinstance(n, int):
        raise ValueError('Can\'t get factorial from non-integer or number lower than zero.')
    factorial = 1
    for i in range(1, n+1):
        factorial *= i
    return round(factorial, 10)


##
# @brief Power of a number.
# @param x Number of which power is calculated.
# @param exp Exponent.
# @return Power of given number.
# @exception ValueError if exp is not a natural number.
#
def pow(x, exp):
    if exp <= 0 or not isinstance(exp, int):
        raise ValueError('This function supports natural exponent only.')
    return round(x ** exp, 10)


##
# @brief Nth root of a number.
# @param x Number of which root is calculated.
# @param n Exponent.
# @return Nth root of given number.
# @exception ValueError if x is lower than 0 and n is even or float.
# @exception ZeroDivisionError if n equals to 0.
#
def nrt(x, n):
    try:
        if x >= 0:
            return round(x ** (1 / n), 10)
        if x < 0:
            if n % 2 == 0 or isinstance(n, float):
                raise ValueError('This library doesn\'t support complex numbers.')
            return round(-((-x) ** (1 / float(n))), 10)
    except ZeroDivisionError:
        raise ValueError('Can\'t get 0th root of any number.')


##
# Values outside (-2*PI, 2*PI) range will be increased/decreased by 2*PI until they will
# get to that range. This shouldn't affect the result unless the x is ludicrously small/large.
#
# @brief Sine of a number using Taylor series.
# @param x Number of which sine is calculated in radians.
# @return Sine of given number.
# @see https://en.wikipedia.org/wiki/Taylor_series#Trigonometric_functions
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
# Values close to minimal/maximal allowed values (from +-0.999) will return set value
# of PI/2. Calculation of precise result for these values takes long time to process.
#
# @brief Arcsine of a number using Taylor series.
# @param x Number of which arcsine is calculated.
# @return Arcsine of given number in radians.
# @exception ValueError if x is outside the (-1, 1) range.
# @see https://en.wikipedia.org/wiki/Taylor_series#Trigonometric_functions
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
# Values outside (-2*PI, 2*PI) range will be increased/decreased by 2*PI until they will
# get to that range. This shouldn't affect the result unless the x is ludicrously small/large.
#
# @brief Cosine of a number using Taylor series.
# @param x Number of which sine is calculated in radians.
# @return Cosine of given number.
# @see https://en.wikipedia.org/wiki/Taylor_series#Trigonometric_functions
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
# Values close to minimal/maximal allowed values (from +-0.999) will return set values
# of 0 and PI. Calculation of precise result for these values takes long time to process.
#
# @brief Arccosine of a number using Taylor series.
# @param x Number of which arccosine is calculated.
# @return Arccosine of given number in radians.
# @exception ValueError if x is outside the (-1, 1) range.
# @see https://en.wikipedia.org/wiki/Taylor_series#Trigonometric_functions
#
def acos(x):
    return PI/2 - asin(x)

##
# @}
#
