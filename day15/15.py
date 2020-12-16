#!/usr/bin/env pypy3
input = [6,3,15,13,1,0]
memory = {}
previous = None
numturns = 30000000

for index, val in enumerate(input):
    memory[previous] = index - 1
    previous = val

for i in range(len(input), numturns):
    if previous not in memory:
        x = 0
    else:
        x = i - 1 - memory[previous]
    memory[previous] = i - 1
    previous = x
print(x)