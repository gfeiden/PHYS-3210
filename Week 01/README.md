## Week 01: Introduction to Python & GitHub

This week, we are going to dive into Python, which is the primary programming
language that we will use this semester. Before we do, we need to make sure that
we have all of the necessary software and/or user accounts to begin our work.

**User Accounts**:
 - [GitHub](https://github.com) (if you do not already have one)

**Software**:
 - [Anaconda Python Distribution](https://www.anaconda.com/distribution/) (w/ Spyder, NumPy, SciPy, Matplotlib, VPython)
 - [GitHub Desktop](https://desktop.github.com/)

### Readings
 1. Chapter 1, _Physical Modeling_ (Monday, in class)
 2. Chapter 2, _Physical Modeling_ (by Wednesday)
 3. Chapter 3, _Physical Modeling_ (Wednesday, in class)
 4. Handout (by Friday)
 5. Chapter 4, _Physical Modeling_ (by Friday)

### Preliminaries

Create an account on [GitHub](https://github.com), if you do not already have one.
GitHub is a software version control platform that keeps a record of changes you
make to software project and stores your files in the cloud. We'll talk more about
version control and managing your work with GitHub this week.

__*Working on Campus Computer*__

Download and install GitHub Desktop. This will allow you to learn
and manage your files on GitHub more easily on a Windows PC.

__*Working on Own Computer*__

Download and install [Anaconda](https://www.anaconda.com/distribution/) and
[GitHub Desktop](https://desktop.github.com/).

### Exercise 1: Debugging

Open `Exercise_01.py` after following along with Chapter 1 (see above). You may
either open the exericse directly in GitHub, or you may download the python
_script_ and open it using Spyder.

The code is supposed to compute the hypotenuse of a triangle using NumPy's square
root function for a triangle with sides *a* = 3 units and *b* = 4 units. It then
prints out the values of the hypotenuse (side *c*) to the screen. Unfortunately,
your colleague (\*\**cough*\*\* me \*\**cough*\*\*) wrote a code filled with *bugs*, i.e.,
errors that prevent the script from running properly. They have asked you to help
them fix their code. __Your job is to find each bug and write a short report for
your colleague explaining (1) where there's an error, (2) why it's an error,
and (3) how to fix the error.__

Before you do anything else, write down what you expect the hypotenuse should be
equal to after the script finishes. [no calculator required] Next, read over the
code line-by-line and make sure you agree with what your colleague has done.
You can also open Spyder and start entering the code line-by-line into the
IPython console. Once you have identified each error in the code, write up your
report and submit it by opening an Issue on GitHub. [Advanced] Edit the script,
upload it to your repository, and create a pull request.

Finally, answer the following question:

> Why does the value for c have a decimal, while the values for a and b do not?
Explain.

You are now ready for Chapter 2!

### Exercise 2: Find a Star's Mass

Open `Exercise_02.py` after following along with the tutorial presented
in Chapter 2. You may either open the file directly in GitHub, or download
the script to open with Spyder.

Your job is to complete the code so that it properly reformats the input
data (loaded from a file) to recover the original walker chains, assess
whether the chains converge on a single answer, and then estimate the
mass for the star DS Tuc A. This might sound like jibberish, so read the
information presented in `Exercise_02.py`. Your instructor will also give
a quick introduction to the general concepts to provide some clarity and
context.

This data was used to find the mass of DS Tuc A (and similarly for DS Tuc B),
which was discovered to host a young exoplanet.
([Newton et al. 2019](https://arxiv.org/abs/1906.10703))

### Exercise 3: Summing Series
A common way to determine the value of a function is to sum over an infinite 
series. For example, the Maclaurin series for sin(x) is 

![equation](https://latex.codecogs.com/gif.latex?%5Csin%28x%29%20%3D%20x%20-%20%5Cfrac%7Bx%5E3%7D%7B3%21%7D%20&plus;%20%5Cfrac%7Bx%5E5%7D%7B5%21%7D%20-%20%5Cfrac%7Bx%5E7%7D%7B7%21%7D%20&plus;%20%5Ccdots).

Perform a series expansion to derive the equation above. Next, write down 
a general expression for the sum of the series that is valid 
between _n_ = 0 and _n_ = _N_, where _N_ ≥ 0. This will serve as your 
_algorithm_ for summing the series on your computer.

One problem with the algorithm is that we do not know which value
of _N_ is suitable for calculating the series' sum. Instead of guessing, 
have your code compute the partial sum until the _N_<sup>th</sup> term 
contributes a negligible amount to the partial sum, say 1 part in 
10<sup>8</sup>. When the correction is below this threshold, we say the
code has achieved _numerical convergence_.

Before writing any lines of code, discuss an approach with your neighbor
and write out on paper how your code should proceed. Code up your 
approach in Spyder once you're done. 

Here are your tasks:

   1. Perform a Maclaurin series expansion of the function sin(_x_) to 
      derive the equation above. 
   2. Derive a generalized, finite summation form for the series based 
      on your Maclaurin series expansion.
   3. Discuss with your neighbor about how to approach coding the problem
      and write out on paper how you code should proceed. 
   4. Code your approach in Spyder once you are finished.
   5. Show that, for small values of _x_, the algorithm converges and that
      it converges to the correct value by comparing your results to the
      value determined using NumPy's sine function.
   6. Which value for _N_ was required to reach the desired precision
      to obtain numerical convergence for small values of _x_?
   7. Steadily increase _x_ and write down the relative error between your
      calculated value for sin(_x_) and the NumPy function's value. 
   8. What do you notice about the relative error?
   9. Will there be a time when the series does not numerically converge? 
      Make a figure or two from the data you generate to support your 
      conclusion.
  10. **_Challenge_** Modify your algorithm to be valid for any value of _x_.

### Weekly Problem 01

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

**_Challenge_**: Write a function to compute the viral load for a given set
of parameters (`A`, `B`, `alpha`, `beta`). Produce figures for assignment 
part b using your function.
