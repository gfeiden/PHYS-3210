## Week 06: Sampling Methods in MC Integration

### Readings
From _Computational Physics_:
 1. Section 5.15 &ndash; 5.17 (by Wednesday)
 2. Section 5.20 &ndash; 5.22 (by Friday)

### Exercise 11: MC Mean Value Method
At its core, MC methods rely on the _mean value theorem_, which states that

![equation](https://latex.codecogs.com/png.latex?%5Clarge%20I%20%3D%20%5Cint_%7Ba%7D%5E%7Bb%7D%20f%28x%29%5Ctextup%7Bd%7Dx%20%3D%20%28b%20-%20a%29%5Clangle%20f%20%5Crangle)

or that the value of an integral is equal to the mean value of the function over an
interval, multiplied by the width of the interval. An MC method evaluates the integral 
by drawing _random samples_ from within the desired interval, evaluating the function 
at each point in the sample, and then computing the mean. Since

![equation](https://latex.codecogs.com/png.latex?%5Clarge%20%5Clangle%20f%20%5Crangle%20%5Csimeq%20%5Cfrac%7B1%7D%7BN%7D%5Csum_%7Bi%20%3D%201%7D%5E%7BN%7D%20f%28x_i%29)

we are easily able to calculate the _sample mean_. We can then approximate the integral

![equation](https://latex.codecogs.com/png.latex?%5Clarge%20I%20%5Csimeq%20%5Cfrac%7B%28b%20-%20a%29%7D%7BN%7D%5Csum_%7Bi%20%3D%201%7D%5E%7BN%7D%20f%28x_i%29)

Today, your tasks are to: 
 1. Integrate the function 

    ![equation](https://latex.codecogs.com/png.latex?%5Clarge%20I%20%3D%20%5Cint_%7B0%7D%5E%7B10%7D%20x%5E2%20%5Ctextup%7Bd%7Dx)
    
    using an MC Mean Value Method by sampling the function 1,000 times. Save each x, y 
    pair. How does your value compare to the analytical value? What if you used 10,000
    samples?
 2. Compute the MC integral, again. Did you get the same value? Plot the (x, y) pairs. 
    What does the resulting figure look like? Does it make sense, given what you've done?
 3. Compute the MC integral 100 times, each drawing 1,000 samples, and calculate the 
    mean and median values of the integral. How do the mean and median values compare 
    to the analytical value? Plot a histogram of the 100 integral values.
 4. Estimate the error in your calculation by finding the standard deviation of the 
    integral's value from your 100 trials. How does that error compare to the error 
    estimate by equation 5.80 in _Compuational Physics_ (pg 106)?
 5. _Bonus_: Integrate

    ![equation](https://latex.codecogs.com/png.latex?%5Clarge%20I_%7B1%7D%20%3D%20%5Cint_%7B0%7D%5E%7B2%5Cpi%7D%20%5Csin%28100x%29%20%5Ctextup%7Bd%7Dx)

    How does it compare to your results from Exercise 09?
  
### Exercise 12: N-D Integrals with MC
We discussed on Monday how MC methods can leverage the _mean value theorem_
to calculate an integral. For the simple integral of _f(x) = x<sup>2</sup>_,
a MC method seemed like a poor choice to evaluate the integral: the resulting
value was less accurate than one woud find with a standard integration 
routine and it took about the same amount of time to compute... if not longer!
However, the real power of MC integration methods is when one has an integral
over _N > 2_ dimensions. 

Consider the 10-D integral

![equation](https://latex.codecogs.com/gif.latex?I_%7B10%5Crm%20D%7D%20%3D%20%5Cint_0%5E1%20%5Ctextup%7Bd%7Dx_1%20%5Cint_0%5E1%20%5Ctextup%7Bd%7Dx_2%20%5Ccdots%20%5Cint_0%5E1%20%5Ctextup%7Bd%7Dx_%7B10%7D%5Cleft%28x_1%20&plus;%20x_2%20&plus;%20%5Ccdots%20&plus;%20x_%7B10%7D%20%5Cright%29%5E2)

Your tasks are to:
 1. Calculate how long it would take (in years) to compute this integral
    using the standard limit definition of an integral (i.e., the code you
    wrote last week). Assume your computer can perform 10<sup>6</sup> 
    evaluations of the integrand per second and that you choose a reasonably
    small value for _h_ such that you break each domain up into 100 segments.
    (i.e., _h_ = (b &minus; a) / 100). What if you wanted to break each 
    domain into 1000 segments?
 2. Generalize the mean value theorem to N dimensions, i.e., 
 
    ![equation](https://latex.codecogs.com/gif.latex?%5Cint_a%5Eb%20%5Ctextup%7Bd%7Dx_1%20%5Cint_c%5Ed%20%5Ctextup%7Bd%7Dx_2%20%5Ccdots%20%5Cint_s%5Et%20%5Ctextup%7Bd%7Dx_%7B10%7Df%28x_1%2C%20x_2%2C%20%5Ccdots%2C%20x_%7B10%7D%29%20%5Csimeq%20%28b%20-%20a%29%28d%20-%20c%29%5Ccdots%20%28t%20-%20s%29%5Clangle%20f%5Crangle)
    
    and evaluate the integral I<sub>10D</sub> using a MC method.
 3. Compare your answer to the analytic solution, I<sub>10D</sub> = 155/6.
 4. Evaluate the integral for different sample sizes, starting with something
    unreasonably small (_N = 2_). Plot the relative error of your calculation
    against 1/&radic;N. Describe your results.
 5. How many MC samples did you need to compute a reasonably accurate 
    solution to the integral? How does the time for computation of the MC
    method compare to the brute force, limit definition method?
 6. Up to how many dimensions is it more efficient to use a limit definition 
    method compared to an MC mean value method? 
 7. _Bonus_: At what point does an MC mean value method become more accurate
    than a limit definition method, regardless of computational efficiency?

### Exercise 13: Acceptance &amp; Rejection Methods
For Exercises 11 and 12, we leveraged the _mean value theorem_ to calculate
the value of an integral with a Monte Carlo method. However, we can also
apply the same "stone throwing" technique that we used to compute the value
of &pi; to create a weighted probability distribution that will be useful
if we ever need to draw samples from a distribution that is not uniform 
(i.e., equal probability of all values). 

The basic idea is to select a random point, say (x, y), and see whether
it lies between the function, f(x), and the zero-line (i.e., y = 0). If 
the value lies between the zero line and f(x), you accept the point and 
include it in your final distribution. You reject points that lie above
f(x). This provides a way to compute a integral _and_ create a _probability
distribution function_ (PDF).

Your tasks are to:
  1. Integrate the function f(x) = x<sup>2</sup> between 0 and 10 using 
     a random sampling technique and counting the number of accepted vs
     rejected points. How many samples did you need to draw to get a 
     reasonable estimate of the integral? 
  2. Make a plot showing the rejected points in one color and the accepted
     points in another color.
  3. Do the same for a trickier function: f(x) = sin(x). Integrate it 
     from 0 to 2&pi;. How does your integral compare to the analytical 
     value? Do you think you'll ever be able to calculate the integral 
     to be precisely equal to the analytical value? Explain why or why not.
  4. Now make up a function in one dimension, g(x), and integrate it over
     some domain. Be creative and make something strange! Plot the function 
     and the resulting accepted / rejected points.
  5. Explain how you might use the resulting sample of accepted points to
     create a weighted random sample from a probability distribution. For
     example, if you wanted to select a random point from a Gaussian (i.e., 
     normal) distribution. 



    
