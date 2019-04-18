# -*-coding:utf-8-*-

input = list(raw_input().split(','))
# print(input)
rowNum = int(input[0])
colNum = int(input[1])
arr = [[0 for i in range(colNum)] for j in range(rowNum)]
# print(arr)
for i in range(rowNum):
    for j in range(colNum):
        arr[i][j] = i*j

print(arr)