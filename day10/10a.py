#!/usr/bin/env python3
from collections import defaultdict

with open("input.txt") as f:
    input = [0] + sorted([int(x) for x in f.read().splitlines()])

input.append((max(input)+ 3))

count = defaultdict(int)
for i in range(1, len(input)):
    count[input[i]-input[i-1]] += 1
print(count[1]*count[3])


