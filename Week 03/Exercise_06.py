#
import numpy as np
import numpy.random as rand
import matplotlib.pyplot as plt

def walk(N):
    """ Function to compute an N-step random walk
    
        Input:
            N  ::  Total number of steps

        Output:
            x  ::  Array of all x positions
            y  ::  Array of all y positions

    """
    # seed random number generator
    rand.seed()

    # initialize x, y
    x = [0.0] 
    y = [0.0]

    # step in x-y space N times
    for n in range(N):
        x.append(x[-1] + (rand.random() - 0.5)*2.0)
        y.append(y[-1] + (rand.random() - 0.5)*2.0)
    
    return np.array(x), np.array(y)


# Example simulation
walker_1 = walk(1000)   # compute path for 1000 steps

# Example plot of (x, y) pairs from example simulation 
plt.plot(walker_1[0], walker_1[1], '-')
plt.xlabel("X")
plt.ylabel("Y")
plt.show()

