#!usr/bin/python
# -*- coding: utf-8 -*-

# Project: fit-ivs-2
# File: math_lib_test.py
# Author: Petr Šilling <xsilli01.stud.fit.vutbr.cz>
# Date created: 2019-03-09
# Last modified: 2019-03-10

from unittest import TestCase
from .math_lib import *

# This file contains math_lib.py function tests.
# Test names are based on the tested criteria and also correspond to
# appropriate functions inside math_lib.py. Tested values, and more
# importantly exceptions, are mostly conforming to the standard Python
# math library. Differences: complex numbers (e.g. in pow) raise ValueErrors;
# power raises ValueError without natural exponent.
#
# Tests can be run from your IDE or using the following command in the project
# root directory: python3 -m unittest src/math_lib_test.py


class TestAdd(TestCase):

    def test_add_near_zero(self):
        self.assertEqual(0, add(0, 0))
        self.assertEqual(1, add(1, 0))
        self.assertEqual(-1, add(0, -1))
        self.assertEqual(3, add(1, 2))
        self.assertEqual(-1, add(-2, 1))
        self.assertEqual(0, add(3, -3))

    def test_add_above_zero(self):
        self.assertEqual(14, add(6, 8))
        self.assertEqual(199, add(100, 99))
        self.assertEqual(1_283, add(770, 513))
        self.assertEqual(4_239, add(3_128, 1_111))
        self.assertEqual(10_053_625, add(8_679_013, 1_374_612))

    def test_add_below_zero(self):
        self.assertEqual(-15, add(-8, -7))
        self.assertEqual(-442, add(-430, -12))
        self.assertEqual(-2_646, add(-133, -2_513))
        self.assertEqual(-5_529, add(-4_528, -1_001))
        self.assertEqual(-10_053_623, add(-1_374_611, -8_679_012))

    def test_add_with_one_float(self):
        self.assertAlmostEqual(2.42, add(0, 2.42))
        self.assertAlmostEqual(-1.2, add(-1.2, 0))
        self.assertAlmostEqual(58.7, add(4.7, 54))
        self.assertAlmostEqual(-409.8, add(45, -454.8))
        self.assertAlmostEqual(587.3, add(432.3, 155))
        self.assertAlmostEqual(-861.0, add(-532.6, -328.4))
        self.assertAlmostEqual(4_100.6, add(-212.4, 4_313))

    def test_add_with_two_floats(self):
        self.assertAlmostEqual(1.81, add(0.41, 1.4))
        self.assertAlmostEqual(-2.3, add(-0.2, -2.1))
        self.assertAlmostEqual(86.0, add(80.6, 5.4))
        self.assertAlmostEqual(-57.1, add(-19.4, -37.7))
        self.assertAlmostEqual(1_021.6, add(875.9, 145.7))
        self.assertAlmostEqual(-958.5, add(-422.8, -535.7))
        self.assertAlmostEqual(680.4, add(3_112.9, -2_432.5))


class TestSub(TestCase):

    def test_sub_near_zero(self):
        self.assertEqual(0, sub(0, 0))
        self.assertEqual(1, sub(1, 0))
        self.assertEqual(1, sub(0, -1))
        self.assertEqual(-1, sub(1, 2))
        self.assertEqual(-3, sub(-2, 1))
        self.assertEqual(6, sub(3, -3))
        self.assertEqual(0, sub(3, 3))

    def test_sub_above_zero(self):
        self.assertEqual(0, sub(7, 7))
        self.assertEqual(13, sub(113, 100))
        self.assertEqual(436, sub(2_434, 1_998))
        self.assertEqual(-3_946, sub(5_823, 9_769))
        self.assertEqual(3_333_800, sub(7_979_413, 4_645_613))

    def test_sub_below_zero(self):
        self.assertEqual(0, sub(-3, -3))
        self.assertEqual(430, sub(-460, -890))
        self.assertEqual(-1_209, sub(-2_862, -1_653))
        self.assertEqual(3_563, sub(-5_528, -9_091))
        self.assertEqual(-70_376_399, sub(-76_374_612, -5_998_213))

    def test_sub_with_one_float(self):
        self.assertAlmostEqual(-3.44, sub(0, 3.44))
        self.assertAlmostEqual(-6.7, sub(-6.7, 0))
        self.assertAlmostEqual(-27.3, sub(4.7, 32))
        self.assertAlmostEqual(1_645.8, sub(991, -654.8))
        self.assertAlmostEqual(-322.1, sub(432.9, 755))
        self.assertAlmostEqual(312.7, sub(-412, -724.7))
        self.assertAlmostEqual(-6_155.5, sub(-1_542.5, 4_613))

    def test_sub_with_two_floats(self):
        self.assertAlmostEqual(-2.0, sub(2.4, 4.4))
        self.assertAlmostEqual(-0.7, sub(-4.2, -3.5))
        self.assertAlmostEqual(33.1, sub(84.6, 51.5))
        self.assertAlmostEqual(30.5, sub(-49.4, -79.9))
        self.assertAlmostEqual(652.8, sub(-132.9, -785.7))
        self.assertAlmostEqual(-223.9, sub(731.4, 955.3))
        self.assertAlmostEqual(8_635.6, sub(3_253.1, -5_382.5))


class TestMul(TestCase):

    def test_mul_near_zero(self):
        self.assertEqual(0, mul(0, 0))
        self.assertEqual(0, mul(1, 0))
        self.assertEqual(0, mul(0, -1))
        self.assertEqual(2, mul(1, 2))
        self.assertEqual(-2, mul(-2, 1))
        self.assertEqual(-15, mul(5, -3))
        self.assertEqual(15, mul(5, 3))

    def test_mul_above_zero(self):
        self.assertEqual(7, mul(1, 7))
        self.assertEqual(1300, mul(13, 100))
        self.assertEqual(4_368, mul(24, 182))
        self.assertEqual(206_397, mul(213, 969))
        self.assertEqual(4_117_329, mul(933, 4_413))

    def test_mul_below_zero(self):
        self.assertEqual(-4, mul(4, -1))
        self.assertEqual(720, mul(-40, -18))
        self.assertEqual(3_366, mul(-22, -153))
        self.assertEqual(55_738, mul(-58, -961))
        self.assertEqual(6_977_956, mul(-4_612, -1_513))

    def test_mul_with_one_float(self):
        self.assertAlmostEqual(0, mul(0, 4.445))
        self.assertAlmostEqual(0, mul(-5.47, 0))
        self.assertAlmostEqual(170.2, mul(7.4, 23))
        self.assertAlmostEqual(-1_545.6, mul(-322, 4.8))
        self.assertAlmostEqual(7_097, mul(94, 75.5))
        self.assertAlmostEqual(68_126.4, mul(-912, -74.7))
        self.assertAlmostEqual(-2_641_837.1, mul(-952.7, 2_773))

    def test_mul_with_two_floats(self):
        self.assertAlmostEqual(1.16, mul(5.8, 0.2))
        self.assertAlmostEqual(38.25, mul(-4.5, -8.5))
        self.assertAlmostEqual(-1_747.3, mul(34.6, -50.5))
        self.assertAlmostEqual(12_926.76, mul(-92.4, -139.9))
        self.assertAlmostEqual(-312_447.76, mul(-421.6, 741.1))
        self.assertAlmostEqual(70_581.28, mul(741.4, 95.2))
        self.assertAlmostEqual(-7_129_005.84, mul(6_410.4, -1_112.1))


class TestDiv(TestCase):

    def test_div_by_zero(self):
        self.assertRaises(ZeroDivisionError, div, 0, 0)
        self.assertRaises(ZeroDivisionError, div, -421, 0)
        self.assertRaises(ZeroDivisionError, div, 234, 0)
        self.assertRaises(ZeroDivisionError, div, -4.1, 0)
        self.assertRaises(ZeroDivisionError, div, 2.4, 0)

    def test_div_near_zero(self):
        self.assertEqual(0, div(0, 1))
        self.assertEqual(0, div(0, -1))
        self.assertEqual(-1, div(1, -1))
        self.assertEqual(-2, div(-4, 2))
        self.assertEqual(2, div(6, 3))
        self.assertEqual(2, div(-6, -3))

    def test_div_above_zero(self):
        self.assertEqual(4, div(4, 1))
        self.assertEqual(10, div(140, 14))
        self.assertEqual(21, div(2_520, 120))
        self.assertEqual(87, div(83_259, 957))
        self.assertEqual(875, div(3_999_625, 4_571))

    def test_div_below_zero(self):
        self.assertEqual(-5, div(5, -1))
        self.assertEqual(10, div(-50, -5))
        self.assertEqual(13, div(-3_250, -250))
        self.assertEqual(75, div(-70_650, -942))
        self.assertEqual(1_254, div(-12_227_754, -9_751))

    def test_div_with_one_float(self):
        self.assertAlmostEqual(0, div(0, 3.95))
        self.assertAlmostEqual(5, div(44, 8.8))
        self.assertAlmostEqual(-7.2, div(-410.4, 57))
        self.assertAlmostEqual(8.9, div(863.3, 97))
        self.assertAlmostEqual(54.8, div(-24_879.2, -454))
        self.assertAlmostEqual(841.8, div(624_615.6, 742))

    def test_div_with_two_floats(self):
        self.assertAlmostEqual(5, div(5.5, 1.1))
        self.assertAlmostEqual(59, div(-88.5, -1.5))
        self.assertAlmostEqual(-6, div(36.6, -6.1))
        self.assertAlmostEqual(2, div(-432.4, -216.2))
        self.assertAlmostEqual(-475.1, div(-415_855.03, 875.3))
        self.assertAlmostEqual(742.1, div(94_617.75, 127.5))
        self.assertAlmostEqual(-987.6, div(7_746_438.12, -7_843.7))


class TestMod(TestCase):

    def test_mod_by_zero(self):
        self.assertRaises(ZeroDivisionError, mod, 0, 0)
        self.assertRaises(ZeroDivisionError, mod, -411, 0)
        self.assertRaises(ZeroDivisionError, mod, 334, 0)
        self.assertRaises(ZeroDivisionError, mod, -7.1, 0)
        self.assertRaises(ZeroDivisionError, mod, 8.4, 0)

    def test_mod_near_zero(self):
        self.assertEqual(0, mod(0, 1))
        self.assertEqual(0, mod(0, -1))
        self.assertEqual(0, mod(1, -1))
        self.assertEqual(1, mod(-5, 2))
        self.assertEqual(2, mod(5, 3))
        self.assertEqual(-2, mod(-5, -3))

    def test_mod_above_zero(self):
        self.assertEqual(0, mod(3, 1))
        self.assertEqual(15, mod(143, 32))
        self.assertEqual(160, mod(1_420, 180))
        self.assertEqual(120, mod(99_319, 437))
        self.assertEqual(2860, mod(64_542_763, 5_871))

    def test_mod_below_zero(self):
        self.assertEqual(0, mod(2, -1))
        self.assertEqual(-10, mod(-50, -20))
        self.assertEqual(-32, mod(-6_152, -102))
        self.assertEqual(-41, mod(-64_241, -428))
        self.assertEqual(-990, mod(-98_322_554, -6_751))

    def test_mod_with_one_float(self):
        self.assertAlmostEqual(0, mod(0, 1.99))
        self.assertAlmostEqual(2.2, mod(22, 19.8))
        self.assertAlmostEqual(32.4, mod(-231.6, 33))
        self.assertAlmostEqual(56.3, mod(973.3, 131))
        self.assertAlmostEqual(-455, mod(-55_419, -785.2))
        self.assertAlmostEqual(516.7, mod(682_799.7, 3_361))

    def test_mod_with_two_floats(self):
        self.assertAlmostEqual(0, mod(4.66, 2.33))
        self.assertAlmostEqual(-11, mod(-48.5, -12.5))
        self.assertAlmostEqual(-5, mod(56.6, -7.7))
        self.assertAlmostEqual(-56.1, mod(-434.4, -126.1))
        self.assertAlmostEqual(108.2, mod(-5_598.9, 815.3))
        self.assertAlmostEqual(379.7, mod(97_117.2, 887.5))
        self.assertAlmostEqual(-4_619.4, mod(53_712_428.6, -7_911.2))


class TestFact(TestCase):

    def test_fact_below_zero(self):
        self.assertRaises(ValueError, fact, -1)
        self.assertRaises(ValueError, fact, -0.1)

    def test_fact_of_zero(self):
        self.assertEqual(1, fact(0))

    def test_fact_above_zero(self):
        self.assertEqual(1, fact(1))
        self.assertEqual(2, fact(2))
        self.assertEqual(6, fact(3))
        self.assertEqual(24, fact(4))
        self.assertEqual(40_320, fact(8))
        self.assertEqual(20_922_789_888_000, fact(16))

    def test_fact_with_float(self):
        self.assertRaises(ValueError, fact, -3.5)
        self.assertRaises(ValueError, fact, -0.11)
        self.assertRaises(ValueError, fact, 3.5)
        self.assertRaises(ValueError, fact, 0.11)


class TestPow(TestCase):

    def test_pow_raised_to_not_natural(self):
        self.assertRaises(ValueError, pow, 3, 0)
        self.assertRaises(ValueError, pow, -2, 0)
        self.assertRaises(ValueError, pow, 4, -1)
        self.assertRaises(ValueError, pow, -5, -5)

        self.assertRaises(ValueError, pow, -0.3, 1.6)
        self.assertRaises(ValueError, pow, -3.1, -2.4)
        self.assertRaises(ValueError, pow, 1.3, 2.6)
        self.assertRaises(ValueError, pow, 0.55, 1.4)
        self.assertRaises(ValueError, pow, -2, 1.1)
        self.assertRaises(ValueError, pow, -5, -2.4)
        self.assertRaises(ValueError, pow, 1, 0.1)
        self.assertRaises(ValueError, pow, 7, -4.3)

    def test_pow_near_zero(self):
        self.assertEqual(0, pow(0, 2))
        self.assertEqual(2, pow(2, 1))
        self.assertEqual(-3, pow(-3, 1))
        self.assertEqual(1, pow(1, 3))
        self.assertEqual(16, pow(-4, 2))

    def test_pow_above_zero(self):
        self.assertEqual(2, pow(2, 1))
        self.assertEqual(27, pow(3, 3))
        self.assertEqual(196, pow(14, 2))
        self.assertEqual(160_000, pow(20, 4))
        self.assertEqual(62_748_517, pow(13, 7))

    def test_pow_with_float_x(self):
        self.assertAlmostEqual(0.01, pow(0.1, 2))
        self.assertAlmostEqual(3.375, pow(1.5, 3))
        self.assertAlmostEqual(45.6976, pow(-2.6, 4))
        self.assertAlmostEqual(-335.544_32, pow(-3.2, 5))
        self.assertAlmostEqual(1_008.062_5, pow(-31.75, 2))
        self.assertAlmostEqual(2_924.207, pow(14.3, 3))


class TestNrt(TestCase):

    def test_nrt_with_n_set_as_zero(self):
        self.assertRaises(ValueError, nrt, -0.2, 0)
        self.assertRaises(ValueError, nrt, 0.7, 0)
        self.assertRaises(ValueError, nrt, -4, 0)
        self.assertRaises(ValueError, nrt, 7, 0)

    def test_nrt_of_negative_number(self):
        self.assertRaises(ValueError, nrt, -0.1, 2)
        self.assertRaises(ValueError, nrt, -0.9, -3.1)
        self.assertRaises(ValueError, nrt, -8, 6)
        self.assertRaises(ValueError, nrt, -1, -9.2)

    def test_nrt_of_zero_with_negative_n(self):
        self.assertRaises(ValueError, nrt, 0, -5)
        self.assertRaises(ValueError, nrt, 0, -0.3)

    def test_nrt_near_zero(self):
        self.assertEqual(0, nrt(0, 2))
        self.assertEqual(2, nrt(2, 1))
        self.assertEqual(-3, nrt(-3, 1))
        self.assertEqual(1, nrt(1, 3))
        self.assertEqual(2, nrt(4, 2))

    def test_nrt_above_zero(self):
        self.assertEqual(3, nrt(27, 3))
        self.assertEqual(2, nrt(256, 8))
        self.assertAlmostEqual(2.734_068_828, nrt(1_142, 7))
        self.assertAlmostEqual(6.831_111_827, nrt(14_875, 5))
        self.assertAlmostEqual(2.482_165_277, nrt(5_153_732, 17))

    def test_nrt_with_one_float(self):
        self.assertAlmostEqual(0, nrt(0, 3.1))
        self.assertAlmostEqual(0.516_778_892, nrt(4, -2.1))
        self.assertAlmostEqual(3.507_434_699, nrt(413, 4.8))
        self.assertAlmostEqual(3.443_924_488, nrt(98_764, 9.3))

    def test_nrt_with_two_floats(self):
        self.assertAlmostEqual(1.071_482_526, nrt(1.3, 3.8))
        self.assertAlmostEqual(0.724_204_297, nrt(3.3, -3.7))
        self.assertAlmostEqual(1.604_823_081, nrt(514.8, 13.2))
        self.assertAlmostEqual(0.319_560_103, nrt(45_415.7, -9.4))


class TestSin(TestCase):

    def test_sin_commonly_known_values(self):
        self.assertEqual(0, sin(0))
        self.assertAlmostEqual(0.5, sin(PI / 6))
        self.assertAlmostEqual(0.707_106_781, sin(PI / 4))
        self.assertAlmostEqual(0.866_025_404, sin(PI / 3))
        self.assertAlmostEqual(1, sin(PI / 2))

        self.assertAlmostEqual(0.5, sin((5 * PI) / 6))
        self.assertAlmostEqual(0.707_106_781, sin((3 * PI) / 4))
        self.assertAlmostEqual(0.866_0254_04, sin((2 * PI) / 3))
        self.assertAlmostEqual(0, sin(PI))

        self.assertAlmostEqual(-0.5, sin((7 * PI) / 6))
        self.assertAlmostEqual(-0.707_106_781, sin((5 * PI) / 4))
        self.assertAlmostEqual(-0.866_025_404, sin((4 * PI) / 3))
        self.assertAlmostEqual(-1, sin((3 * PI) / 2))

        self.assertAlmostEqual(-0.5, sin((11 * PI) / 6))
        self.assertAlmostEqual(-0.707_106_781, sin((7 * PI) / 4))
        self.assertAlmostEqual(-0.866_025_404, sin((5 * PI) / 3))
        self.assertAlmostEqual(0, sin(2 * PI))

    def test_sin_above_zero(self):
        self.assertAlmostEqual(0.909_297_427, sin(2))
        self.assertAlmostEqual(-0.879_695_760, sin(10.5))
        self.assertAlmostEqual(0.683_909_954, sin(132.7))
        self.assertAlmostEqual(-0.889_940_618, sin(1_532))

    def test_sin_below_zero(self):
        self.assertAlmostEqual(0.958_924_275, sin(-5))
        self.assertAlmostEqual(-0.777_794_162, sin(-21.1))
        self.assertAlmostEqual(0.962_850_154, sin(-243.2))
        self.assertAlmostEqual(-0.919_896_053, sin(-3_841))


class TestAsin(TestCase):

    def test_asin_x_not_defined(self):
        self.assertRaises(ValueError, asin, 3)
        self.assertRaises(ValueError, asin, -42)
        self.assertRaises(ValueError, asin, 1.01)
        self.assertRaises(ValueError, asin, -1.001)

    def test_asin_commonly_known_values(self):
        self.assertEqual(0, asin(0))
        self.assertAlmostEqual(PI / 6, asin(0.5))
        self.assertAlmostEqual(PI / 4, asin(0.707_106_781))
        self.assertAlmostEqual(PI / 3, asin(0.866_025_404))
        self.assertAlmostEqual(PI / 2, asin(1))

        self.assertAlmostEqual(-PI / 6, asin(-0.5))
        self.assertAlmostEqual(-PI / 4, asin(-0.707_106_781))
        self.assertAlmostEqual(-PI / 3, asin(-0.866_025_404))
        self.assertAlmostEqual(-PI / 2, asin(-1))

    def test_asin_above_zero(self):
        self.assertAlmostEqual(0.170_829_669, asin(0.17))
        self.assertAlmostEqual(0.283_794_109, asin(0.28))
        self.assertAlmostEqual(0.546_850_951, asin(0.52))
        self.assertAlmostEqual(1.055_202_321, asin(0.87))

    def test_asin_below_zero(self):
        self.assertAlmostEqual(-0.110_223_050, asin(-0.11))
        self.assertAlmostEqual(-0.357_571_104, asin(-0.35))
        self.assertAlmostEqual(-0.500_654_712, asin(-0.48))
        self.assertAlmostEqual(-1.287_002_218, asin(-0.96))


class TestCos(TestCase):

    def test_cos_commonly_known_values(self):
        self.assertAlmostEqual(1, cos(0))
        self.assertAlmostEqual(0.866_025_404, cos(PI / 6))
        self.assertAlmostEqual(0.707_106_781, cos(PI / 4))
        self.assertAlmostEqual(0.5, cos(PI / 3))
        self.assertAlmostEqual(0, cos(PI / 2))

        self.assertAlmostEqual(-0.5, cos((2 * PI) / 3))
        self.assertAlmostEqual(-0.707_106_781, cos((3 * PI) / 4))
        self.assertAlmostEqual(-0.866_0254_04, cos((5 * PI) / 6))
        self.assertAlmostEqual(-1, cos(PI))

        self.assertAlmostEqual(-0.5, cos((4 * PI) / 3))
        self.assertAlmostEqual(-0.707_106_781, cos((5 * PI) / 4))
        self.assertAlmostEqual(-0.866_025_404, cos((7 * PI) / 6))
        self.assertAlmostEqual(0, cos((3 * PI) / 2))

        self.assertAlmostEqual(0.5, cos((5 * PI) / 3))
        self.assertAlmostEqual(0.707_106_781, cos((7 * PI) / 4))
        self.assertAlmostEqual(0.866_025_404, cos((11 * PI) / 6))
        self.assertAlmostEqual(1, cos(2 * PI))

    def test_cos_above_zero(self):
        self.assertAlmostEqual(-0.653_643_621, cos(4))
        self.assertAlmostEqual(0.986_192_302, cos(12.4))
        self.assertAlmostEqual(-0.964_035_833, cos(254.2))
        self.assertAlmostEqual(0.547_905_791, cos(2_506))

    def test_cos_below_zero(self):
        self.assertAlmostEqual(-0.416_146_837, cos(-2))
        self.assertAlmostEqual(0.252_119_408, cos(-30.1))
        self.assertAlmostEqual(-0.069_821_171, cos(-394.2))
        self.assertAlmostEqual(0.308_091_888, cos(-1_031.7))


class TestAcos(TestCase):

    def test_acos_x_not_defined(self):
        self.assertRaises(ValueError, acos, 2)
        self.assertRaises(ValueError, acos, -31)
        self.assertRaises(ValueError, acos, 1.001)
        self.assertRaises(ValueError, acos, 1.01)

    def test_acos_commonly_known_values(self):
        self.assertAlmostEqual(0, acos(1))
        self.assertAlmostEqual(PI / 6, acos(0.866_025_404))
        self.assertAlmostEqual(PI / 4, acos(0.707_106_781))
        self.assertAlmostEqual(PI / 3, acos(0.5))
        self.assertAlmostEqual(PI / 2, acos(0))

        self.assertAlmostEqual((PI * 2) / 3, acos(-0.5))
        self.assertAlmostEqual((PI * 3) / 4, acos(-0.707_106_781))
        self.assertAlmostEqual((PI * 5) / 6, acos(-0.866_025_404))
        self.assertAlmostEqual(PI, acos(-1))

    def test_acos_above_zero(self):
        self.assertAlmostEqual(1.450_506_444, acos(0.12))
        self.assertAlmostEqual(1.223_879_429, acos(0.34))
        self.assertAlmostEqual(0.976_410_527, acos(0.56))
        self.assertAlmostEqual(0.427_512_265, acos(0.91))

    def test_acos_below_zero(self):
        self.assertAlmostEqual(1.670_963_748, acos(-0.10))
        self.assertAlmostEqual(1.813_162_178, acos(-0.24))
        self.assertAlmostEqual(2.252_349_538, acos(-0.63))
        self.assertAlmostEqual(2.668_141_496, acos(-0.89))
