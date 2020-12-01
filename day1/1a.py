#!/usr/bin/env python3
import itertools
import math

print(math.prod(next(i for i in itertools.combinations(list(map(int, open('input.txt', 'r').read().splitlines())), 2) if sum(i) == 2020)))