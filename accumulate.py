#!/usr/bin/env python2.7
# coding=utf-8

import sympy

x = sympy.symbols('x')


def f_1():
    return (1 + sympy.cos(x)) ** 2 / 2


def f_2():
    return ((2 * sympy.cos(x)) ** 2 - 1) / 2


y = sympy.integrate(f_2(), (x, sympy.pi / -3, sympy.pi / 3))
print y
print float(y)





