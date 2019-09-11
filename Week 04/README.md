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

### Lab 03: Self-Avoiding Random Walks, pt 1
Proteins are large molecules made from a series of smaller molecular chains
called _monomers_. These monomers can be nonpolar hydrophobic monomers 
that are repelled by water molecules or polar monomers that are attracted
by water. By stringing together nonpolar and polar monomers, we can build
a protein. However, as with most things, nature strives to create monomer
chains that minimize the chain's energy. This is acheived by folding the
protein in such a way so as to maximize the number of unconnected nonpolar
monomer neighbors.

Your tasks are to:
 1. modify your random walk program, `Exercise_06.py`, so that it can produce a randomly 
    folded chain of monomers. Assume that each monomer has a fixed length 
    (unit length = 1) and that each monomer can, at most, be connected to 
    two other monomers. In other words, we want our random walker to move 
    on a 2D lattice in such a way that it cannot connect to a location where 
    it has previously been; there are at most three possible locations for 
    the walker to move. Once the walker reaches a location where it cannot
    step any further (i.e., it's surrounded by other monomers), the simulation
    ends and you've finished building your protein. **Carefully devise a 
    plan with a partner, or partners, and write pseudocode for executing 
    this plan**.
 2. At the end of each step, randomly decide whether the monomer was a 
    nonpolar or polar monomer, with a weighting such that nonpolar monomers
    are more likely than polar monomers. 
 3. Record the chain's length.
 4. Visualize the resulting chain.

### Lab 03: Self-Avoiding Random Walks, pt 2
We're going to continue working with your self-avoiding random walk 
program to build proteins. 

Your tasks are to:
 1. Calculate the chain's energy, _E = &minus;&epsilon; &#8729; f_, where _&epsilon;_ is some constant
    (e.g., _&epsilon; = 1_) and _f_ is the number of nonpolar monomers that are neighbors,
    but that are **_not_** connected. Record this value along with the 
    chain's length.
 2. Run a reasonably large number of simulations and save the output from
    each (i.e., simulation number, chain length, energy, number of folds). 
    Bonus: save the full walk for each chain so that you can visualize them 
    later.
 3. Determine how the lowest energy for each chain depends on the chain
    length. Compare your results to those from more sophisticated simulations
    by researching similar results using other methods (e.g., molecular 
    dynamics) or by finding results for real protein structures.
 4. Write about the successes and (possible) failures of your model. Use
    figures and visualizations to support your arguments.
 5. _Challenge_: Extend your results to 3D. Only do this once you have 
    completed every other step and written up your results.

