import numpy as np
from scipy.integrate import quad
from functools import partial
import matplotlib.pyplot as plt


def dN_dE(E, N0, gamma1, E0, Ec=-1, gamma2=1, pl=False ):
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
        x = np.linspace(lo, hi, 100)
        y = x * x * dN_dE(x, self.N0, self.gamma1, self.E0, self.Ec) * 1.6e-6
        plt.loglog(x, y)
        # plt.show()

    def __str__(self):
        return f""" 
                    Prefactor: {self.N0} +/- 
                    gamma1: {self.gamma1}
                    Cutoff: {self.Ec}
                    Scale: {self.E0}
                """
if __name__ == "__main__":

    j0218 = Star(1.7e-11, 1.8949, 735, 3766)
    j0218.set_err(0.062e-11, 0.04, 397)


    b1821 = Star(6e-12, 1.906, 895.187, 4501.92)
    b1821.set_err(0.35e-12, 0.067, 710)

    j1939 = Star(5.86176e-12 * 0.4, 2.37029, 1000, 4482.17)
    j1939.set_err(5.5e-13 * 0.4, 0.06, 1192.53)

    j1939 = Star(1.71e-12, 2.37, 1000)
    j1939.set_err(2.38e-13, 0.13)

    j1939 = Star(1.54e-12, 2.90, 1000, 9844)
    j1939.set_err(0.98e-12, 0.38, 2000)

    print(j1939.get_energy_flux())
    print(j1939.get_energy_err())
    print(j1939.get_photon_flux())
    print(j1939.get_photon_err())

# print(np.log(18409504/4410944) * 2)