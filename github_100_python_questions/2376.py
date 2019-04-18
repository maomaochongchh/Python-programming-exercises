# -*-coding:utf-8-*-

i=0
while i>=0:
    if i>35:
        print('No solution')
    if 4*i+2*(35-i) == 94:
        print(i, (35-i))
        break
    else:
        i +=1