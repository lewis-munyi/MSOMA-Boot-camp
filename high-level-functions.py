from math import sqrt, pi, pow

def identity(k):
    return k

def cube(k):
    return pow(k,3)

def summation(n,term):
    total, k = 0, 1
    k = 1
    while k <= n:
        total = k
        total += term(k)
        k += 1
    return total
