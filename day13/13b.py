#!/usr/bin/env python3
from functools import reduce

def chinese_remainder(n, a):
    sum = 0
    prod = reduce(lambda a, b: a*b, n)
    for n_i, a_i in zip(n, a):
        p = prod // n_i
        sum += a_i * mul_inv(p, n_i) * p
    return sum % prod
 
 
 
def mul_inv(a, b):
    b0 = b
    x0, x1 = 0, 1
    if b == 1: return 1
    while a > 1:
        q = a // b
        a, b = b, a%b
        x0, x1 = x1 - q * x0, x0
    if x1 < 0: x1 += b0
    return x1
 
bus_lines = open("input.txt").read().splitlines()[1].split(",")

n=[]
a=[]
for index, bus in enumerate(bus_lines):
    if bus != "x":
        n.append(int(bus))
        a.append((-index) % int(bus))
print(chinese_remainder(n,a))