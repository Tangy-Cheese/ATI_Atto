import numpy as np

import torch
import torch.nn as nn
import torch.optim as optim

from scipy.optimize import fsolve

import tqdm as tqdm
import warnings

import pandas as pd
import csv
import json

import matplotlib.pyplot as plt


# Constants
PI = np.pi

def physical_params()->None:
    
    omega = 0.057
    E_0 = 0.0534
    I_p = 0.5
    U_p = E_0**2 / (4*omega**2)
    t_cyc = 2*PI / omega 
    
    print("Params:")
    print(f"  ω  = {omega:.5f} a.u.    E₀ = {E_0:.5f} a.u.")
    print(f"  Ip = {I_p:.3f} a.u.     Up = {U_p:.4f} a.u.")
    print(f"  Keldysh γ = {np.sqrt(I_p/(2*U_p)):.3f}")
    print(f"  Cutoff 2U = {2*U_p:.4f} a.u.")

    pass

def vector_pot():

    

    return 
