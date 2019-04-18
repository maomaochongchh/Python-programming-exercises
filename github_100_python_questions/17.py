# -*-coding:utf-8-*-

# stopword = ''
# str = ''
# output = 0
# for line in iter(raw_input, stopword):
#   str += line + '\n'
# a = str.split('\n')
# a = a[:-1]
# for line in a:
#     b = line.split(' ')
#     if b[0] == 'D':
#         output += int(b[1])
#     else:
#         output -= int(b[1])
# print(output)


netAmount = 0
while True:
    s = raw_input()
    if not s:
        break
    values = s.split(" ")
    operation = values[0]
    amount = int(values[1])
    if operation == "D":
        netAmount += amount
    elif operation == "W":
        netAmount -= amount
    else:
        pass
print netAmount