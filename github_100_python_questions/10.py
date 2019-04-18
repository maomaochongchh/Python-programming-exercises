# -*-coding:utf-8-*-

words = [word for word in raw_input().split(' ')]
words = list(set(words))
words.sort()
print(' '.join(words))