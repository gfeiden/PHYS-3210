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
 1. Handout (by Friday, 23 Aug 2019)

### Preliminaries

Create an account on [GitHub](https://github.com), if you do not already have one. 
GitHub is a software version control platform that keeps a record of changes you
make to software project and stores your files in the cloud. We'll talk more about
version control and managing your work with GitHub this week.

__*Working on Campus Computer*__

Download and install GitHub Desktop on your P-Drive. This will allow you to learn 
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

You're now ready for Chapter 2!

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

![equation](https://latex.codecogs.com/gif.latex?%5Csin%28x%29%20%3D%20x%20-%20%5Cfrac%7Bx%5E3%7D%7B3%21%7D%20&plus;%20%5Cfrac%7Bx%5E5%7D%7B5%21%7D%20-%20%5Cfrac%7Bx%5E7%7D%7B7%21%7D%20&plus;%20%5Ccdots)

Problem 2.5 from Landau+

### Weekly Problem 01

Read the handout prior to class on Friday. Try to understand the derivation
of Equation 4. Then, complete problem 5.1 (First Computer Lab: HIV Example)
in Physical Modeling. In addition, answer the following questions:

_Challenge_: Write a function to compute the viral load for a given set
of parameters (`A`, `B`, `alpha`, `beta`) and produce figures for 
assignment part b using your function.


