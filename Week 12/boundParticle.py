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
        # position inside potential
        V0 = -83.0
    else:
        # position outside potential
        V0 = 0.0
    return V0

def solve_wave_function(dx, x_left, x_right, a, E):
    """ """
    # set constants in Schrodinger Eq.
    q = 0.0483
    kappa_2 = -q*E
    kappa   = np.sqrt(kappa_2)
    
    # set initial conditions for x >> a using analytical solution
    xs   = [x_left]
    psi  = [np.exp(-kappa*abs(xs[-1]))]
    dpsi = [-np.sign(xs[-1]) * kappa * np.exp(-kappa*abs(xs[-1]))]
    
    # set in position using Eulerian scheme
    for n in range(int((x_right - x_left)/dx)):
        # x position from previous step
        x = xs[-1]
        
        # calculate new spatial derivative for wave function for step dx
        dpsi_new = dpsi[-1] + (q*potential(x, a) + kappa_2)*psi[-1]*dx
        
        # calculate new wave function value for step dx
        psi_new  = psi[-1]  + dpsi[-1]*dx
        
        # step in position from x_old to x_new
        x += dx  
        
        xs.append(x)          # append updated x position
        psi.append(psi_new)   # append new value for wavefunction 
        dpsi.append(dpsi_new) # append new spatial derivative of wave function
    
    xs   = np.array(xs)   # convert position list to array
    psi  = np.array(psi)  # convert wave function list to array
    dpsi = np.array(dpsi) # convert wave function derivative list to array
    
    return xs, psi, dpsi


# set parameters of run
a =  2.0       # potential size -a <= x <= +a
x_match = 1.9  # position to match the left/right integrator
dx = 1.0e-3    # absolute value of the position step size


# Guess initial values for energy iterator
E  = [-10.0, -20.0]
delta = E[1] - E[0]

# Energy iterator to solve for best fit E
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
    
    # calculate wave function and positional derivatives for test Energy
    xs_left,  psi_left,  dpsi_left  = solve_wave_function( dx, -100., x_match, a, E_test)
    xs_right, psi_right, dpsi_right = solve_wave_function(-dx,  100., x_match, a, E_test)
    
    # compute logarithmic derivative to check for convergence
    dE_test = (dpsi_left[-1]/psi_left[-1] - dpsi_right[-1]/psi_right[-1]) / (dpsi_left[-1]/psi_left[-1] + dpsi_right[-1]/psi_right[-1])
    
    # check whether wavefunction is continuous at x_match
    if (abs(dE_test) < 1.0e-5):
        # solution found, exit loop
        E_final = E_test
        print("Iteration {:02.0f}: Matched! E = {:+12.7f} MeV".format(n, E_final))
        break
    else:
        # select a new E and retry
        delta = np.sign(dE_test)*5.0
        E = [E_test, E_test + delta]
        print("Iteration {:02.0f}: No Match. Propose: E = {:+12.7f} MeV, deltaE = {:+12.7f} MeV".format(n, E_test, delta))



# create final curve using E_final (to be safe)
xs_left,  psi_left,  dpsi_left  = solve_wave_function( dx, -100., x_match, a, E_final)
xs_right, psi_right, dpsi_right = solve_wave_function(-dx,  100., x_match, a, E_final)

# plot the wave function for the best fit particle Energy
plt.plot(xs_left,  psi_left,  'o', ms=1.0)
plt.plot(xs_right, psi_right, 'o', ms=1.0)
plt.xlim(-a - 1.0, a + 1.0)
plt.xlabel("$x$ [fm]")
plt.ylabel("$\psi(x)$")
plt.show()

