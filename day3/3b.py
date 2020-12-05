#!/usr/bin/env python3
from math import prod

print((lambda m:prod(sum(line[i*dx %len(line)] == '#' for i,line in enumerate(m[::dy])) for dx,dy in [(3,1),(1,1),(5,1),(7,1),(1,2)]))(open('input.txt').read().splitlines()))