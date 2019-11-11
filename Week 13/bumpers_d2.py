# -*- coding: utf-8 -*-
"""
Classical (chaotic) scattering with a static 2D potential

Created on Mon Nov 11 10:33:50 2019

@author: gafeiden
"""
import numpy as np
import matplotlib.pyplot as plt

def bumperForce(x):
    """ Calculate force on ball at position [X, Y]
    
      Input:
          x -- list where x[0] == X, x[1] == Y
    
    """
    Fx = -2.0*x[0]*x[1]**2*(1.0 - x[0]**2)*np.exp(-(x[0]**2 + x[1]**2))
    Fy = -2.0*x[1]*x[0]**2*(1.0 - x[1]**2)*np.exp(-(x[0]**2 + x[1]**2))
    
    return [Fx, Fy]

def solveBumpers(x0, v0, m=1.0, dt=1.0e-3):
    """ """
    x = [x0]
    v = [v0]
    for n in range(int(100./dt)):
        F  = bumperForce(x[-1])
        
        v_X = v[-1][0] + F[0]*dt/m
        v_Y = v[-1][1] + F[1]*dt/m
        
        x_X = x[-1][0] + v[-1][0]*dt
        x_Y = x[-1][1] + v[-1][1]*dt
        
        v.append([v_X, v_Y])
        x.append([x_X, x_Y])
    
    x = np.array(x)
    v = np.array(v)
    
    return x, v

x1, v1 = solveBumpers(x0=[0.0, 0.1], v0=[0.1, 0.10])
x2, v2 = solveBumpers(x0=[0.0, 0.1], v0=[0.1, 0.11])

plt.plot(x1[:,0], x1[:,1], lw=2)
plt.plot(x2[:,0], x2[:,1], lw=2)
