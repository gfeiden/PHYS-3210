## Week 09: Data Fitting &amp; Interpolation

### Readings
From _Computational Physics_:
 1. Sections 7.5 &amp; 7.7 (by Wednesday)
 2. Section 8.1 &ndash; 8.3 (by Friday)

### Exercise 17: Fitting an Energy Spectrum w/ Lagrange Interpolation
_Problem 3 in Chapter 7 of Computational Physics_

The cross sections measured for the resonant scattering of neutrons from 
a nucleus are given in Table 7.1 (pg. 151). As shown in the table, the data 
was taken in energy steps of 25 MeV. However, to test theoretical predictions,
we need the data at a higher resolution. 

There are a couple common ways to solve this problem: interpolation or
least-squares fitting. Today, we'll explore interpolation, or the process
of using known data to estimate values of intermediate data points (data
on a sub-grid scale).

Your tasks are to:

 1. Write a subroutine to perform an _n_-point Lagrange interpolation using 
    the above equation (7.23 in your book). Treat _n_ as an arbitrary
    input parameter. (actually, use routines in `scipy.interpolate`) 
 2. Use your Lagrange interpolation procedure to fit the entire experimental
    spectrum given in Table 7.1 with one polynomial (i.e., fit all nine 
    data points with an eighth-order polynominal). Use your polyinomial 
    to plot the cross section in steps of 5 MeV.
 3. Use your graph to deduce the resonance energy, E<sub>r</sub> (the
    peak position) and &Gamma; (the full-width at half-maximum). Compare 
    your results with those predicted by a theorist 
    (E<sub>r</sub>, &Gamma;) = (78, 55) MeV.
 4. A more realistic use of Lagrange interpolation is to perform local
    interpolation over a small domain of the data, e.g., over three data
    points. Interpolate the preceding cross-sectional data in 5 MeV steps
    using 3-point Lagrange interpolation over each interval (Note that 
    the ends may be special cases).
 5. Now, try fitting the data using a few different 1D interpolation 
    algorithms. Try performing 1D linear interpolation between data points
    and try a 1D cubic spline interpolation. Plot the cross section in
    steps of 5 MeV.
 6. Discuss and compare your results.
    





    
