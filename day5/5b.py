#!/usr/bin/env python3

import more_itertools

print([list(group) for group in more_itertools.consecutive_groups(set(range(1024)) - set([int(line.replace("F", "0").replace("B", "1").replace("L", "0").replace("R", "1"), 2) for line in open('input.txt', 'r').read().splitlines()]))][1][0])