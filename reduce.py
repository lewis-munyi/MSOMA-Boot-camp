import functools

from functools import reduce

mylist = [2,4,3,4,56,7,8]

def mysum(x,y):
    return x + y

print (reduce(mysum,mylist))