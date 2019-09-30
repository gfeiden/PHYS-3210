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

### Lab 04: Masses on a String




    
