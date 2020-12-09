#!/usr/bin/env python3
with open("input.txt") as f:
    instructions = [(op, int(arg)) for op, arg in [x.split() for x in f.read().splitlines()]]


def solve(ops):
    executed = set()
    i = 0
    acc = 0

    while i < len(ops):
        if i in executed:
            return None
        executed.add(i)
        instruction = ops[i][0]
        value = ops[i][1]
        if instruction == "acc":
            acc += value
            i += 1
        if instruction == "jmp":
            i += value
        if instruction == "nop":
            i += 1
    return acc

for i in range(len(instructions)):
    newList = instructions[:]
    newList[i] = ("nop", instructions[i][1])
    answer = solve(newList)
    if answer:
        print(answer)
