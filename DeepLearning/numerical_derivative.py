import numpy as np
def numerical_derivative(f,x):
    delta_x = np.exp(-4)
    return (f(x + delta_x) - f(x - delta_x)) / (2*delta_x)

def func1(x):
    return 3*x*np.exp(x)

print("result= ", numerical_derivative(func1,3))
