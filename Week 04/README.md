## Week 04: Monte Carlo Methods

### Readings
From _Computational Physics_:
 1. Sections 4.1 &amp; 4.2 (by Monday)
 2. Sections 4.3 &amp; 4.4 (by Wednesday)
 3. Sections 4.5 &amp; 4.6 (by Friday)

### Exercise 07: Is it Random?
When using a random number generator, it is always good practice to verify
that the sequence of numbers produced by the routine appear to be random. 
Essentially, you want to verify whether there are any _noticable_ correlations
among the data.

Use the `powerResidue` function in `rand.py` to accomplish these tasks:
 1. Generate a sequence of random numbers. Familiarize yourself with the 
    function's input, which might require reviewing Section 4.2 in your 
    book. 
 2. Print out the random sequence. How does the list appear to you?
 3. Try changing the seed value and the constants used in the code to 
    produce a random sequence that repeats itself. (use your book as a guide).
 3. Plot your sequence of random numbers against the list index (i.e., 0, 
    1, 2, ..., N). Do you notice any obvious patterns? 
 4. Generate a few sequences of equivalent length, _N_. Print them and 
    plot them (in the same figure). What do you notice about the sequences?
 5. If there are any noticeable correlations, devise a simple way to fix
    the problem and make the changes to the code. Repeat part 4.
 6. Create a scatter plot with random (x, y) coordinates using our 
    `powerResidue` function and using NumPy's `random` function. How do
    they compare when you use the default values for constants and the 
    seed for `powerResidue`?
 7. _Challenge_ Perform randomness tests by determining either the k-th
    moment of the distribution of points or by performing a nearest-neighbor
    correlation test to find the correlation coefficient. Compare your 
    results with the expected values. (see pg 74 in your book)
    
Write up the results of each part, including figures, and push your 
document to GitHub.

### Exercise 08: Self-Avoiding Random Walks

### Lab 03: Spontaneous Decay
