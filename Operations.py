import numpy as np

def operations(h, w):
    """
    Takes two inputs, h and w, and makes two Numpy arrays A and B of size
    h x w, and returns A, B, and s, the sum of A and B.

    Arg:
      h - an integer describing the height of A and B
      w - an integer describing the width of A and B
    Returns (in this order):
      A - a randomly-generated h x w Numpy array.
      B - a randomly-generated h x w Numpy array.
      s - the sum of A and B.
    """
    A = np.zeros((h,w))
    B = np.zeros((h,w))

    for i in range(h):
        for j in range(w):
            A[i,j]=np.random.randint(0,100)
            B[i,j]=np.random.randint(0,100)
    s= A + B
    return print(A, B, s)
    raise NotImplementedError
    

h=int(input())
w=int(input())
operations(h,w)