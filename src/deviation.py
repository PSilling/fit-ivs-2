from math_lib import *
from fileinput import input


def sum_numbers(val):
    sum_loc = 0
    for n in val:
        sum_loc = add(sum_loc, n)
    return sum_loc


def mean(calc_sum, leng):
    return mul(div(calc_sum, leng), 1.0)


def deviation(leng, val):
    org_sum = sum_numbers(val)
    calc_mean = mean(org_sum, leng)
    updt_sum = 0
    for n in val:
        updt_sum = add(updt_sum, pow(sub(n, calc_mean), 2))
    updt_sum = mul(updt_sum, div(1, sub(leng, 1)))
    return nrt(updt_sum, 2)


def main(numbers):
    values = list()
    for line in numbers:
        values.append(float(line))
    print(deviation(len(values), values))


main(input())
