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
  




    
