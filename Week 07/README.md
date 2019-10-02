## Week 07: Matrix Computing

### Readings
From _Computational Physics_:
 1. Section 6.1 &ndash; 6.3 (by Wednesday)
 2. Section 6.6 (by Friday)
 3. Section 6.4 &ndash; 6.5 (Optional)

### Exercise 14: Linear Algebra Routines
Quite often, physical systems are modeled by simultaneously solving a 
set of equations (_N_ equations for _N_ unknowns). While it may be trivial
to solve a small number equations analytically, it doesn't take long for
such problems to become intractable. To solve problems like this, of any
dimension, it's advantageous to write the system of equations in matrix
form and use linear algebra methods to find a solution.

Before we get into solving a more complicated problem (Lab 04), it's best
to get familiar with different linear algebra methods available to you. 
Matrices are implemented in Python using the `list` type or, more importantly,
using the NumPy `array` type. NumPy has a library of linear algebra routines,
called `linalg`,
(optimized for speed and accuracy) that can be used to perform basic 
linear algebra procedures. Some of these are listed in Table 6.1 in your 
book, but the full list of routines can be found on the `linalg` 
![documentation webpage](https://docs.scipy.org/doc/numpy/reference/routines.linalg.html).

To get familiar with the `linalg` package and working more closely with 
arrays, complete the exercises in Section 6.6.

### Lab 04: Masses on a String (Problem 3: N-D Newton Raphson)
Two weights, _W_<sub>1</sub> = 10 N and _W_<sub>2</sub> = 20 N, are hung 
from three pieces of string with lengths _L_<sub>1</sub> = 3 dm, 
_L_<sub>2</sub> = _L_<sub>3</sub> = 4 dm and a horizontal bar _L_ = 8 dm,
as shown in Figure 6.1 (in your book). 

Your tasks are to:
 1. Write down the relevant equations for static equilibrium (see your 
    book for guidance).
 2. Come up with a first guess for each of the unknown parameters in the
    problem (tensions &amp; angles). Discuss with your neighbor and your
    professor how you came up with your initial guess.
 3. Find the angles assumed by the strings and the tensions exerted by 
    the strings.
 4. Discuss whether your solution is physically reasonable. For example, 
    check that the tensions are positive and that the inferred angles 
    correspond to a realistic geometry (i.e., make a sketch). Compare the 
    string tensions to the weights. Do they appear to be reasonable?
 5. See at what point your initial guess for the string angles is so bad 
    that the computer cannot find a physical solution.
 6. Change the weights and string lengths. Test whether you are able to
    find a solution. Make a few plots to explore the dependency between
    different variables. Were there any surprising dependencies that you
    uncovered? Explain why or why not.
 7. _**Challenge**_ Solve the same problem, but with three masses and 4
    lengths of string.





    
