import numpy as np

def scalar_function(x, y):
    """
    Returns the f(x,y) defined in the problem statement.
    """
    if x>y:
        return print(x/y)
    else:
        return print(x*y)
    raise NotImplementedError

x=int(input())
y=int(input())

scalar_function(x,y)