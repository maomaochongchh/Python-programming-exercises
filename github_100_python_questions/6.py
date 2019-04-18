# -*-coding:utf-8-*-
import numpy as np

def formula(x):
    x = x.split(',')
    y = []
    for i in x:
        i = int(i)
        y.append(int(np.sqrt((float(2*i*50)/30.0))))
    return y


x = raw_input()
output = formula(x)
print(','.join(str(i) for i in output))

