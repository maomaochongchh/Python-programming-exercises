# -*-coding:utf-8-*-

sentence = raw_input()
num_letter = 0
num_num = 0
for i in sentence:
    if i.isdigit():
        num_num = num_num+1
    if i.isalpha():
        num_letter = num_letter+1
print 'LETTERS ', num_letter
print 'NUMS ', num_num