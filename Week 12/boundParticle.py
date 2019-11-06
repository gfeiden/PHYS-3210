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

def wave_function_outside(x, kappa):
    """ """ 
    psi = np.exp(-kappa*abs(x))
    dpsi_dx = -1.0*x/abs(x) * kappa*np.exp(-kappa*abs(x))
    return psi, dpsi_dx

def solve_wave_function(dx, x_left, x_right, a, E):
    """ """
    q = 0.0483
    kappa_2 = -q*E
    
    xs   = [x_left]
    psi  = [np.exp(-np.sqrt(kappa_2)*abs(xs[-1]))]
    dpsi = [-1.0*(xs[-1])/abs(xs[-1]+1.0e-16) * np.sqrt(kappa_2) * np.exp(-np.sqrt(kappa_2)*abs(xs[-1]))]
    for n in range(int((x_right - x_left)/dx)):
        x = xs[-1]
        if abs(x) > a:
            psi_new, dpsi_new = wave_function_outside(x+dx, np.sqrt(kappa_2))
        else:
            dpsi_new = dpsi[-1] + (q*potential(x, a) + kappa_2)*psi[-1]*dx
            psi_new  = psi[-1] + dpsi[-1]*dx
        
        x += dx
        
        xs.append(x)
        psi.append(psi_new)
        dpsi.append(dpsi_new)
    
    xs   = np.array(xs)
    psi  = np.array(psi)
    dpsi = np.array(dpsi)
    return xs, psi, dpsi

E = -20.0    
a =  2.0
x_match = a
dx = 1.0e-2

xs = np.arange(-100., 100., 1.0e-2)
V  = []
for x in xs:
    if abs(x) > a:
        V.append(0)
    else:
        V.append(-83.0)
V = np.array(V)

E  = [-10.0, -20.0]
dE = []
delta = E[1] - E[0]
for n in range(30):
    dE = []
    
    # try a lower value for |E|
    xs_left,  psi_left,  dpsi_left  = solve_wave_function( dx, -100., x_match, a, E[0])
    xs_right, psi_right, dpsi_right = solve_wave_function(-dx,  100., x_match, a, E[0])

    dE.append((dpsi_left[-1]/psi_left[-1] - dpsi_right[-1]/psi_right[-1]) / (dpsi_left[-1]/psi_left[-1] + dpsi_right[-1]/psi_right[-1]))

    # try a higher value for |E|
    xs_left,  psi_left,  dpsi_left  = solve_wave_function( dx, -100., x_match, a, E[1])
    xs_right, psi_right, dpsi_right = solve_wave_function(-dx,  100., x_match, a, E[1])

    dE.append((dpsi_left[-1]/psi_left[-1] - dpsi_right[-1]/psi_right[-1]) / (dpsi_left[-1]/psi_left[-1] + dpsi_right[-1]/psi_right[-1]))

    # choose new E for a test run
    #E_test = 
    break
    # check whether wavefunction is continuous at xmatch
    if (abs(psi_left[-1] - psi_right[-1]) < 1.0e-6):
        # solution found, exit loop
        break
    else:
        # select a new E and retry
        pass

#plt.plot(xs, V, '-', lw=3, c="black")
plt.plot(xs_left,  psi_left,  'o', ms=1.0)
plt.plot(xs_right, psi_right, 'o', ms=1.0)
plt.xlim(-a - 1.0, a + 1.0)
plt.xlabel("$x$ [fm]")
plt.ylabel("$\psi(x)$")
plt.show()

