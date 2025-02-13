import numpy as np
import math

# Constant parameters and assumed values
Tx_power = 1                            # Laser Power [W]
wave_length = 1550e-9                   # Optical Laser wavelength [m]
L = [2, 5, 10, 20, 30, 40 ,50]          # Distance Tx to Rx
theta_div = 20                          # Divergence angle [microrad]

# Simple functions for calculating the gain and losses
def Tx_gain(theta_div):
    Gtx = 8/(theta_div**2)
    return Gtx

def Tx_trans_loss(T):        
    return T

def free_space(wave_length, L):
    L_fs = ((wave_length)/(4 * np.pi() * L)) ** 2
    return

def atmos_loss(T):
    return T

def static_loss(theta_pe, theta_div):
    T_pe = np.exp((-2 * theta_pe ** 2)/(theta_div))
    L_pe = 10 * np.log(T_pe)
    return L_pe

def avg_jitter_loss(theta_div, sigma_pj):
    T_pa = (theta_div ** 2)/(theta_div ** 2 + 4 * sigma_pj ** 2)
    L_pa = 10 * np.log(T_pa)
    return L_pa

def jitter_scint_loss (p0, sigma_pj, theta_div, L_pa):
    L_ps = 10 * np.log(p0 ** ((4 * sigma_pj ** 2)/(theta_div ** 2))) + L_pa
    return L_ps

def 


# Trade off to find optimum divergence angle
def system_tradeoff():
    return

def geometric_loss(Lfs, Gtx):
    Geo_loss = Lfs + Gtx
    return 