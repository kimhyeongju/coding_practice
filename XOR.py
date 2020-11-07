from LogicGate_class import *
import numpy as np

xdata = np.array([[0,0],[0,1],[1,0],[1,1]])
tdata = np.array([0,1,1,0])

XOR_obj = LogicGate("XOR_GATE",xdata,tdata)

print(XOR_obj.name,'\n')

for input_data in xdata:
    sigmoid_val, local_val = XOR_obj.predict(input_data)
    print(input_data, '=', local_val, '\n')
