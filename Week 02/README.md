## Week 02: More Advanced Python

### Readings
 1. Handout (by Monday)
 2. Chapter 4, _Physical Modeling_ (by Monday)
 3. Sections 6.1 &ndash; 6.4, _Physical Modeling_ (by Wednesday)

### Weekly Problem 01: HIV Lab

Read the handout prior to class on Friday. Try to understand the derivation
of Equation 4. Before you begin, derive Equation 4 from the reading and 
explain in detail your reasoning for each step of the derivation.

Next, complete Problem 5.1 (First Computer Lab: HIV Example) in Physical 
Modeling. In addition, answer the following questions:

 1. What were the key assumptions made in the derivation and in your 
    approach to solving the problem that made the problem tractable? 
 2. What would be the consequences of relaxing the assumptions listed
    in question 1? How might your approach to solving the problem change?
 3. How did the two limiting cases help simplify the problem?

Please upload your answers to these questions and your code to GitHub
by Friday, 30 August 2019.

~~**_Challenge_**: Write a function to compute the viral load for a given set
of parameters (`A`, `B`, `alpha`, `beta`). Produce figures for assignment 
part b using your function.~~

### Exercise 04: Make Your (Coding) Life Easier

Write a function to compute the viral load for HIV after administering 
an antiretroviral drug (Problem 5.1 in text; Week 1, Problem 1). The 
function should accept values for `A`, `B`, `alpha`, `beta`, and `time` 
as input and return the viral load, V(t).

Using your function, plot the function for a different combinations of 
`A` and `alpha` (fix `B` and `beta` as you did in Problem 5.1). Add axis
labels, a plot title, and a legend with unique labels for each plotted
curve. Save the figure as a PDF or other image file, add it to a Word 
document, and describe how adjusting `A` and `alpha` change the function's 
properties. Be sure to reference your figure and describe each change
in detail. 

Upload your write up and code to GitHub.

### Weekly Problem 02: Projectile Motion
Imagine launching a ball with some device (a cannon, a spring, your arm)
that gives the ball an initial velocity, **_v_**, at some angle with respect
to the ground. Write a function that integrates the 2D equations of motion 
to compute the ball's trajectory and its velocity over time. Assume that 
air exerts a drag force on the ball along a given direction of motion that 
is proportional to the object's velocity squared, i.e., 

![equation](https://latex.codecogs.com/gif.latex?%5Clarge%20F_%7BD%2C%5Chat%7B%5Cj%7D%7D%20%3D%20c%5Ccdot%20v_%7B%5Chat%7B%5Cj%7D%7D%5E2)

Your function should accept the ball's mass, initial position, velocity, and launch
angle as input. The drag coefficient, time step size, and acceleration 
due to gravity are optional inputs. After computing the trajectory, the 
function should return the _x_ and _y_ positions, the _x_ and _y_ velocities, 
and the time.

With your function, you should
 1. Verify your code works properly by computing the trajectory for some
    initial launch velocity and angle, but without air resistance. Find
    the total distance travelled and total time of flight and compare with
    an analytical solution (i.e., pencil &amp; paper).
 2. Predict what will happen when you add air resistance.
 3. Compare your results without drag to those with drag (i.e., air
    resistance). A reasonble value for the drag coefficient in the above
    equation for a sphere moving through air is 2 x 10<sup>&ndash;3</sup> 
    kg/m. Plot the ball's height vs distance travelled for each case.
 4. Write up your results and describe the effect of air resistance.
 5. Find the terminal velocity of the ball [hint: you may need to change 
    your initial launch conditions].
 6. Play around with the inputs. Change the acceleration due to gravity. 
    Explore your simulation and perform an experiment that you find interesting.
 7. Try to break your code and describe what you had to do to break it 
    (i.e., without changing your code, give it input that you think will
    return a non-physical answer).

Write up your results (including plots) and push your code and paper to 
to GitHub.


