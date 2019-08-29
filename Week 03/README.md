## Week 03: Computational Errors and Uncertainties

### Readings

 1. Section 3.1 (by Monday)

### Exercise 05: Subtractive Cancelation &ndash; Harmonic Series
Round off error has a way of creeping into seemingly simple computations.
Consider, for example, two different ways to calculate a finite harmonic 
series,

![equation](https://latex.codecogs.com/gif.latex?%5Clarge%20H_N%5E%7B%5Crm%20up%7D%20%3D%20%5Csum_%7Bn%3D1%7D%5E%7BN%7D%5Cfrac%7B1%7D%7Bn%7D%5C%20%5Ctextrm%7B%20and%20%7D%5C%20H_N%5E%7B%5Crm%20dn%7D%20%3D%20%5Csum_%7Bn%3DN%7D%5E%7B1%7D%5Cfrac%7B1%7D%7Bn%7D) .

Both series are finite, provided that _N_ is a finite number, and they 
should, in principle, yield the same value for _H<sub>N</sub>_. 

Your task is to
 1. Write a function that accepts _N_ as an input and returns a finite 
    harmonic series using each algorithm. (or write two functions, it's
    up to you).
 2. Make a plot showing &nbsp;&nbsp;
    ![equation](https://latex.codecogs.com/gif.latex?%5Clarge%20%5Cfrac%7BH_N%5E%7B%5Crm%20up%7D%20-%20H_N%5E%7B%5Crm%20dn%7D%7D%7B%7CH_N%5E%7B%5Crm%20up%7D%7C%20&plus;%20%7CH_N%5E%7B%5Crm%20dn%7D%7C%7D%20%5Ctextrm%7B%20vs%20%7D%20N)
 3. Observe the linear regime in your figure and explain why the downward
    sum is generally more precise. If you are having trouble seeing that
    this is the case, find an analytical solution for the _N = 6_ harmonic
    series. Compare your two algorithmic answers to the analytical solution.

### Exercise 06: Subtractive Cancelation &ndash; Quadratic Formula

