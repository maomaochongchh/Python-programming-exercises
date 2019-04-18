# -*-coding:utf-8-*-

numbers = raw_input()
list_num = numbers.split(',')
output =[]
for i in list_num:
    if int(i)%2!=0:
        output.append(i)
print(','.join(output))