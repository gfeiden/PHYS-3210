## Week 10: Ordinary Differential Equations &ndash; Non-linear Oscillations

### Readings
From _Computational Physics_:
 1. Sections 9.1 &amp; 9.3 (by Wednesday)
 2. Sections 9.4 &amp; 9.7 (by Friday)

### Exercise 22: Shooting for an Eigenvalue Solution
_Based on Problem 9.1 in Computational Physics_

Consider a particle with definite energy _E_ moving in a one-dimensional
finite square well potential, _V(x)_. To determine the particle's energy
and its wavefunction, we must solve the one-dimensional Schr&ouml;dinger 
equation,

![equation](https://latex.codecogs.com/png.latex?-%5Cfrac%7B%5Chbar%5E2%7D%7B2m%7D%5Cfrac%7Bd%5E2%7D%7Bdx%5E2%7D%5Cpsi%28x%29%20&plus;%20V%28x%29%5Cpsi%28x%29%20%3D%20E%5Cpsi%28x%29)

In this case, it is safe to assume the system is time-independent. If we
are interested to compute the bound-state energies, we must solve the ODE
while simultaneously satisfying the boundary conditions, turning our problem
into one of finding the eigenvalues _E_ as well as solving for the wave
function _&psi;(x)_.

Your task is to solve for _&psi;(x)_ and the ground state energy (i.e., 
the most negative eigenvalue) using a shooting method. Assume the potential
for our finite square well is

![equation](https://latex.codecogs.com/png.latex?V%28x%29%20%3D%20%5Cbegin%7Bcases%7D%20-V_0%20%3D%20-83%5C%20%5Ctextrm%7B%20MeV%2C%7D%20%26%20%5Ctextrm%7B%20for%20%7D%20%7Cx%7C%20%5Cle%20a%20%3D%202%5C%20%5Ctextrm%7Bfm%7D%2C%20%5C%5C%200%2C%20%26%20%5Ctextrm%7B%20for%20%7D%20%7Cx%7C%20%3E%20a%20%3D%202%5C%20%5Ctextrm%7Bfm%7D%2C%20%5Cend%7Bcases%7D)
    
Write a rudimentary solver following the general steps outlined in Section 
9.2. Start by planning how you are going to approach solving this problem
on a white board and/or in your notes. __Work with a partner, or two__. 
Plot your potential and the ground state wave function once you've solved 
the problem.


    
    
