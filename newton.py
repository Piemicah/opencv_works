import numpy as np

def f(x):
    return (2*x/3 - np.sin(x))

def df(x):
    return (2/3 - np.cos(x))

x0 = 0.061
for i in range(20):
    x1 = x0 - f(x0)/df(x0)
    print("x",i," = ",x0,": f(",x0,") = ",f(x0),": f'(",x0,") = ",df(x0))
    x0 = x1

