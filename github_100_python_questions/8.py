# -*-coding:utf-8-*-

words = [w for w in raw_input().split(',')]
# print(words)
words.sort()
print(','.join(words))