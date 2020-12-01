#!/usr/bin/env python3
import itertools
import math

with open('input.txt', 'r') as f:
    print(math.prod(next(i for i in itertools.combinations(list(map(int, f.read().splitlines())), 3) if sum(i) == 2020)))