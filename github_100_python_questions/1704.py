# -*-coding:utf-8-*-

n = int(raw_input())
def f(n):
    i = 0
    while i < n+1:
        if i%2 == 0:
            yield i
        i = i+1

output = f(n)
values = []
for i in output:
    values.append(str(i))
print(",".join(values))
