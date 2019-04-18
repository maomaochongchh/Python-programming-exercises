# -*-coding:utf-8-*-

def PutNumber(n):
    i=0
    while i < n:
        j = i
        i = i+1
        if j%7 ==0:
            yield j

for a in PutNumber(100):
    print(a)
