# -*-coding:utf-8-*-

input_str = raw_input()
words = input_str.split(' ')
output = {}
for word in words:
    num = words.count(word)
    output[word] = num
words = output.keys()
words.sort()
for word in words:
    print('{}:{}'.format(word, output[word]))
