import numpy as np

from scipy.optimize import fsolve

import tqdm as tqdm
import warnings

import csv
import json

import matplotlib.pyplot as plt

# Constants and params
PI = np.pi

omega = 0.057 # Agnualar frequency of the laser
E_0 = 0.0534 # Maximum amplutude of laser
I_p = 0.5 # Ionisation potential
U_p = E_0**2 / (4*omega**2) # Ponderomotive energy
t_cyc = 2*PI / omega # Period of laser

def A(t: complex)->complex:
    """Vector potential representing the laser field.

    :param t: Ionisation time which is a combination of
        imaginary tunnelling time and real propogation time.
    :return: Mathematical expression of A.
    """
    return (E_0/omega) * np.cos(omega*t)
    
def saddle(x: list[float], p: float, I_p_eff: float)->list[float]:
    """Scipy fsolve needs real valued functions so the complex
    equation is split into real and imaginary parts.

    :param I_p_eff: Effective ionisation potential that takes
        into account for the perpendicular momenta.  
    :param x: List of real time and imaginary time components.
    :param p: The perpendicular momentum.
    :return: The 1D saddlepoint equation split into real and
        imaginary components.
    """
    t_s = x[0] + 1j * x[1]
    R = 0.5 * (p + A(t_s))**2 + I_p_eff

    return [R.real, R.imag]

if __name__ == "__main__":
    pass
