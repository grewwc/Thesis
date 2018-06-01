import matplotlib.pyplot as plt

import numpy as np


class Star:
    def __init__(self, N0, gamma1, scale, cutoff, index2):
        self.N0 = N0
        self.gamma1 = gamma1
        self.scale = scale
        self.cutoff = cutoff
        self.index2 = index2

    def set_err(self, delta_n0, delta_gamma1, delta_cutoff):
        self.delta_N0 = delta_n0
        self.delta_gamma1 = delta_gamma1
        self.delta_cutoff = delta_cutoff


J0534_old = Star(4.92e-10, -1.9, 635.59, 4200, 1)
J0534_new = Star(5.73e-10, -2.07, 635.59, 9880.36, 1)
J0534_old.set_err(4.92e-10 * 5e-2, 0.1, 200)
J0534_new.set_err(0.036e-10, 0.011, 573)


def dN_dE(N0, gamma1, scale, cutoff, index2, E):
    return N0 * np.power(E/scale, gamma1) * np.exp(-E/cutoff)


def getRange_from_delta(x, deltax):
    return [x-deltax, x, x + deltax]


def func_range(func, E, star):
    temp_min = 1e10
    temp_max = -1
    res = []
    for _N0 in getRange_from_delta(star.N0, star.delta_N0):
        for _gamma1 in getRange_from_delta(star.gamma1, star.delta_gamma1):
            for _cutoff in getRange_from_delta(star.cutoff, star.delta_cutoff):
                temp = E * E * func(_N0, _gamma1, star.scale,
                                    _cutoff, 1, E) * 1.6e-6
                if temp < temp_min:
                    temp_min = temp
                elif temp > temp_max:
                    temp_max = temp
    res.append(temp_min)
    res.append(temp_max)
    return res


def fill_shade(func, Num, star, **kwargs):
    ymin = []
    ymax = []
    x = np.linspace(100, 1e5, Num)
    for Ei in x:
        temp = func_range(func, Ei, star)
        ymin.append(temp[0])
        ymax.append(temp[1])

    plt.fill_between(x, ymin, ymax, **kwargs)


def plot():
    plt.xlim(1e2, 3e5)
    plt.ylim(1e-15, 1e-9)

    data = np.loadtxt('/Users/grewwc/test_before.txt',
                      delimiter=' ').transpose()
    x1, y1 = data
    plt.loglog()

    plt.plot(x1, y1, c='b')
    x2, y2 = np.loadtxt('/Users/grewwc/test_now.txt',
                        delimiter=' ').transpose()
    plt.plot(x2, y2, c='r')

    fill_shade(dN_dE, 1000, J0534_old, facecolor='grey', alpha=0.4)
    fill_shade(dN_dE, 1000, J0534_new, facecolor='grey', alpha=0.4)

    plt.show()


def test_plot():
    plt.xlim(1e2, 3e5)
    plt.ylim(1e-15, 1e-9)
    data = np.loadtxt('/Users/grewwc/test_test.txt',
                      delimiter=' ').transpose()
    x1, y1 = data
    plt.loglog()
    plt.plot(x1, y1, c='b')
    plt.show()

plot()
