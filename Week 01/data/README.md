# Data Files for Week 01

All data is provided by Kinder &amp; Nelson via the webpage for A Student's Guide to Python. [LINK](http://physicalmodelingwithpython.blogspot.com/p/data-sets.html)

## HIV Example Data

HIV infection time course.

File HIVseries.mat contains a single variable `a` with two columns of data.  The
first is the time in days since administration of a treatment to an HIV positive
patient; the second contains the concentration of virus in that patient's blood,
in arbitrary units.

HIVseries.csv and HIVseries.npy contain the same data in the same format.
HIVseries.npz contains the same data in two separate arrays called
`time_in_days` and `viral_load`.

Data from A. Perelson. [Modelling viral and immune system dynamics](https://www.ncbi.nlm.nih.gov/pubmed/11905835). Nature Revs. Immunol. (2002) vol. 2 (1) pp. 28--36 (Box 1).

## Baceterial Example Data

Novick/Weiner data for protein folding.
  
g149novickA.mat is data from their Fig. 1 (high inducer).
    Column 1:   Time in hours. The e-folding time was about 3 hours.
    Column 2:   Fraction of maximum beta-galactosidase activity.

g149novickB.mat is data from their Fig. 2 (low inducer).
    Column 1:   Time in hours. The e-folding time was about 3 hours.
    Column 2:   Fraction of maximum beta-galactosidase activity.

g149novickA.txt, g149novickA.npy, g149novickB.txt, and g149novickB.npy contain
the same data.

novick.npz:
    Both data sets in a single file.

Novick and Weiner. [Enzyme induction as an all-or-none phenomenon](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC528498/).
Proc Natl Acad Sci USA (1957) vol. 43 (7) pp. 553--66.
