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
    
### Exercise 18: Pi Meson Lifetime
Figure 7.6 in your book shows experimental data on the number of decays,
N_decay, of the &pi; meson as a function of time (Stetz et al. 1993). 
The data has been binned into intervals of &Delta;t = 10 ns. Your problem
is to evaluate how well a typical radioactive decay model describes the
data and, if it provides a reasonable description of the data, to determine
the &pi; meson's lifetime, &tau;.

To perform these tasks, you are going to perform linear and non-linear 
least-squares regressions using the pre-packaged SciPy routine `curve_fit` 
from the `scipy.optimize` library.

Your tasks are to:
 1. Read in the data from `pi_meson_decays.dat`. Compare the times and 
    measured decays to Figure 7.6 and assess whether you think it looks
    reasonable.
 
 2. Estimate the error (or uncertainty) for each bin and construct a new
    array of those uncertianties. (hint: we are essentially counting the 
    number of decays)
 
 3. You can linearize the exopnential decay law (Taylor expand), which 
    should be valid over long time baselines. That is
    
    ![equation](https://latex.codecogs.com/gif.latex?%5Cln%5Cleft%7C%20%5Cfrac%7B%5CDelta%20N%28t%29%29%7D%7B%5CDelta%20t%7D%20%5Cright%7C%20%5Capprox%20%5Cln%5Cleft%7C%20%5Cfrac%7B%5CDelta%20N_0%7D%7B%5CDelta%20t%7D%20%5Cright%7C%20-%20%5Cfrac%7B1%7D%7B%5Ctau%7D%5CDelta%20t)
    
    which is linear in &Delta;t and is therefore ammenable to a linear
    regression analysis.
 
 4. Perform a least-squares regression for a function that fits a straight
    line (of the form given above) to the data. (hint: you'll need to 
    manipulate your data to put it in the correct form) Compare your inferred
    &pi; meson lifetime to the tabulated lifetime of 2.6 x 10<sup>&minus;8</sup> s
    and comment on the difference.
    
 5. Plot the data and your best fit straight line on the same graph and 
    comment on the agreement.
    
 6. Perform the a non-linear least-squares regression on the data using 
    the formula for exponential decay. How does your inferred &pi; meson
    lifetime compare to the value inferred from linear regression?
    
 7. Plot your best fit exponential decay curve and the data on the same
    graph and comment on the agreement.
 
 8. For both cases, deduce goodness of fit of the fitted curve and the 
    estimate the approximate error on your inferred lifetime. How does 
    this look to your eye? 
    
 9. Discuss ways to improve the quality of your fit. Try one or two!



    
