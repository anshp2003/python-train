from functools import reduce

list1=[1,2,23,5,6,58]
mul=reduce(lambda x,y:x*y,list1)
print(mul)