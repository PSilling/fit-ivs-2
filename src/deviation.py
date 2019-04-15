#!usr/bin/python
# -*- coding: utf-8 -*-

##
# @file deviation.py
# @brief Program for standard deviation calculation for profiling.
# @author Lukáš Schmelcer <xschme00.stud.fit.vutbr.cz>
#
# * Project: fit-ivs-2
#

from math_lib import *
from fileinput import input


##
# @defgroup deviation Standard deviation
# @brief Standard deviation calculation for calculator profiling.
# @{
#


##
# @brief Sums numbers from given list.
# @param val List of values to be summed.
# @return Total sum of numbers from given list.
#
def sum_numbers(val):
    sum_loc = 0
    for n in val:
        sum_loc = add(sum_loc, n)
    return sum_loc


##
# @brief Calculates arithmetic mean value.
# @param calc_sum Summary of numbers to calculate mean from.
# @param leng Amount of numbers to calculate mean from.
# @return Arithmetic mean of given summary of given amount of numbers.
#
def mean(calc_sum, leng):
    return mul(div(calc_sum, leng), 1.0)


##
# @brief Calculates standard deviation from list of numbers.
# @param leng Amount of numbers in the list.
# @param val List of values for standard deviation calculation.
# @return Standard deviation of numbers from given list.
#
def deviation(leng, val):
    org_sum = sum_numbers(val)
    calc_mean = mean(org_sum, leng)
    updt_sum = 0
    for n in val:
        updt_sum = add(updt_sum, pow(sub(n, calc_mean), 2))
    updt_sum = mul(updt_sum, div(1, sub(leng, 1)))
    return nrt(updt_sum, 2)


##
# @brief Loads numbers from standard input and prints their standard deviation.
# @param numbers List of numbers.
#
def main(numbers):
    values = list()
    for line in numbers:
        values.append(float(line))
    print(deviation(len(values), values))


main(input())


##
# @}
#
