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
    dpsi_dx = -np.sign(x) * kappa * np.exp(-kappa*abs(x))
    return psi, dpsi_dx

def solve_wave_function(dx, x_left, x_right, a, E):
    """ """
    q = 0.0483
    kappa_2 = -q*E
    kappa   = np.sqrt(kappa_2)
    
    xs   = [x_left]
    psi  = [np.exp(-kappa*abs(xs[-1]))]
    dpsi = [-np.sign(xs[-1]) * kappa * np.exp(-kappa*abs(xs[-1]))]
    for n in range(int((x_right - x_left)/dx)):
        x = xs[-1]
        if abs(x) > a:
            psi_new, dpsi_new = wave_function_outside(x+dx, kappa)
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
a =  1.5
x_match = a
dx = 1.0e-2

E  = [-10.0, -20.0]
delta = E[1] - E[0]
for n in range(20):
    dE = []
    
    # try a lower value for |E|
    xs_left,  psi_left,  dpsi_left  = solve_wave_function( dx, -100., x_match, a, E[0])
    xs_right, psi_right, dpsi_right = solve_wave_function(-dx,  100., x_match, a, E[0])

    dE.append((dpsi_left[-1]/psi_left[-1] - dpsi_right[-1]/psi_right[-1]) / (dpsi_left[-1]/psi_left[-1] + dpsi_right[-1]/psi_right[-1]))

    # try a higher value for |E|
    xs_left,  psi_left,  dpsi_left  = solve_wave_function( dx, -100., x_match, a, E[1])
    xs_right, psi_right, dpsi_right = solve_wave_function(-dx,  100., x_match, a, E[1])

    dE.append((dpsi_left[-1]/psi_left[-1] - dpsi_right[-1]/psi_right[-1]) / (dpsi_left[-1]/psi_left[-1] + dpsi_right[-1]/psi_right[-1]))

    # bisect to find a new E for test run
    DdE_DE = (dE[1] - dE[0])/(E[1] - E[0])
    E_test = E[0] - dE[0]/DdE_DE
    
    xs_left,  psi_left,  dpsi_left  = solve_wave_function( dx, -100., x_match, a, E_test)
    xs_right, psi_right, dpsi_right = solve_wave_function(-dx,  100., x_match, a, E_test)
    
    dE_test = (dpsi_left[-1]/psi_left[-1] - dpsi_right[-1]/psi_right[-1]) / (dpsi_left[-1]/psi_left[-1] + dpsi_right[-1]/psi_right[-1])
    
    print(dE_test)
    # check whether wavefunction is continuous at xmatch
    if (abs(dE_test) < 1.0e-8):
        # solution found, exit loop
        E_final = E_test
        print("Iteration {:02.0f}: Matched! E = {:+12.7f} MeV".format(n, E_final))
        break
    else:
        # select a new E and retry
        delta = -np.sign(dE_test)
        E = [E_test, E_test + delta]
        print("Iteration {:02.0f}: No Match. Propose: E = {:+12.7f} MeV, deltaE = {:+12.7f} MeV".format(n, E_test, delta))


xs_left,  psi_left,  dpsi_left  = solve_wave_function( dx, -100., x_match, a, E_final)
xs_right, psi_right, dpsi_right = solve_wave_function(-dx,  100., x_match, a, E_final)

plt.plot(xs_left,  psi_left,  'o', ms=1.0)
plt.plot(xs_right, psi_right, 'o', ms=1.0)
#plt.xlim(-a - 1.0, a + 1.0)
plt.xlabel("$x$ [fm]")
plt.ylabel("$\psi(x)$")
plt.show()

