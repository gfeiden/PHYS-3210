## Week 08: Trial-and-Error Searching &amp; Data Fitting

### Readings
From _Computational Physics_:
 1. Sections 7.1 &ndash; 7.4 (by Wednesday)
 2. Section 7.5 (by Friday) 

### Introduction
In Lab 04, we saw an example of a trial-and-error approach to finding a
solution to a set of coupled, non-linear equations. The idea of iterating
to a solution by improving on an initial guess is ubiquitous in computational
science and is a foundational technique. We're going to further explore 
the trial-and-error process this week.

### Exercise 15: Finding Bound-State Energies
The primary idea behind trial-and-error methods is to find the roots of 
an equation, or set of equations. That is, to find where _f(x) &asymp; 0_.
For any equation, it is typically possible to rewrite it in this form, 
allowing a solution to be found through _root finding_ procedures. Let's 
look at an example.

A particle with mass _m_ bound within a 1D finite square well of radius 
_a_ is permitted to have only specific energies while in the bound state. 
The value of the potential as a function of position is

![equation](https://latex.codecogs.com/gif.latex?%5Clarge%20V%28x%29%20%3D%20%5Cleft%5C%7B%20%5Cbegin%7Bmatrix%7D%20-V_0%20%26%20%7B%5Crm%20for%20%7D%5C%20%7Cx%7C%20%5Cle%20a%5C%5C%200%20%26%20%7B%5Crm%20for%20%7D%5C%20%7Cx%7C%20%3E%20a%20%5C%5C%20%5Cend%7Bmatrix%7D%5Cright.)

Energies of bound states _E = &minus;E<sub>B</sub> < 0_ within the well 
are solutions to the equations

![equation](https://latex.codecogs.com/gif.latex?%5Clarge%20%5Csqrt%7B10%20-%20E_B%7D%5Ccdot%5Ctan%5Cleft%28%5Csqrt%7B10%20-%20E_B%7D%20%5Cright%29%20%3D%20%5Csqrt%7BE_B%7D%5C%20%7B%5Crm%20%28even%29%7D)

![equation](https://latex.codecogs.com/gif.latex?%5Clarge%20%5Csqrt%7B10%20-%20E_B%7D%5Ccdot%5Ccot%5Cleft%28%5Csqrt%7B10%20-%20E_B%7D%20%5Cright%29%20%3D%20%5Csqrt%7BE_B%7D%5C%20%7B%5Crm%20%28odd%29%7D)

where _even_ and _odd_ refer to the wave function's symmetry. The problem
has been simplified by choosing units so that &hbar; = 1, 2_m_ = 1, _a_ = 1,
and _V<sub>0</sub> = 10_. Your primary task is to find several bound-state 
energies, _E<sub>B</sub>_, that satisfy the above equation and to evaluate 
how altering the potential affects the number of bound states and the bound 
state energies.



 1. Use the `bisect`and `newton` methods available in `scipy.optimize`
    to find roots of the equation using bisection and Newton-Raphson
    algorithms, repsectively.
    
