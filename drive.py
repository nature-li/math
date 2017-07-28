#!/usr/bin/env python2.7
# coding=utf-8

import math
import numpy as np
import matplotlib.pyplot as plt


def f_1(theta):
    r = 2 * math.cos(theta)
    return r


def f_2(theta):
    return 1


def __main__():
    plt.subplot(111, polar=True)

    theta_list = np.arange(0, 2 * np.pi, 0.02)
    radius_list = [f_1(theta) for theta in theta_list]
    plt.plot(theta_list, radius_list, lw=1)

    theta_list = np.arange(0, 2 * np.pi, 0.02)
    radius_list = [f_2(theta) for theta in theta_list]
    plt.plot(theta_list, radius_list, lw=1)

    plt.show()


if __name__ == '__main__':
    __main__()
