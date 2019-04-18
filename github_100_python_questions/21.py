# -*-coding:utf-8-*-

import math
stopword = ''
strs = []
for str in iter(raw_input, stopword):
    strs.append(str)
start = [0,0]
end =[0,0]
for str in strs:
    str = str.split(' ')
    if str[0] == 'UP':
        end[1] += int(str[1])
    elif str[0] == 'DOWN':
        end[1] -= int(str[1])
    elif str[0] == 'RIGHT':
        end[0] -= int(str[1])
    else:
        end[0] += int(str[1])

print(int(round(math.sqrt(end[0]**2+end[1]**2))))