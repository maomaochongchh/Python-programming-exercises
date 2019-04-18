# -*-coding:utf-8-*-

pw_list = [x for x in (raw_input()).split(',')]

output = []
for str in pw_list:
    lower = 0
    digit = 0
    upper = 0
    chareacter = 0
    if len(str) >=6 and len(str) <=12:
        for i in str:
            if i.islower():
                lower += 1
            elif i.isupper():
                upper += 1
            elif i.isdigit():
                digit += 1
            elif i == "$" or i =="#" or i =="@":
                chareacter += 1
            else:
                break
    else:
        continue
    if lower and digit and upper and chareacter:
        output.append(str)
print(','.join(output))