import numpy as np

def norm(A, B):
    """
    Takes two Numpy column arrays, A and B, 
    and returns the L2 norm of their
    sum.

    Arg:
      A - a Numpy array
      B - a Numpy array
    Returns:
      s - the L2 norm of A+B.
    """
    S = A + B
    s = np.linalg.norm(S)
    return print(s,S)
    raise NotImplementedError

A=np.random.random((5,1))
B=np.random.random((5,1))
norm(A,B)
