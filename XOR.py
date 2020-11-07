from LogicGate_class import *
import numpy as np

xdata = np.array([[0,0],[0,1],[1,0],[1,1]])
tdata = np.array([0,1,1,0])

# 다음은 error가 줄지 않아 잘못된 결과를 예측
"""
XOR_obj = LogicGate("XOR_GATE",xdata,tdata)
XOR_obj.train()

print(XOR_obj.name,'\n')

for input_data in xdata:
    sigmoid_val, logical_val = XOR_obj.predict(input_data)
    print(input_data, '=', local_val, '\n')
"""

# AND(NAND,OR)로 구현
NAND_obj = LogicGate("NAND_GATE", xdata, np.array([1,1,1,0]))
NAND_obj.train()
OR_obj = LogicGate("OR_GATE", xdata, np.array([0,1,1,1]))
OR_obj.train()
AND_obj = LogicGate("AND_GATE", xdata, np.array([0,0,0,1]))
AND_obj.train()

s1 = []     # NAND
s2 = []     # OR
new_input_data = [] # AND
final_output = []

for index in range(len(xdata)):
    s1 = NAND_obj.predict(xdata[index])
    s2 = OR_obj.predict(xdata[index])

    new_input_data.append(s1[-1])
    new_input_data.append(s2[-1])

    sigmoid_val, logical_val = AND_obj.predict(np.array(new_input_data))

    final_output.append(logical_val)
    new_input_data = []

print("XOR GATE")

for index in range(len(xdata)):
    print(xdata[index], ' = ', final_output[index], end='')
    print('\n')


