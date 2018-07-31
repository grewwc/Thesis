import numpy as np
from scipy.integrate import quad
from functools import partial
import matplotlib.pyplot as plt


def dN_dE_old(E, N0, gamma1, E0, Ec=-1, gamma2=1, pl=False ):
    if not pl:
        return N0 * np.power(E/E0, -gamma1) * np.exp(-np.power(E/Ec, gamma2))
    else:
        return N0 * np.power(E/E0, -gamma1)


class Star:
    def __init__(self, N0, gamma1, E0, Ec=-1, gamma2=1):
        self.N0 = N0
        self.gamma1 = gamma1
        self.E0 = E0
        self.Ec, self.gamma2 = Ec, gamma2

    def set_err(self, N0, gamma1, Ec=-1):
        self.N0_err = N0
        self.gamma1_err = gamma1
        self.Ec_err = Ec

    def get_photon_flux(self, lo=100, hi=100000, pl=False):
        func = partial(dN_dE, N0=self.N0, gamma1=self.gamma1,
                       E0=self.E0, Ec=self.Ec, pl=pl)
        return quad(lambda E: func(E), lo, hi, points=[100, 1000])

    def get_photon_err(self, lo=100, hi=100000, pl=False):
        func = partial(dN_dE, N0=self.N0 + self.N0_err, gamma1=self.gamma1,
                       E0=self.E0, Ec=self.Ec, pl=pl)
        return quad(lambda E: func(E), lo, hi, points=[100, 1000])[0] \
            - self.get_photon_flux(lo, hi, pl)[0]

    def get_energy_flux(self, lo=100, hi=100000, pl=False):
        func = partial(dN_dE, N0=self.N0, gamma1=self.gamma1,
                       E0=self.E0, Ec=self.Ec, pl=pl)
        return quad(lambda E: func(E) * E * 1.6e-6, lo, hi, points=[100, 1000])

    def get_energy_err(self, lo=100, hi=100000, pl=False):
        func = partial(dN_dE, N0=self.N0_err + self.N0, gamma1=self.gamma1,
                       E0=self.E0, Ec=self.Ec, pl=pl)
        return quad(lambda E: func(E) * E * 1.6e-6, lo, hi, points=[100, 1000])[0] \
            - self.get_energy_flux(lo, hi, pl)[0]

    def plot_shape(self, lo=100, hi=100000):
        plt.ylim(1e-14, 1e-10)
        x = np.linspace(lo, hi, 5000)
        y = x * x * dN_dE_old(x, self.N0, self.gamma1, self.E0, self.Ec) * 1.6e-6
        plt.loglog(x, y)
        # plt.show()


def dN_dE(E, K, gamma, E0, a, b=0.666667):
    return K*np.power(E/E0, -gamma) * np.exp(-a * np.power(E, b))


class Star_new:
    def __init__(self, K, gamma, E0, a, b=0.666667):
        self.K = K 
        self.gamma = gamma 
        self.E0 = E0 
        self.a = a 
        self.b = b

    def set_err(self, K, gamma1, Ec=-1):
        self.K_err = K
        self.gamma1_err = gamma1

    def get_photon_flux(self, lo=100, hi=300000):
        func = partial(dN_dE, N0=self.K, gamma1=self.gamma,
                       E0=self.E0, a=self.a, b=self.b)
        return quad(lambda E: func(E), lo, hi, points=[100, 1000])

    def get_photon_err(self, lo=100, hi=300000):
        func = partial(dN_dE, N0=self.K + self.K_err, gamma1=self.gamma,
                       E0=self.E0, a=self.a, b=self.b)
        return quad(lambda E: func(E), lo, hi, points=[100, 1000])[0] \
            - self.get_photon_flux(lo, hi)[0]

    def get_energy_flux(self, lo=100, hi=300000):
        func = partial(dN_dE, N0=self.K, gamma1=self.gamma,
                       E0=self.E0, a=self.a)
        return quad(lambda E: func(E) * E * 1.6e-6, lo, hi, points=[100, 1000])

    def get_energy_err(self, lo=100, hi=300000):
        func = partial(dN_dE, N0=self.K_err + self.K, gamma1=self.gamma,
                       E0=self.E0, a=self.a, b= self.b)
        return quad(lambda E: func(E) * E * 1.6e-6, lo, hi, points=[100, 1000])[0] \
            - self.get_energy_flux(lo, hi)[0]

    def plot_shape(self, lo=100, hi=300000):
        plt.ylim(1e-14, 1e-10)
        x = np.linspace(lo, hi, 5000)
        y = x * x * dN_dE(x, self.K, self.gamma, self.E0, self.a, self.b) * 1.6e-6
        plt.loglog(x, y, label='new')
        plt.legend()

    def __str__(self):
        return f""" 
                    Prefactor: {self.K}
                    gamma1: {self.gamma}
                    Expfactor: {self.a}
                    Index2: {self.b}
                    Scale: {self.E0}
                """



j0218_new = Star_new(2.01e-11, 1.77, 821.475, 6.73e-3, 2./3)
j0218_new.set_err(1.9e-12, 0.07)

j0218 = Star(1.7e-11, 1.8949, 735, 3766)
j0218.set_err(0.062e-11, 0.04, 397)

j0218_new.plot_shape()
j0218.plot_shape()
plt.show()
