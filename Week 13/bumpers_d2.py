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
    t = [0.0]
    x = [x0]
    v = [v0]
    for n in range(int(100./dt)):
        F  = bumperForce(x[-1])
        
        v_X = v[-1][0] + F[0]*dt/m
        v_Y = v[-1][1] + F[1]*dt/m
        
        x_X = x[-1][0] + v[-1][0]*dt
        x_Y = x[-1][1] + v[-1][1]*dt
        
        # check for wall collision in x-direction
        if (3.0 - abs(x_X) < 1.0e-4) or abs(x_X) > 3.0:
            v_X = -1.0*v_X
        elif (3.0 - abs(x_Y) < 1.0e-4) or abs(x_Y) > 3.0:
            v_Y = -1.0*v_Y
        else:
            pass
        
        v.append([v_X, v_Y])
        x.append([x_X, x_Y])
        t.append(t[-1] + dt)
    
    t = np.array(t)
    x = np.array(x)
    v = np.array(v)
    
    return t, x, v

t1, x1, v1 = solveBumpers(x0=[-0.5, 0.4], v0=[ 1.1, 1.1], m=0.1, dt=1.0e-4)
t2, x2, v2 = solveBumpers(x0=[-0.5, 0.4], v0=[ 0.1, 0.1], m=0.1, dt=1.0e-4)

# plot potential contours
x_v = np.arange(-10.0, 10.01, 0.01)
y_v = np.arange(-10.0, 10.01, 0.01)
X_v, Y_v = np.meshgrid(x_v, y_v)
Z_v = X_v**2 * Y_v**2 * np.exp(-(X_v**2 + Y_v**2))

# PLOT TRAJECTORIES W/ POTENTIAL CONTOURS
fig, ax = plt.subplots(1, 1)#, figsize=(10, 8))

cb = ax.contourf(X_v, Y_v, Z_v, 10, cmap="Oranges")
ax.plot(x1[:,0], x1[:,1], lw=1)
ax.plot(x2[:,0], x2[:,1], lw=1)

ax.set_xlim(-3.0, 3.0)
ax.set_xlabel("X Position")
ax.set_ylim(-3.0, 3.0)
ax.set_ylabel("Y Position")

cbar = fig.colorbar(cb)
cbar.ax.set_ylabel("Scattering Potential")

fig.tight_layout()
plt.show()

# PLOT Position vs Time
fig, ax = plt.subplots(2, 1)
ax[0].plot(t1, x1[:,0], lw=1)
ax[0].plot(t2, x2[:,0], lw=1)
ax[0].set_xlabel("Time [s]")
ax[0].set_ylim(-3.0, 3.0)
ax[0].set_ylabel("X Position")

ax[1].plot(t1, x1[:,1], lw=1)
ax[1].plot(t2, x2[:,1], lw=1)
ax[1].set_xlabel("Time [s]")
ax[1].set_ylim(-3.0, 3.0)
ax[1].set_ylabel("Y Position")

fig.tight_layout()
plt.show()

# PLOT Velocity vs Time
fig, ax = plt.subplots(2, 1)
ax[0].plot(t1, v1[:,0], lw=1)
ax[0].plot(t2, v2[:,0], lw=1)
ax[0].set_xlabel("Time [s]")
ax[0].set_ylim(-1.0, 1.0)
ax[0].set_ylabel("X Velocity")

ax[1].plot(t1, v1[:,1], lw=1)
ax[1].plot(t2, v2[:,1], lw=1)
ax[1].set_xlabel("Time [s]")
ax[1].set_ylim(-1.0, 1.0)
ax[1].set_ylabel("Y Velocity")

fig.tight_layout()
plt.show()

# PLOT Velocity vs Position
fig, ax = plt.subplots(2, 1)
ax[0].plot(x1[:,0], v1[:,0], lw=1)
ax[0].plot(x2[:,0], v2[:,0], lw=1)
ax[0].set_xlabel("X Position")
ax[0].set_xlim(-3.0, 3.0)
ax[0].set_ylabel("X Velocity")

ax[1].plot(x1[:,1], v1[:,1], lw=1)
ax[1].plot(x2[:,1], v2[:,1], lw=1)
ax[1].set_xlabel("Y Position")
ax[1].set_xlim(-3.0, 3.0)
ax[1].set_ylabel("Y Velocity")

fig.tight_layout()
plt.show()