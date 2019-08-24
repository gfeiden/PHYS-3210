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
Write a function that returns a projectile's trajectory for a given set 
of initial data (_x_ &amp; _y_ position, _x_ &amp; _y_ velocity). Ignore 
air resistence, for now.

Modify your equations and code to include the effects of drag on the 
projectile. Assume the drag force along a given direction of motion is 
proportional to the object's velocity squared, i.e.,

![equation](https://latex.codecogs.com/gif.latex?%5Clarge%20F_%7BD%2C%5Chat%7B%5Cj%7D%7D%20%3D%20c%5Ccdot%20v_%7B%5Chat%7B%5Cj%7D%7D%5E2)


