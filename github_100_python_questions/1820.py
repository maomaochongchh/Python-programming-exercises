# -*-coding:utf-8-*-

import math
def bin_search(li, element):
    print(type(element))
    start = 0
    end = len(li)-1
    index =-1
    while start <= end and index == -1:
        mid = int(math.floor((end+start)/2.0))
        if li[mid] == element:
             index = mid
             return index
        elif li[mid] < element:
            start = mid+1
        else:
            end = mid-1

li = range(0,11)
print(bin_search(li,10))