## Week 04: Differentiation &amp; Integration

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
    
    
    
    
    
    
