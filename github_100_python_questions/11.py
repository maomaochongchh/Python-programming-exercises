# -*-coding:utf-8-*-

value = []
nums = [num for num in raw_input().split(',')]
for num in nums:
    n = int(num, 2)
    if n % 5 == 0:
        value.append(num)

print(','.join(value))
