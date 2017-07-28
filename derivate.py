#!/usr/bin/env python2.7
# coding=utf-8

import numpy
import math
import sympy


def f_1(x):
    return (1 + math.cos(x)) ** 2 / 2


def f(x):
    return ((2 * numpy.cos(x)) ** 2 - 1) / 2


def func(a, b, n):
    d = (b - a) * 1.0 / n

    s = 0
    for k in xrange(1, n + 1):
        s += f(a + k * d) * (b - a) / n
    print s


func(numpy.pi / -3, numpy.pi / 3, 100000)
