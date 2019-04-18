# -*-coding:utf-8-*-

lines = []
while True:
    s = raw_input()
    if s:
        lines.append(s)
    else:
        break

for line in lines:
    line = line.upper()
    print(line)