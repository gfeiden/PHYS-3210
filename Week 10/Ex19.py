# -*- coding: utf-8 -*-
"""
Anharmonic Oscillations with Euler's Method

Created on Mon Oct 21 10:32:23 2019

@author: gafeiden
"""
import numpy as np
import matplotlib.pyplot as plt

def springForce(k, x, p):
    """ Calculate the spring force """
    return -k*x**(p - 1)

# initial conditions of mass
m  = 1.0  # object's mass [kg]
v0 = 0.0  # object's initial x velocity [m/s]
x0 = 1.0  # object's initial position [m]

v_list = [v0]
x_list = [x0]

# spring constant
k = 10.0   # 
p = 2

dt = 1.0e-2  # time step [s]
t  = 0.0     # initial time [s]
t_list = [t]
for i in range(1000):
    t  += dt
    v0 += dt/m * springForce(k, x0, p)
    x0 += v0*dt
    
    v_list.append(v0)
    x_list.append(x0)
    t_list.append(t)
    
plt.plot(x_list, t_list, '-', lw=3)
plt.xlabel("Position [m]")
plt.ylabel("Time [s]")
