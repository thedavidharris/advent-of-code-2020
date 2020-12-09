#!/usr/bin/env python3
from collections import defaultdict

with open("input.txt") as f:
    instructions = [(op, int(arg)) for op, arg in [x.split() for x in f.read().splitlines()]]


executed = set()
i = 0
acc = 0

while True:
    if i in executed:
        print(acc)
        exit(0)
    executed.add(i)
    instruction = instructions[i][0]
    value = instructions[i][1]
    if instruction == "acc":
        acc += value
        i += 1
    if instruction == "jmp":
        i += value
    if instruction == "nop":
        i += 1
