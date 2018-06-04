import matplotlib.pyplot as plt
from scipy.special import kv
from scipy.integrate import quad
import numpy as np
from functools import partial


def g(x):
    return kv(5/3, x)


def f(x):
    return x * quad(g, x, np.inf)[0]


def fx(x):
    return x**2 * quad(g, x, np.inf)[0]



x = np.linspace(1e-2, 10, 1000)

fig, (ax1, ax2) = plt.subplots(2, sharex=True)

def plot1():
    global ax1
    ax1.loglog()
    ax1.set(ylabel=
        r'$F\left(\frac{\nu}{\nu_c}\right)$')
    ax1.yaxis.label.set_size(17)

    ax1.set_ylim(2e-3, 1)
    ax1.plot(x, [f(xi) for xi in x])

def plot2():
    global ax2
    ax2.loglog()

    ax2.set_ylim(2e-3, 1)

    ax2.set(ylabel=
        r'$\left(\frac{\nu}{\nu_c}\right) F\left(\frac{\nu}{\nu_c}\right)$')
    ax2.yaxis.label.set_size(17)
    ax2.set(xlabel=r'$\nu/\nu_c$')
    ax2.xaxis.label.set_size(17)

    ax2.plot(x, [fx(xi) for xi in x])

plot1()
plot2()
plt.show()


