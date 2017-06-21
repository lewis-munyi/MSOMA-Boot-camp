import functools

from functools import reduce

mylist = [1,4,3,2,2]

def mysum(x,y):
    return x * y

print (reduce(mysum,mylist))