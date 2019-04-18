# -*-coding:utf-8-*-

stopword = ''
items = []
output = []
for item in iter(raw_input, stopword):
    items.append(item)
items.sort()
for item in items:
    output.append(tuple(item.split(',')))
print(output)
# from operator import itemgetter, attrgetter
# l = []
# while True:
#     s = raw_input()
#     if not s:
#         break
#     l.append(tuple(s.split(",")))
#
# print sorted(l, key=itemgetter(0,1,2))