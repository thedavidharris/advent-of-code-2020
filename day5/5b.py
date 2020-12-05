#!/usr/bin/env python3

from itertools import groupby
from operator import itemgetter

print([list(map(itemgetter(1), g)) for k,g in groupby(enumerate(set(range(1024)) - set([int(line.replace("F", "0").replace("B", "1").replace("L", "0").replace("R", "1"), 2) for line in open('input.txt', 'r').read().splitlines()])),  key=lambda x: x[0] - x[1])][1][0])