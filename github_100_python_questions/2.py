# -*-coding:utf-8-*-

def fact(x):
    y = 1
    for i in range(1,x+1):
        y = y*i
    return y

def fact_ans(x):
    if x == 0:
        return 0
    return x*fact_ans(x-1) #yao xue hui yong di gui

x =  raw_input()
y = fact(int(x))
print(y)