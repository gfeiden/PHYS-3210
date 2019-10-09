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
and _V<sub>0</sub> = 10_. 

Your primary task is to find several bound-state 
energies, _E<sub>B</sub>_, that satisfy the above equation and to evaluate 
how altering the potential affects the number of bound states and the bound 
state energies. 

 1. Before you begin solving the problem using root finding techniques, 
    you need to better understand the function. Make a plot showing 
    
    ![equation](https://latex.codecogs.com/gif.latex?%5Clarge%20%5Csqrt%7B10%20-%20E_B%7D%5Ccdot%5Ctan%5Cleft%28%5Csqrt%7B10%20-%20E_B%7D%20%5Cright%29%20-%20%5Csqrt%7BE_B%7D%20%3D%200%5C%20%7B%5Crm%20vs%7D%5C%20E_B)
    
    Use your plot to get a rough sense of where _f(E<sub>B</sub>) = 0_. 
    You'll write a program to find precise values, but you need to know
    the domain of interest before you start your root finding procedure.

 2. Write a program that uses a bisection algorithm to find a solution 
    to the problem. The library `scipy.optimize` has a procedure called
    `bisect` that implements the bisection algorithm. You need to learn
    (a) what a bisection method is, and (b) how to use the algorithm.
    
 3. You may also use a Newton-Raphson method &mdash; the method you used
    to solve the masses on a string problem &mdash; to find the roots of 
    an equation. Use the `newton` method in `scipy.optimize` to find 
    solutions to the equation. Compare your solutions to those found with
    the bisection method.
    
 4. Evaluate _f(E<sub>B</sub>)_ to determine the precision of your solutions.
    
 5. Show that an alternative form of the _even_ equation is
 
    ![equation](https://latex.codecogs.com/gif.latex?%5Clarge%20%5Csqrt%7BE_B%7D%5Ccdot%5Ccot%5Cleft%28%5Csqrt%7B10%20-%20E_B%7D%20%5Cright%20%29%20-%20%5Csqrt%7B10%20-%20E_B%7D%20%3D%200.)
    
    Plot this equation and the original form. What do you notice? Why 
    might this function be advantageous compared to the other? Find the 
    roots of this equation using either method.

 6. Recall that the value 10 is related to the strength of the binding
    potential. What happens if you change the value from 10 to 20? What
    about to 30? 
    
 7. Evaluate the precision of your solutions.
 
 8. Try another root finding algorithm to find a solution to the problem.
    Which method did you choose and how does it work? Why might it be 
    better or worse compared to a bisection or Newton-Raphson method?
    
### Exercise 16: Temperature Dependence of Magnetization
Imagine a collection of _N_ spin&ndash;&frac12; particles each with a 
magnetic moment &mu;. The collection of particles has some temperature, 
_T_, and it's sitting in an external magnetic field, _B_. A good example would 
be a piece of iron in a rock on Earth (Earth has a magnetic field). 

When the collection of particles come to equilibrium there are _N<sub>L</sub>_
particles in the lower energy state (spins aligned with the magnetic field)
and _N<sub>U</sub>_ particles in the upper energy state (spins opposed to
the magnetic field). For a dipole with magnetic moment &mu;, its energy
in a magnetic field is given by _E = &minus;**&mu; &sdot; B**_. Thus, spin-up 
particles have a lower energy than spin-down particles. 

Assuming that the molecular magnetic field _B<sub>&mu;</sub> = &lambda; M_ 
is much stronger than the external magnetic field and that a Boltzmann
distribution will yield the number of particles in each state, we can
describe the _magnetization_ _M(T)_ by the equation 
_M(T) = &mu;(N<sub>L</sub> &minus; N<sub>U</sub>)_. Using a Boltzmann 
distribution to find the total number of particles in each energy state,
the equation can be written as

![equation](https://latex.codecogs.com/gif.latex?M%28T%29%20%3D%20N%5Cmu%20%5Ccdot%20%5Ctanh%5Cleft%28%5Cfrac%7B%5Clambda%5Cmu%20M%28T%29%7D%7Bk_B%20T%7D%20%5Cright%20%29)

This can be further simplified by choosing suitable non-dimensional quantities
_m = M / (N &mu;)_ and _t = T / T<sub>C</sub>_, where 
_T<sub>C</sub> = (N&mu;<sup>2</sup>&lambda;) / k<sub>B</sub>_ is a characteristic
temperature called the Curie Temperature. 

![equation](https://latex.codecogs.com/gif.latex?m%28t%29%20%3D%20%5Ctanh%5Cleft%28%5Cfrac%7Bm%28t%29%7D%7Bt%7D%20%5Cright%20%29)

Your task is to find the reduced magnetism, _m(T)_, as a function of 
temperature by solving the transcendental equation above using methods 
discussed on Monday. Remember to always plot your function _first_.

  1. In this case, the equation is slightly more complicated because we
     have two free variables, _m_ and _t_. To proceed, find the roots of 
     the equation for a variety of fixed _t_ values. Choose values above
     and below _t = 1_.
  
  2. Find the root of the equation to six significant figures for _t = 0.5_
     using the bisection and Newton-Raphson algorithms.
  3. Compare the time is takes to find the solutions.
  4. Construct a plot of the reduced magnetization _m(t)_ as a function 
     of the reduced temperature _t_. 
  5. For _t &ge; 1_, you should find that there are no solutions to the 
     equation. Explain why this is the case and why it makes physical sense.
  6. How does this problem relate to the evidence we have for seafloor 
     spreading due to tectonic plate motion and the evidence we have for 
     geomagnetic reversals?
     



    
