import numpy as np

def numerical_derivative(f,x):
    delta_x = np.exp(-4)
    grad = np.zeros_like(x)

    it = np.nditer(x,flags=['multi_index'], op_flags=['readwrite'])

    while not it.finished:
        idx = it.multi_index
        tmp_val = x[idx]    # numpy 타입은 mutable이므로 원래 값을 저장 해놔야 함

        x[idx] = float(tmp_val) + delta_x
        fx1 = f(x)
        x[idx] = tmp_val - delta_x
        fx2 = f(x)

        grad[idx] = (fx1 - fx2) / (2*delta_x)

        x[idx] = tmp_val
        it.iternext()

    return grad

def func1(input_obj):
    w = input_obj[0]
    x = input_obj[1]
    y = input_obj[2]
    z = input_obj[3]
    return w*x + x*y*z + 3*w + z*(y**2)

input_array = np.array([1., 2., 3., 4.])
print("result: ", numerical_derivative(func1,input_array))