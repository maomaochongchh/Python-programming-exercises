# -*-coding:utf-8-*-

nums =[]
for i in range(1000, 3001):
    i = str(i)
    if int(i[0]) % 2 == 0 and int(i[1]) % 2 == 0 and int(i[2]) % 2 == 0 and int(i[3]) % 2 == 0:
        nums.append(i)

print(','.join(nums))