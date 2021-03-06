## Week 05: Differentiation &amp; Integration

### Readings
From _Computational Physics_:
 1. Sections 5.1  &ndash; 5.3  (by Tuesday)
 2. Sections 5.7  &ndash; 5.11 (by Wednesday)
 3. Sections 5.14 &ndash; 5.15 (by Friday)

### Exercise 08: Difference Algorithms
Derivatives are an essential operation in physics as they describe the 
rate of change of a quantity with respect to some other quantity (typically 
a spacial dimension or time). You probably remember how to take derivatives 
of various functions from memory (e.g., power rule, chain rule, etc.), but 
it has probably been a while since you used the definition of a derivative
to calculate a derivative's value. Recall,

![equation](https://latex.codecogs.com/png.latex?%5Clarge%20f%27%28x%29%20%3D%20%5Cfrac%7Bdf%7D%7Bdx%7D%20%3D%20%5Clim_%7Bh%20%5Crightarrow%200%7D%20%5Cfrac%7Bf%28x%20&plus;%20h%29%20-%20f%28x%29%7D%7Bh%7D)

which results from a taking a Taylor expansion of the function _f(x + h_).
While you may have found this to be an annoyance in Calculus, this explicit
definition provides an algorithm for computing a derivative, called 
_Forward Difference_.

Today, we are going to look at different schemes for finding a numerical 
derivative of the function _f(x)_ = sin(_x_). Here are your tasks:

 1. **_For your write up_**: Derive the definition of a derivative by 
    expanding _f_(_x + h_) about the point _x_ (since _h_ is small).
 2. Create two arrays, one for _x_ and one for sin(_x_). Use NumPy's `arange` 
    function to create an array of _x_ values from &minus;2&pi; to 2&pi; 
    with equal spacing _h_, where _h_ is some small value. Then, create
    an array for sin(_x_) using NumPy's built in `sin` function (you've 
    already demonstrated you can do this numerically).
 3. Write a function to compute the derivative of sin(_x_) using a forward
    difference scheme. 
 4. Plot your forward difference derivative f'(_x_) vs _x_ and compare it
    to the derivative returned by NumPy's `gradient` function. Also, compare
    results from both algorithms to the exact, analytical value. 
 5. Create an error plot, showing the relative error for each algorithm
    compared to the exact value.
 6. Are there any differences between the algorithms? Explain using your
    figures as evidence.
 7. What is the difference between NumPy's `gradient` function and your 
    foward difference algorithm? Explain.
 8. Compute second derivatives using each algorithm and compare your results
    to the analytical value. Graph both the function and the relative error
    compared to the exact value.
 9. _Challenge_: Add random noise to your function, i.e., _f_(_x_) = 
    sin(_x_) + &epsilon;, where &epsilon; is a small, random number.
10. _Bonus_: Do the same test, but for a different function, e.g., 
    _f_(_x_) = x<sup>2</sup> or _f_(_x_) = _e_<sup>_x_</sup>.
    
### Exercise 09: Integration Techniques
An equally important operation in physics is the integral, where you attempt
to specify the area under some &mdash; typically predefined &mdash; curve. 
Again, you may recall how to perform some integrals from memory or, if 
given enough time, you could analytically calculate a number of different 
integrals. However, integrals are fairly straight forward to calculate 
numerically. Just as we utilized the limit definition of a derivative as
an algorithm, we can do the same for an integral. Recall,

![equation](https://latex.codecogs.com/png.latex?%5Clarge%20%5Cint_a%5Eb%20f%28x%29%20dx%20%3D%20%5Clim_%7Bh%20%5Crightarrow%200%7D%5Cleft%5Bh%20%5Csum_%7Bi%3D1%7D%5E%7B%28b-a%29/h%7D%20f%28x_i%29%20%5Cright%20%5D)
    
A direct translation of this definition into a numerical algorithm suggests
that, to integrate a function, you divide the domain of interest into a 
series of small boxes of width _h_ and height _f(x<sub>i</sub>)_. 

Of course, a square box may not perfectly represent the shape of the function,
so other algorithms have been developed to better approximate the shape
of an arbitrary function at the top of the box (e.g., trapezoid rule, 
Simpson's rule, Gaussian quadrature).

Here are your tasks for today:
  1. Write a function to integrate an array of values with some spacing 
     _dx_ in the domain. (i.e., write a function to calculate an integral
     using the algorithm specified above)
  2. Integrate _f(x) = x<sup>2</sup> from _x = 0_ to _x = 10_ using your
     integration function.
  3. Compare your result to the analytical solution.
  4. Compare your result to the solution using NumPy's trapezoid integration
     function `trapz`. 
  5. Import the SciPy library `scipy.integrate` and use a few different 
     integration routines to compare to the results of your integrator. 
  6. Repeat steps 2 &ndash; 5 for function _f<sub>1</sub>(x)_ listed below. Explain why
     your integrator may have trouble with this function. Which integrators
     from SciPy provide consistent results and which of the ones you tested
     are more like the results from your integrator?
  7. _For Your Write Up_: Look up the algorithm for one of the SciPy 
     integrators that returned different results. Explain why the results
     may be different and whether your think the SciPy integrator is more
     accurate.

Functions to integrate:

![equation](https://latex.codecogs.com/png.latex?%5Clarge%20f_%7B1%7D%28x%29%20%3D%20%5Cint_%7B0%7D%5E%7B2%5Cpi%7D%20%5Csin%28100x%29%5Ctextup%7Bd%7Dx)
&nbsp;&nbsp;&nbsp;
![equation](https://latex.codecogs.com/png.latex?%5Clarge%20f_%7B2%7D%28x%29%20%3D%20%5Cint_%7B0%7D%5E%7B2%5Cpi%7D%20%5Csin%5Ex%28100x%29%5Ctextup%7Bd%7Dx)

  
## Exercise 10: Monte Carlo Integration
Integration methods discussed on Wednesday (Exercise 09) work very well
for single and double integrals. As the dimensionality of your integral 
increases, it's preferable to use Monte Carlo (MC) methods. You've used 
MC methods already, they're methods that require the use of random 
numbers. While it's rather intuitive to understand why MC methods work
for random walks, it's perhaps not obvious that they can be used to evaluate
integrals.

The most basic MC methods rely on using a _sampling_ technique. To illustrate
how a sampling technique works, you're going to compute the value of &pi;
by performing a 2D integration (_Computational Physics_, pg 104). 

 1. Imagine a circular pond within a square with sides of length 2 units.
    Place the circular pond at the square's center and allow it to have 
    a radius _R = 1_ unit.
 2. Recall that the analytic answer is
 
    ![equation](https://latex.codecogs.com/png.latex?%5Clarge%20A%20%3D%20%5Ciint%20r%20%5Ctextup%7Bd%7Dr%5Ctextup%7Bd%7D%5Cphi%20%3D%20%5Cpi%20R%5E2)
    
    which is equal to &pi; if _R = 1_ unit.
 3. Generate a random sample of _N_ points (_x<sub>i</sub>_, _y<sub>i</sub>_) 
    within the square such that _&minus;1 &le; x<sub>i</sub> &le; 1_ and 
    _&minus;1 &le; y<sub>i</sub> &le; 1_.
 4. For each point, calculate its distance _r<sub>i</sub>_ from the square's
    center. If _r<sub>i</sub>_ &le; 1, increase the number of points in
    the pond by one `N_pond += 1`.
 5. Calculate the value of &pi; knowing that the number of points in the
    pond compared to the total number of points is related to the ratio 
    of the pond's area to the square's area (assuming all points are randomly
    and uniformly distributed) 
 
    ![equation](https://latex.codecogs.com/png.latex?%5Clarge%20%5Cfrac%7BN_%7B%5Crm%20pond%7D%7D%7BN%7D%20%3D%20%5Cfrac%7BA_%7B%5Crm%20pond%7D%7D%7BA_%7B%5Crm%20square%7D%7D)
 
 6. Plot your sample points and draw a cirlce to show which points are 
    within the pond. Ideally, your visualization would plot your sample
    using different color points for the points inside and outside of the
    pond. 
 7. Increase your sample size _N_ until you get &pi; accurate to three 
    significant figures. Approximately how large a value for _N_ was required?

Write up your results and include at least one figure as described in part 6.
 
If you finish early, go back and work on previous exercises, or re-read
Section 5.15 and use an MC method to evaluate the integral

![equation](https://latex.codecogs.com/png.latex?%5Clarge%20I%20%3D%20%5Cint_%7B0%7D%5E%7B10%7D%20x%5E2%20%5Ctextup%7Bd%7Dx)
    




    
