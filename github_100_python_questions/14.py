# -*-coding:utf-8-*-

sentence = raw_input()
upper = 0
lower = 0
for i in sentence:
    if i.isupper():
        upper = upper+1
    if i.islower():
        lower = lower+1
print 'UPPER CASE ', upper
print 'LOWER CASE ', lower