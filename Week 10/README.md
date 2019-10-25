## Week 10: Ordinary Differential Equations &ndash; Non-linear Oscillations

### Readings
From _Computational Physics_:
 1. Section 8.4 &amp; 8.5 (by Wednesday)
 2. Section 8.6 &amp; 8.7 (by Friday)

### Exercise 19: Anharmonic Oscillation with Euler's method
_Based on Problem in Section 8.8 in Computational Physics_

Use Euler's method to solve for an anharmonic oscillator's motion that 
is subject to the spring potential

![equation](https://latex.codecogs.com/png.latex?V%28x%29%20%3D%20%5Cfrac%7B1%7D%7Bp%7Dkx%5E%7Bp%7D%5C%20%5Ctextrm%7B%20%28even%20%7Dp%29.)

Do not introduce time-dependent external forces, yet. Explore solutions 
using different values for the exponent _p_ between 2 and 12. 

 1. If _p = 2_, do you get a result that you expect? Explain.

 2. Check that the solution remains periodic with constant amplitude and
    period fo ra given initial condition, regardless of how non-linear 
    you make the force.
 
 3. Where is along it's path does the oscillating mass have the highest
    velocity? Does this make physical sense? Explain. (if it doesn't make
    sense, go back and check your work!)
 
 4. Verify that nonharmonic oscillators are _nonisochronous_, that is, vibrations
    with different amplitudes have different periods. 

### Exercise 20: Anharmonic Oscillation with RK2
Use a second-order Runge-Kutta method (RK2) to solve for the motion of 
the same anharmonic oscillator in Exercise 19. Compare your results with
those from Euler's method and explore different step sizes using each method.
What do you observe?

### Exercise 21: Energy Conservation
_Problem 8.8.1 in Computational Physics_

Use your RK2 program for the anharmonic oscillator to investigate several
of the oscillator's properties and your algorithm's properties.
 1. Construct a graph of the inferred period of oscillation as a function
    of initial amplitude.
 
 2. Verify that the motion is oscilatory, but not harmonic, for _p > 6_.
 
 3. Plot the potential energy PE(_t_) = _V_[_x(t)_], the kinetic energy,
    and the total energy versus time for 50 periods. Comment on the correlation
    between the potential and kinetic energy. How does it depend on the 
    potential's free parameters (i.e., _p_)?
  
 4. Check the long-term _stability_ of your solution by plotting
 
    ![equation](https://latex.codecogs.com/png.latex?-%5Clog_%7B10%7D%5Cleft%7C%20%5Cfrac%7BE%28t%29%20-%20E%28t%3D0%29%7D%7BE%28t%3D0%29%7D%20%5Cright%7C)
    
    for a large number of periods. Because _E(t)_ should be independent 
    of time (no dissipative forces), the numerator is the absolute error
    in your solution and, when divided by _E(0)_ becomes the relative 
    error. Try to acheive a relative error of about 1 part in 10<sup>11</sup>.
    
 5. Because a particle bound by a large-_p_ oscillator is essentially 
    "free" most of the time, you should observe that the time average of 
    its kinetic energy exceeds the time averaged potential energy. Show
    that your solution obeys the Viral Theorem:
    
    ![equation](https://latex.codecogs.com/png.latex?%5Clangle%20KE%20%5Crangle%20%3D%20%5Cfrac%7Bp%7D%7B2%7D%20%5Clangle%20PE%20%5Crangle)
    
    
