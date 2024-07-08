import numpy as np
def neural_network(inputs, weights):
    """
     Takes an input vector and runs it
     through a 1-layer neural network
     with a given weight matrix and returns the output.

     Arg:
       inputs - 2 x 1 NumPy array
       weights - 2 x 1 NumPy array
     Returns (in this order):
       out - a 1 x 1 NumPy array, 
       representing the output of the neural network
    """
    S = inputs*weights
    s = np.linalg.norm(S)
    return print(s,S)
    raise NotImplementedError


inputs=np.random.random((2,1))
weigths=np.random.random((2,1))
neural_network(inputs,weigths)