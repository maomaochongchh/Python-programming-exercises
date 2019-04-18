# -*-coding:utf-8-*-

def dict(x):
    dict = {}
    for i in range(1, x+1):
        dict[i] = pow(i, 2)
    return dict

x = int(raw_input())
y = dict(x)
print(y)