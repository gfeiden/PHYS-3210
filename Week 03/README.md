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

### Exercise 06: Random Walking
The file `Exercise_06.py` contains a function that simulates a 2D random 
walk. That is, the code simulates a point that starts at the origin and 
takes steps in the _x_ and _y_ directions in random directions and with
random step sizes between 0 and 1 unit distance. 

Use the code provided to guide you through the following taks.
 1. Annotate the code to explain what is happening at each line in the 
    code.
 2. In a single figure, plot the results for a few random walkers that 
    take 1000 steps. Be sure to label your axes appropriately. Write a 
    short paragraph or two describing whether the results look like what 
    you would expect from a _random_ walk. Reference the data in your 
    figure as evidence.
 3. For a single walker, calculate how far the walker moved from the 
    origin after 1000 steps. [hint: **not** the total distance traveled,
    but the final distance from the origin] Do you expect every walker to
    end up the same distance from the origin?
 4. Run 100 simulations for a walker that takes _N_ steps (you choose _N_).
    For each walker, calculate the final distance from the origin. [hint:
    you should have a list or an array of final distances] Does each 
    walker end up the same distance from the origin? Is this what you 
    expected?
 5. Make a histogram of the final distances and find the average distance,
    the standard deviation, and the median distance. Describe the distribution
    of final distances. Is this what you expected? Explain why it makes 
    sense and explain what it tells you about your results.
 6. Describe a physical scenario where this type of simulation might be 
    a useful model for reality. [note: do not use the scenario described 
    in the handout]
 6. _Challenge_: Expand your simulations to 3 dimensions and describe how
    your results for part 5 change.

