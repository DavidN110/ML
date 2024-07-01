import random
import numpy as np

def randomization(n):
    """
    Arg:
    n - an integer
    Returns:
    A - a randomly-generated nx1 Numpy array.
    """
    #Your code here
    A = []
    for i in range(0,n):
        a=random.randint(0,100)    
        A.append(a)
    return print(A)
m = int(input())
randomization(m)