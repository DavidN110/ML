import numpy as np

def vector_function(x, y):
    """
    Make sure vector_function can deal with vector input x,y 
    """
    print(x,y)
    if x.all()>y.all():
        return print(x/y)
    else:
        return print(x*y)
    raise NotImplementedError

x=np.random.randint(low=30, high=60, size=10)
y=np.random.randint(low=30, high=60, size=10)
vector_function(x,y)