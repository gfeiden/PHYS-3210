# -*- coding: utf-8 -*-
"""
Shooting solution for finite square well potential

Created on Mon Nov  4 10:30:05 2019

@author: gafeiden
"""
import numpy as np
import matplotlib.pyplot as plt

def potential(x, a):
    """ """
    if abs(x) <= a:
        V0 = -83.0
    else:
        V0 = 0.0
    return V0

def wave_function_outside(x, kappa_2):
    """ """ 
    psi = np.exp(-kappa_2*abs(x))
    dpsi_dx = -1.0*x/abs(x) * kappa_2*np.exp(-kappa_2*abs(x))
    return psi, dpsi_dx

def solve_wave_function(dx, x_left, x_right, kappa_2, E):
    """ """
    x    = [xl]
    psi  = [np.exp(-kappa_2*abs(x[-1]))]
    dpsi = [-1.0*x/abs(x) * kappa_2 * np.exp(-kappa_2*abs(x[-1]))]
    for n in range(int((x_right - x_left)/dx)):
        
    return 